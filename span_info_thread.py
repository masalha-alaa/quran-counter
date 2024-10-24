import re
from PySide6.QtCore import Signal, QThread, QCoreApplication
from PySide6.QtGui import QTextCursor
from arabic_reformer import is_diacritic, normalize_letter, alif_khunjariyah
from cursor_position_info import CursorPositionInfo
from my_data_loader import MyDataLoader
from arabic_reformer import rub_el_hizb_mark
from enum import Enum, auto
from json import load
from random import choice


class NGrams(Enum):
    UNIGRAMS = auto()
    BIGRAMS = auto()
    TRIGRAMS = auto()


class SpanInfo:
    def __init__(self):
        self.surah_name = ""
        self.surah_num = ""
        self.metadata = None
        self.letters_from_beginning_of_surah = 0
        self.letters_from_beginning_of_quran = 0
        self.letters_in_selection = 0
        self.most_repeated_letter = ""
        self.words_from_beginning_of_surah = 0
        self.words_from_beginning_of_quran = 0
        self.words_in_selection = 0
        self.surah_exclusive_words = []
        self.surah_exclusive_bigrams = []
        self.surah_exclusive_trigrams = []

    @property
    def surah_exclusive_uni_random(self):
        chosen = choice(self.surah_exclusive_words)
        return f"{chosen[0]} ({chosen[1]})"

    @property
    def surah_exclusive_bi_random(self):
        chosen = choice(self.surah_exclusive_bigrams)
        return f"{chosen[0]} ({chosen[1]})"

    @property
    def surah_exclusive_tri_random(self):
        chosen = choice(self.surah_exclusive_trigrams)
        return f"{chosen[0]} ({chosen[1]})"

    def __repr__(self):
        return (f"{self.surah_name = }\n"
                f"{self.letters_from_beginning_of_surah = }\n"
                f"{self.letters_from_beginning_of_quran = }\n"
                f"{self.letters_in_selection = }\n"
                f"{self.most_repeated_letter = }\n"
                f"{self.words_from_beginning_of_surah = }\n"
                f"{self.words_from_beginning_of_quran = }\n"
                f"{self.words_in_selection = }\n"
                f"{self.surah_exclusive_words = }\n"
                f"{self.surah_exclusive_bigrams = }\n"
                f"{self.surah_exclusive_trigrams = }\n"
                )


class SpanInfoThread(QThread):
    result_ready = Signal(SpanInfo, float, QThread)
    verse_mark_regex_ptrn = re.compile(r"[\d()]")
    waikanna = ["وَيْكَأَنَّ", "وَيْكَأَنَّهُۥ"]

    def __init__(self, thread_id=0, surah_name="", count_waw_as_a_word=True, count_waikaana_as_two_words=True,
                 metadata=None):
        super().__init__()
        self._surah_name = surah_name
        self._thread_id = thread_id
        self.text_iter = None
        self.count_waw_as_a_word = count_waw_as_a_word
        self.count_waikaana_as_two_words = count_waikaana_as_two_words
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
        for word in self.text_iter:
            if not self.verse_mark_regex_ptrn.search(word):
                if not is_diacritic(word) and word != rub_el_hizb_mark:
                    if word in self.waikanna:
                        if self.count_waikaana_as_two_words:
                            self.info.words_in_selection += 2
                        else:
                            self.info.words_in_selection += 1
                    elif self.count_waw_as_a_word and word.startswith("و") and not MyDataLoader.is_waw_part_of_word(word):
                        self.info.words_in_selection += 2
                    else:
                        self.info.words_in_selection += 1

                for ch in word:
                    if ch == alif_khunjariyah or not is_diacritic(ch):
                        ch = normalize_letter(ch)
                        letters[ch] = letters.get(ch, 0) + 1
                        self.info.letters_in_selection += 1
            QCoreApplication.processEvents()
        self.info.most_repeated_letter = max(letters.items(), key=lambda x: x[1], default="")

        try:
            self.result_ready.emit(self.info, self._thread_id, self)
            # try catch is for debug only - exception isn't thrown in non-debug mode
        except RuntimeError as e:
            print(e)
