from functools import lru_cache
# import regex as re
import re
from my_utils.my_data_loader import MyDataLoader
from my_utils.globals import beginning_of_word, end_of_word
from PySide6.QtCore import Signal, QThread, QMutex
from arabic_reformer import reform_regex, alamaat_waqf_regex, diacritics_regex, arabic_alphabit, remove_diacritics, normalize_alif
from nltk.stem.isri import ISRIStemmer
from itertools import permutations
from difflib import SequenceMatcher
from preprocessing import Preprocessor
from models.match_item import MatchItem
from text_validators.arabic_with_regex_validator import ArabicWithRegexValidator
from algos.related_words import RelatedWords
from models.finder_result_object import FinderResultObject


class FinderThread(QThread):
    class SingleCache:
        def __init__(self):
            self.key = ""
            self.value = ""

    MY_CACHE_MUTEX = QMutex()
    result_ready = Signal(str, int, FinderResultObject, float, QThread)
    dia_or_waqf = rf"(?:(?={re.escape(alamaat_waqf_regex)})|(?={re.escape(diacritics_regex)}))"
    char_followed_by_dia_or_waqf = re.compile(rf"\[?[{''.join(arabic_alphabit)+' '}]+\]?{dia_or_waqf}")
    MIN_CLOSE_MATCH_RAW_THRESHOLD = 6
    MAX_CLOSE_MATCH_RAW_THRESHOLD = 10
    my_cache = SingleCache()
    REGEX_CHARS_FOR_ROOT_FIND = r"()?:|[]"
    nested_brackets_regex = re.compile(r"\[([^\[\]]*)\[(.*?)\]([^\[\]]*)\]")

    def __init__(self, thread_id=None):
        super().__init__()
        self._thread_id = thread_id
        self.df = MyDataLoader.get_data()
        self.related_words_algo = RelatedWords()
        self._working_col = MyDataLoader.get_working_col()
        self.arabic_stemmer = ISRIStemmer()
        self.preprocessor = Preprocessor()
        self.initial_word = None
        self.alif_alif_maksura_variations = None
        self.ya_variations = None
        self.ta_variations = None
        self.maintain_words_order = None
        self.optional_al_tarif = None
        self.full_word = None
        self.beginning_of_word_flag = None
        self.end_of_word_flag = None
        self.root_flag = None
        self._activate_root_finder_fallback = False
        self.regular_expression = None
        self.close_match = None
        self.close_match_threshold = None
        self.related_words = None
        self.related_words_threshold = None
        self._default_close_match_threshold = 6
        self._default_related_words_threshold = 1

        self._final_word = None
        self._words_num = None

    def set_data(self,
                 word,
                 alif_alif_maksura_variations,
                 ya_variations,
                 ta_variations,
                 maintain_words_order,
                 optional_al_tarif,  # TODO: Currently ignored, need to implement
                 full_word,
                 beginning_of_word_flag,
                 end_of_word_flag,
                 root_flag,
                 regular_expression,
                 close_match,
                 related_words,
                 close_match_threshold:int=None,
                 related_words_threshold:int=None):
        self.initial_word = word
        self.alif_alif_maksura_variations = alif_alif_maksura_variations
        self.ya_variations = ya_variations
        self.ta_variations = ta_variations
        self.maintain_words_order = maintain_words_order
        self.optional_al_tarif = optional_al_tarif
        self.full_word = full_word
        self.beginning_of_word_flag = beginning_of_word_flag
        self.end_of_word_flag = end_of_word_flag
        self.root_flag = root_flag
        self.regular_expression = regular_expression
        self.close_match = close_match
        self.close_match_threshold = (close_match_threshold if isinstance(close_match_threshold, int) else self._default_close_match_threshold) / 10
        self.related_words = related_words
        self.related_words_threshold = (related_words_threshold if isinstance(related_words_threshold, int) else self._default_related_words_threshold)

    @lru_cache(maxsize=8)
    def reform_regex_with_local_params(self, txt):
        return reform_regex(txt,
                            alif_alif_maksura_variations=self.alif_alif_maksura_variations,
                            ya_variations=self.ya_variations,
                            ta_variations=self.ta_variations,
                            chars_to_not_add_diacritics_to=ArabicWithRegexValidator.SUPPORTED_REGEX_CHARS if (self.optional_al_tarif or self.regular_expression) else FinderThread.REGEX_CHARS_FOR_ROOT_FIND if self.root_flag else None,
                            alamat_waqf_after_space=not self.regular_expression)

    def _prep_data(self):
        if self.root_flag:
            # new_text = self._get_root(self.initial_word).strip()
            # check if root in root list
            try:
                new_text = MyDataLoader.root_to_words.loc[(preprocessed_w := self.preprocessor.normalize_for_root(self.initial_word)), 'regex']
            except KeyError:
                try:
                    # check if word in words list
                    new_text = MyDataLoader.word_to_words.loc[preprocessed_w, 'regex']
                except KeyError:
                    # stem and check if root in root list
                    new_text = self._get_root(self.initial_word).strip()
                    try:
                        new_text = MyDataLoader.root_to_words.loc[preprocessed_w, 'regex']
                    except KeyError:
                        # activate fallback to compare against roots of all words
                        self._activate_root_finder_fallback = True
        elif self.full_word or self.close_match or self.related_words:
            new_text = self.initial_word.strip()
        else:
            new_text = self.initial_word

        # TODO: add safety checks to prevent unintended combinations (e.g. optional-al-tarif & regex together)
        #       (right now it's prevented in gui in main.py)

        if self.optional_al_tarif:
            al_tarif = "ال"
            optional_al_tarif = f"(?:{al_tarif})?"
            new_text = ' '.join([(optional_al_tarif + (w if not w.startswith(al_tarif) else w[len(al_tarif):]))
                        for w in re.split("\s+", new_text)])

        if not (self.close_match or self.related_words):
            new_text = self.reform_regex_with_local_params(new_text)
            if self.root_flag:
                new_text = self.flatten_nested_brackets(new_text)

        # print(new_text)
        num_of_search_words = len(new_text.split()) if not self.root_flag else 1

        if not (self.root_flag or self.close_match or self.related_words or self.regular_expression):
            if not self.maintain_words_order and num_of_search_words > 1:
                separator = f" {alamaat_waqf_regex}"
                new_text = '|'.join([separator.join(perm) for perm in permutations(new_text.split(separator))])

            new_text = f"({new_text})"  # capturing group

            if self.full_word:
                new_text = self.make_full_word(new_text)
            elif self.beginning_of_word_flag:
                    new_text = self.make_beginning_of_word(new_text)
            elif self.end_of_word_flag:
                    new_text = self.make_end_of_word(new_text)
        elif self.regular_expression:
            new_text = f"({new_text})"
            new_text = self.strip_extra_braces(new_text)

        self._final_word = new_text
        self._words_num = num_of_search_words

    def make_full_word(self, w):
        new_w = beginning_of_word + rf"{w}" + end_of_word
        return new_w

    def make_beginning_of_word(self, w):
        new_w = beginning_of_word + rf"{w}"
        return new_w

    def make_end_of_word(self, w):
        new_w = rf"{w}" + end_of_word
        return new_w

    def flatten_nested_brackets(self, pattern):
        """
        ChatGPT (take it with a grain of salt)
        Flattens nested square brackets in a regex pattern by merging their content.
        """
        while True:
            # Find nested brackets using a regex
            match = FinderThread.nested_brackets_regex.search(pattern)
            if not match:
                break  # No more nested brackets

            # Extract content inside the brackets
            outer_start = match.group(1)  # Content before inner bracket
            inner = match.group(2)  # Content of inner bracket
            outer_end = match.group(3)  # Content after inner bracket

            # Merge the inner and outer content into a single bracket
            merged = f"[{outer_start}{inner}{outer_end}]"

            # Replace the nested structure with the merged one
            pattern = pattern[:match.start()] + merged + pattern[match.end():]

        return pattern

    def strip_extra_braces(self, text):
        remove_idx = set()
        i, j = 1, len(text) - 2
        found_braces = True
        while i < j:
            if text[i] == "(" and text[j] == ")":
                if found_braces:
                    remove_idx.update([i, j])
                else:
                    found_braces = True
                i += 1
                j -= 1
            elif text[i] == "(":
                found_braces = False
                j -= 1
            elif text[j] == ")":
                found_braces = False
                i += 1
            else:
                found_braces = False
                i += 1
                j -= 1
        if remove_idx:
            modified_text = ""
            for i in range(len(text)):
                if i not in remove_idx:
                    modified_text += text[i]
            return modified_text
        return text

    def my_get_close_matches(self, word, sentence, threshold=0.6):
        matches = []
        offset = 0
        SEPARATOR = ' '
        for i, w in enumerate(sentence.split(SEPARATOR)):  # assuming one space separator
            ratio = SequenceMatcher(None, word, normalize_alif(remove_diacritics(w))).ratio()
            if ratio >= threshold:
                match = (offset, offset + len(w))
                matches.append(match)
            offset += len(w) + len(SEPARATOR)
        return matches

    def my_get_related_words(self, regex_pattern, sentence):
        matches = [m.span(1) for m in re.finditer(regex_pattern, sentence)]
        return matches


    def _find_in_surah(self, row, w):
        verses_clean_split = row[self._working_col]
        number_of_matches = 0
        all_matches = []
        for i, verse in enumerate(verses_clean_split):
            # re.sub("\uFEFB", "لا", verse) ?
            if self.root_flag:
                split_verse = verse.split()
                cumsum = [0]
                for j in range(len(split_verse)):
                    cumsum.append(cumsum[j] + len(split_verse[j]) + 1)
                matches_in_verse = [(cumsum[i], cumsum[i] + len(word)) for i, word in enumerate(split_verse) if re.match(rf"{w}$", self._get_root(word) if self._activate_root_finder_fallback else word)]
            elif self.close_match:
                matches_in_verse = self.my_get_close_matches(w, verse, threshold=self.close_match_threshold)
            elif self.related_words:
                matches_in_verse = self.my_get_related_words(w, verse)
            else:
                matches_in_verse = [m.span(1) for m in re.finditer(w, verse)]
            if matches_in_verse:
                match_item = MatchItem(surah_num=int(row.name),
                                       verse_num = i + 1,
                                       verse_text=verse,
                                       spans=matches_in_verse)
                all_matches.append(match_item)
                number_of_matches += len(matches_in_verse)
            # if i % 100 == 0:
            #     QCoreApplication.processEvents()
        return (all_matches if all_matches else None), number_of_matches, len(all_matches) > 0, len(all_matches)

    def _actually_find_word(self, w, surah_nums=None):
        paths = {}
        if surah_nums is None:
            data = self.df
        else:
            data = self.df.loc[surah_nums]
        if data.empty:
            spans, number_of_matches, index_mask, number_of_verses = [], [], [], []
        else:
            if self.related_words:
                paths, related_words = self.get_paths_to_related_words(w, self.related_words_threshold)
                # TODO: tri regex?
                w = self._final_word = self.make_full_word(f"({'|'.join(related_words)})")
                # w = self._final_word = f"({'|'.join(related_words)})"
            # print(w)
            spans, number_of_matches, index_mask, number_of_verses = zip(*data.apply(lambda row: self._find_in_surah(row, w), axis=1))  # NOTE: index is not retained
        # spans = chain.from_iterable(tup for lst in spans if lst is not None for tup in lst)
        # spans = (tup for lst in spans if lst is not None for tup in lst)
        spans = [tup for lst in spans if lst is not None for tup in lst]
        # return spans, sum(number_of_matches), index_mask, sum(number_of_verses), data[np.array(index_mask)].index
        return spans, sum(number_of_matches), index_mask, sum(number_of_verses), data[list(index_mask)].index, paths

    def _find_word(self, w):
        if not (self.root_flag or self.close_match or self.related_words or self.regular_expression):  # TODO: check if needed
            # get prefix of word (everything excluding last letter and its harakat)
            *_, prefix_idx = FinderThread.char_followed_by_dia_or_waqf.finditer(w)
            prefix = w[:prefix_idx.span()[0]]

            # check if prefix is cached, and take cache if available
            # (the cache is the sura numbers the prefix was found it)
            FinderThread.MY_CACHE_MUTEX.lock()
            if FinderThread.my_cache.key == prefix:
                prefix_surah_idx_cache = FinderThread.my_cache.value
                FinderThread.MY_CACHE_MUTEX.unlock()
            else:
                prefix_surah_idx_cache = None
            FinderThread.MY_CACHE_MUTEX.unlock()
        else:
            prefix = ""
            prefix_surah_idx_cache = None

        # search word in relevant surahs (cached surah numbers, or all surahs if no cache)
        results = self._actually_find_word(w, prefix_surah_idx_cache)
        surah_nums = results[-2]
        # cache results for next time
        if len(prefix) > 0:
            FinderThread.MY_CACHE_MUTEX.lock()
            FinderThread.my_cache.key = w[:-1]
            FinderThread.my_cache.value = surah_nums
            FinderThread.MY_CACHE_MUTEX.unlock()

        spans, total_number_of_matches, index_mask, total_number_of_verses, _, paths = results
        results_obj = FinderResultObject(spans, total_number_of_matches, sum(index_mask), total_number_of_verses, paths)
        return results_obj

    def get_paths_to_related_words(self, word, cutoff=1):
        related_words_paths = self.related_words_algo.get_by_distance(word, cutoff)
        new_words = map(self.reform_regex_with_local_params, related_words_paths.keys())
        return related_words_paths, new_words

    @lru_cache(maxsize=256)
    def _get_root(self, w):
        return self.arabic_stemmer.stem(w)

    def run(self):
        # print(f"finder start {id(self)}")
        self._prep_data()
        word = self._final_word
        words_num = self._words_num
        if word:
            result = self._find_word(word)
            self.result_ready.emit(self.initial_word, words_num, result, self._thread_id, self)
        # print(f"finder end {id(self)}")
