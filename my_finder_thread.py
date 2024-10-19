from functools import lru_cache
import re
from my_data_loader import MyDataLoader
from PySide6.QtCore import Signal, QThread
from arabic_reformer import reform_regex
from nltk.stem.isri import ISRIStemmer


class FinderThread(QThread):
    result_ready = Signal(str, int, tuple, QThread)

    def __init__(self):
        super().__init__()
        self.df = MyDataLoader.get_data()
        self._working_col = MyDataLoader.get_working_col()
        self.arabic_stemmer = ISRIStemmer()
        self.initial_word = None
        self.alif_alif_maksura_variations = None
        self.ya_variations = None
        self.ta_variations = None
        self.full_word = None
        self.beginning_of_word_flag = None
        self.end_of_word_flag = None

        self._final_word = None
        self._words_num = None

    def set_data(self, word, alif_alif_maksura_variations, ya_variations, ta_variations, full_word, beginning_of_word_flag, end_of_word_flag, root_flag):
        self.initial_word = word
        self.alif_alif_maksura_variations = alif_alif_maksura_variations
        self.ya_variations = ya_variations
        self.ta_variations = ta_variations
        self.full_word = full_word
        self.beginning_of_word_flag = beginning_of_word_flag
        self.end_of_word_flag = end_of_word_flag
        self.root_flag = root_flag

    def _prep_data(self):
        if self.root_flag:
            new_text = self._get_root(self.initial_word)
        else:
            new_text = self.initial_word

        # ignore diacritics
        # TODO: make checkbox?
        new_text = reform_regex(new_text,
                                alif_alif_maksura_variations=self.alif_alif_maksura_variations,
                                ya_variations=self.ya_variations,
                                ta_variations=self.ta_variations)

        num_of_search_words = len(new_text.split())
        if not self.root_flag:
            new_text = f"({new_text})"  # capturing group
            beginning_of_word = r"[ ^]"
            end_of_word = r"[ ,$]"
            if self.full_word:
                new_text = beginning_of_word + rf"{new_text}" + end_of_word
            else:
                if self.beginning_of_word_flag:
                    new_text = beginning_of_word + rf"{new_text}"
                if self.end_of_word_flag:
                    new_text = rf"{new_text}" + end_of_word
        self._final_word = new_text
        self._words_num = num_of_search_words

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
                matches_in_verse = [(cumsum[i], cumsum[i] + len(word)) for i, word in enumerate(split_verse) if re.match(w, self._get_root(word))]
            else:
                matches_in_verse = [m.span(1) for m in re.finditer(w, verse, flags=re.M)]
            if matches_in_verse:
                # [(surah_num, verse_num, verse, [spans]), (...), ...]
                all_matches.append((int(row.name)+1, i + 1, verse, matches_in_verse))
                number_of_matches += len(matches_in_verse)
        return (all_matches if all_matches else None), number_of_matches, len(all_matches) > 0, len(all_matches)

    def _find_word(self, w):
        spans, number_of_matches, found_in_surah, number_of_verses = zip(*self.df.apply(lambda row: self._find_in_surah(row, w), axis=1))  # NOTE: index is not retained
        # spans = chain.from_iterable(tup for lst in spans if lst is not None for tup in lst)
        # spans = (tup for lst in spans if lst is not None for tup in lst)
        spans = [tup for lst in spans if lst is not None for tup in lst]
        return spans, sum(number_of_matches), sum(found_in_surah), sum(number_of_verses)

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
            self.result_ready.emit(self.initial_word, words_num, result, self)
        # print(f"finder end {id(self)}")
