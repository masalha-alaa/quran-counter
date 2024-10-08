import os
import re
from cachetools import cached, LRUCache
from cachetools.keys import hashkey
import openai
from arabic_reformer.reformer import Reformer
from ast import literal_eval


class Disambiguator:
    # MAX_WORDS = (8192 / (1000/750))  # 6144
    MAX_WORDS = 700

    def __init__(self, openai_key=None):
        if openai_key is None:
            self._key = openai_key
        elif os.path.exists(openai_key):
            self._key = open(openai_key, mode='r').read()
        elif isinstance(openai_key, str):
            self._key = openai_key

        if self._key:
            openai.api_key = self._key

        self.reformer = Reformer()
        self.remove_ref = re.compile(r"^\d{,3}:\d{,3}:\s+", flags=re.M)

        # TODO: settings to choose model
        # self._gpt_model = "gpt-3.5-turbo"
        self._gpt_model = "gpt-4"
        # self._gpt_model = "GPT-4o"
        # self._gpt_model = "GPT-4o mini"

    @cached(cache=LRUCache(maxsize=128))
    def get_chatgpt_response(self, word):
        template = f"Write the different meanings of the Arabic word '{word}' in Arabic."
        template += "\n"
        template += "The final result must be only a dictionary s.t. the keys are 'meaning_1', 'meaning_2', 'meaning_3'... And the values are the meanings in Arabic. Don not write any English word, do not write aything other than the requested dictionary."
        response = openai.chat.completions.create(
            # model="gpt-3.5-turbo",
            model="gpt-4",
            messages=[{"role": "system", "content": "Respond in a valid JSON format only."},
                      {"role": "user", "content": template}],
            max_tokens=500,  # Adjust according to your needs
            temperature=0.7,  # Adjust for creativity vs. determinism
        )
        return response.choices[0].message.content

    @cached(cache={}, key=lambda word, verses, verses_ref, meaning, query: hashkey(word, verses_ref, meaning))
    def get_relevant_verses(self, word, meaning, verses_ref, verses):
        """
        :param verses_ref: for caching purposes only
        """
        verses_for_prompt = [[]]
        verse_counter = 0
        words_count = 0
        for verse in verses:
            words_count += len(verse.split())
            if words_count > Disambiguator.MAX_WORDS:
                verses_for_prompt.append([])
                verse_counter = 0
                words_count = 0
            verses_for_prompt[-1].append(f"{verse_counter + 1}. {self.remove_ref.sub('', verse)}")
            verse_counter += 1

        ptr = self.reformer.reform_regex(word)
        responses = []
        for verses_for_prompt_chunk in verses_for_prompt:
            variations = set()
            for verse in verses_for_prompt_chunk:
                variations.update(re.findall(ptr, verse))
            variations = '/'.join(variations)
            prompt = f"First, for each of the given verses from the Holy Quran, infer the meaning of the word '{word.strip()}' as it appears in each verse. The word may appear in different variations and with different diacritics, such as {variations} ..."
            prompt += "\n"
            prompt += "If the given word doesn't appear in any variation, skip the verse."
            prompt += "\n"
            prompt += f"Second, return a Python list consisting of the numbers of the verses in which the meaning of the word '{word.strip()}' that you inferred corresponds to the following meaning: '{meaning}'."
            prompt += "\n"
            prompt += "Do not return the inferred meanings (they are just for helping you in the task). I only need the numbers of the verses."
            prompt += "\n"
            prompt += "The verses:"
            prompt += "\n"
            prompt += '\n\n'.join(verses_for_prompt_chunk)

            # print("///////////////////////////////////////")
            # print(prompt)
            # print("///////////////////////////////////////")

            response = openai.chat.completions.create(
                # TODO: settings to choose model
                # model="gpt-3.5-turbo",  # it really sucks
                model="gpt-4",  # good
                messages=[
                    {"role": "system", "content": "Respond in a valid python list only."},
                    {"role": "user", "content": prompt.strip()}],
                max_tokens=500,  # Adjust according to your needs
                temperature=0.7,  # Adjust for creativity vs. determinism
            )
            # TODO: exception handling
            # print(f"gpt response = {response.choices[0].message.content}")
            responses.append(literal_eval(response.choices[0].message.content))

        assert len(responses) == len(verses_for_prompt), "Number of responses does not correspond to number of requests"

        counter = len(verses_for_prompt[0])
        for i in range(1, len(responses)):
            for j, verse_number in enumerate(responses[i]):
                responses[i][j] += counter
            counter += len(verses_for_prompt[i])

        return [i - 1 for i in sum(responses, [])]
