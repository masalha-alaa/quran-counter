import re
from PySide6.QtCore import Signal, QThread, QCoreApplication, QMutex
from PySide6.QtGui import QTextCursor
from arabic_reformer import is_diacritic, normalize_letter, alif_khunjariyah, rub_el_hizb_mark, sujood_mark
from models.cursor_position_info import CursorPositionInfo
from my_utils.my_data_loader import MyDataLoader
from enum import Enum, auto
from random import choice
from my_utils.insensitive_to_last_diacritic_dict import InsensitiveToLastDiacriticDict


class NGrams(Enum):
    UNIGRAMS = auto()
    BIGRAMS = auto()
    TRIGRAMS = auto()


class SpanInfo:
    def __init__(self):
        self.surah_name = ""
        self.surah_num = 0
        self.metadata = None
        self.letters_from_beginning_of_surah = 0
        self.letters_from_beginning_of_quran = 0
        self.letters_in_selection = 0
        self.letters_histogram = [0] * len(set(MyDataLoader.letters_histogram_index.values()))
        self.surah_unique_words_num = 0
        self.most_repeated_letter = ""
        self.most_repeated_word = ""
        self.words_from_beginning_of_surah = 0
        self.words_from_beginning_of_quran = 0
        self.words_in_selection = 0
        self.surah_exclusive_words = []
        self.surah_exclusive_words_diff_roots = []
        self.surah_exclusive_bigrams = []
        self.surah_exclusive_trigrams = []

    def _my_choose_random(self, population, default=None):
        if len(population):
            chosen = ["", 0]
            max_retries = 5
            while (not chosen[0] or chosen[0] == "و" or chosen[0].endswith(" و")) and max_retries > 0:
                chosen = choice(population)
                max_retries -= 1
            return chosen
        return default

    @property
    def surah_exclusive_uni_random(self):
        chosen = self._my_choose_random(self.surah_exclusive_words)
        return "" if chosen is None else f"{chosen[0]} ({chosen[1]})"

    @property
    def surah_exclusive_uni_diff_roots_random(self):
        chosen = self._my_choose_random(self.surah_exclusive_words_diff_roots)
        return "" if chosen is None else f"{chosen[0]} ({chosen[1]})"

    @property
    def surah_exclusive_bi_random(self):
        chosen = self._my_choose_random(self.surah_exclusive_bigrams)
        return "" if chosen is None else f"{chosen[0]} ({chosen[1]})"

    @property
    def surah_exclusive_tri_random(self):
        chosen = self._my_choose_random(self.surah_exclusive_trigrams)
        return "" if chosen is None else f"{chosen[0]} ({chosen[1]})"

    def __repr__(self):
        return (f"{self.surah_name = }\n"
                f"{self.letters_from_beginning_of_surah = }\n"
                f"{self.letters_from_beginning_of_quran = }\n"
                f"{self.letters_in_selection = }\n"
                f"{self.letters_histogram = }\n"
                f"{self.surah_unique_words_num = }\n"
                f"{self.most_repeated_letter = }\n"
                f"{self.most_repeated_word = }\n"
                f"{self.words_from_beginning_of_surah = }\n"
                f"{self.words_from_beginning_of_quran = }\n"
                f"{self.words_in_selection = }\n"
                f"{self.surah_exclusive_words = }\n"
                f"{self.surah_exclusive_bigrams = }\n"
                f"{self.surah_exclusive_trigrams = }\n"
                )


