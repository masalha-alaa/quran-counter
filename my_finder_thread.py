from functools import lru_cache
# import regex as re
import re
from my_data_loader import MyDataLoader
from PySide6.QtCore import Signal, QThread, QMutex
from arabic_reformer import reform_regex, alamaat_waqf_regex, diacritics_regex, arabic_alphabit
from nltk.stem.isri import ISRIStemmer
from itertools import permutations


class FinderThread(QThread):
    class SingleCache:
        def __init__(self):
            self.key = ""
            self.value = ""

    MY_CACHE_MUTEX = QMutex()
    result_ready = Signal(str, int, tuple, float, QThread)
    dia_or_waqf = rf"(?:(?={re.escape(alamaat_waqf_regex)})|(?={re.escape(diacritics_regex)}))"
    char_followed_by_dia_or_waqf = re.compile(rf"\[?[{''.join(arabic_alphabit)+' '}]+\]?{dia_or_waqf}")
    my_cache = SingleCache()

    def __init__(self, thread_id=None):
        super().__init__()
        self._thread_id = thread_id
        self.df = MyDataLoader.get_data()
        self._working_col = MyDataLoader.get_working_col()
        self.arabic_stemmer = ISRIStemmer()
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
                 root_flag):
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

    def _prep_data(self):
        if self.root_flag:
            new_text = self._get_root(self.initial_word).strip()
        elif self.full_word:
            new_text = self.initial_word.strip()
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
            if not self.maintain_words_order and num_of_search_words > 1:
                separator = f" {alamaat_waqf_regex}"
                new_text = '|'.join([separator.join(perm) for perm in permutations(new_text.split(separator))])

            new_text = f"({new_text})"  # capturing group

            beginning_of_word = r"(?: |^)"
            end_of_word = r"(?: |$)"
            # beginning_of_word = r"\b"
            # end_of_word = r"\b"
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
                matches_in_verse = [(cumsum[i], cumsum[i] + len(word)) for i, word in enumerate(split_verse) if re.match(rf"{w}$", self._get_root(word))]
            else:
                matches_in_verse = [m.span(1) for m in re.finditer(w, verse)]
            if matches_in_verse:
                # [(surah_num, verse_num, verse, [spans]), (...), ...]
                all_matches.append((int(row.name), i + 1, verse, matches_in_verse))
                number_of_matches += len(matches_in_verse)
            # if i % 100 == 0:
            #     QCoreApplication.processEvents()
        return (all_matches if all_matches else None), number_of_matches, len(all_matches) > 0, len(all_matches)

    def _actually_find_word(self, w, surah_nums=None):
        if surah_nums is None:
            data = self.df
        else:
            data = self.df.loc[surah_nums]
        if data.empty:
            spans, number_of_matches, index_mask, number_of_verses = [], [], [], []
        else:
            spans, number_of_matches, index_mask, number_of_verses = zip(*data.apply(lambda row: self._find_in_surah(row, w), axis=1))  # NOTE: index is not retained
        # spans = chain.from_iterable(tup for lst in spans if lst is not None for tup in lst)
        # spans = (tup for lst in spans if lst is not None for tup in lst)
        spans = [tup for lst in spans if lst is not None for tup in lst]
        # return spans, sum(number_of_matches), index_mask, sum(number_of_verses), data[np.array(index_mask)].index
        return spans, sum(number_of_matches), index_mask, sum(number_of_verses), data[list(index_mask)].index

    def _find_word(self, w):
        if not self.root_flag:  # TODO: check if needed
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
        surah_nums = results[-1]
        # cache results for next time
        if len(prefix) > 0:
            FinderThread.MY_CACHE_MUTEX.lock()
            FinderThread.my_cache.key = w[:-1]
            FinderThread.my_cache.value = surah_nums
            FinderThread.MY_CACHE_MUTEX.unlock()

        spans, total_number_of_matches, index_mask, total_number_of_verses, _ = results
        return spans, total_number_of_matches, sum(index_mask), total_number_of_verses

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