class SpanInfoThread(QThread):
    # RUNNING_THREADS_MUTEX = QMutex()
    result_ready = Signal(SpanInfo, float, QThread)
    verse_mark_regex_ptrn = re.compile(r"[\d()]")
    waikanna = ["وَيْكَأَنَّ", "وَيْكَأَنَّهُۥ"]

    class WawWordsMatrixCol(Enum):
        WAW_PART_OF_WORD = 0
        COUNT_WAW_SEPARATE = auto()
        IS_HARF_MAANA = auto()
        COUNT_HARF_MAANA = auto()

    # [2:] because i'm assuming [1] is a diacritic that belongs to the waw
    waw_words_count_matrix = lambda idx, word: {
        (False, False, False, False): [None, word],
        (False, False, False, True): [None, word],
        (False, False, True, False): [None, None],
        (False, False, True, True): [None, word],
        (False, True, False, False): [word[:2], word[2:]],
        (False, True, False, True): [word[:2], word[2:]],
        (False, True, True, False): [word[:2], None],
        (False, True, True, True): [word[:2], word[2:]],
        (True, False, False, False): [None, word],
        (True, False, False, True): [None, word],
        (True, False, True, False): [None, None],
        (True, False, True, True): [None, word],
        (True, True, False, False): [None, word],
        (True, True, False, True): [None, word],
        (True, True, True, False): [None, None],
        (True, True, True, True): [None, word],
    }[idx]

    def __init__(self, thread_id=0, surah_name="",
                 count_waw_as_a_word=True,
                 count_waikaana_as_two_words=True,
                 count_huroof_maani=True,
                 metadata=None):
        super().__init__()
        self._surah_name = surah_name
        self._thread_id = thread_id
        self.text_iter = None
        self.count_waw_as_a_sep_word = count_waw_as_a_word
        self.count_waikaana_as_two_words = count_waikaana_as_two_words
        self.count_huroof_maani = count_huroof_maani
        self.info = SpanInfo()
        self.info.metadata = metadata

    @property
    def thread_id(self) -> int:
        return self._thread_id

    def from_text(self, text: str):
        self.text_iter = iter(text.split())

    def from_text_cursor(self, cursor: QTextCursor):
        self.text_iter = iter(cursor.selection().toPlainText().split())

    def from_ref(self, start: CursorPositionInfo, end: CursorPositionInfo):
        self.text_iter = MyDataLoader.iterate_over_verses_words(start.surah_num, start.verse_num,
                                                                start.word_num_in_verse,
                                                                end.surah_num, end.verse_num,
                                                                end.word_num_in_verse)

    def run(self):
        self.info.surah_name = self._surah_name
        self.info.surah_num = MyDataLoader.get_surah_num(self.info.surah_name)
        letters = {}
        words = InsensitiveToLastDiacriticDict()
        waw_words_matrix_idx = [False] * len(SpanInfoThread.WawWordsMatrixCol)
        for word in self.text_iter:
            if not self.verse_mark_regex_ptrn.search(word):
                if not is_diacritic(word) and word not in [rub_el_hizb_mark, sujood_mark]:
                    if word in self.waikanna:
                        words[word] = words.get(word, 0) + 1
                        if self.count_waikaana_as_two_words:
                            self.info.words_in_selection += 2
                        else:
                            self.info.words_in_selection += 1
                    elif word.startswith("و"):
                        word_after_waw = word[2:]  # [2:] because i'm assuming [1] is a diacritic that belongs to the waw
                        # if we're asked to count waw as part of word, then no need to check if it's part of word, just count 1.
                        waw_part_of_word = not self.count_waw_as_a_sep_word or MyDataLoader.is_waw_part_of_word(word)
                        # if we're asked to count huroof maani, don't check if it's a harf maana, just count it.
                        is_harf_maana = self.count_huroof_maani or MyDataLoader.is_harf_maani(word_after_waw)
                        waw_words_matrix_idx[SpanInfoThread.WawWordsMatrixCol.WAW_PART_OF_WORD.value] = waw_part_of_word
                        waw_words_matrix_idx[SpanInfoThread.WawWordsMatrixCol.COUNT_WAW_SEPARATE.value] = self.count_waw_as_a_sep_word
                        waw_words_matrix_idx[SpanInfoThread.WawWordsMatrixCol.IS_HARF_MAANA.value] = is_harf_maana
                        waw_words_matrix_idx[SpanInfoThread.WawWordsMatrixCol.COUNT_HARF_MAANA.value] = self.count_huroof_maani
                        waw, rest_of_word = SpanInfoThread.waw_words_count_matrix(tuple(waw_words_matrix_idx), word)

                        # SpanInfoThread.RUNNING_THREADS_MUTEX.lock()
                        # print()
                        # print(f"{word = }")
                        # print(f"{word[:2] = }")
                        # print(f"{waw_part_of_word = }")
                        # print(f"{self.count_waw_as_a_sep_word = }")
                        # print(f"{is_harf_maana = }")
                        # print(f"{self.count_huroof_maani = }")
                        # print(f"{waw = }")
                        # print(f"{rest_of_word = }")
                        # SpanInfoThread.RUNNING_THREADS_MUTEX.unlock()

                        if waw:
                            self.info.words_in_selection += 1
                            words[word] = words.get(waw, 0) + 1
                        if rest_of_word:
                            self.info.words_in_selection += 1
                            words[rest_of_word] = words.get(rest_of_word, 0) + 1
                    elif not self.count_huroof_maani and MyDataLoader.is_harf_maani(word):
                        pass  # skip it
                    else:
                        self.info.words_in_selection += 1
                        words[word] = words.get(word, 0) + 1

                for ch in word:
                    if ch == alif_khunjariyah or (not is_diacritic(ch) and not ch in [rub_el_hizb_mark, sujood_mark]):
                        ch = normalize_letter(ch)
                        letters[ch] = letters.get(ch, 0) + 1
                        self.info.letters_in_selection += 1
                        try:
                            self.info.letters_histogram[MyDataLoader.letters_histogram_index[ch]] += 1
                        except KeyError:
                            print(f"{ch} not in hist")
            QCoreApplication.processEvents()
        self.info.most_repeated_letter = max(letters.items(), key=lambda x: x[1], default="")
        self.info.most_repeated_word = max(words.items(), key=lambda x: x[1], default="")
        self.info.surah_unique_words_num = len(words)

        try:
            self.result_ready.emit(self.info, self._thread_id, self)
            # try catch is for debug only - exception isn't thrown in non-debug mode
        except RuntimeError as e:
            print(e)
