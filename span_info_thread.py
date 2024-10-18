import re
from PySide6.QtCore import Signal, QThread
from PySide6.QtGui import QTextCursor
from arabic_reformer import is_diacritic
from cursor_position_info import CursorPositionInfo
from my_data_loader import MyDataLoader


class SpanInfo:
    def __init__(self):
        self.letters_from_beginning_of_surah = 0
        self.letters_from_beginning_of_quran = 0
        self.letters_in_selection = 0
        self.words_from_beginning_of_surah = 0
        self.words_from_beginning_of_quran = 0
        self.words_in_selection = 0


class SpanInfoThread(QThread):
    result_ready = Signal(SpanInfo, QThread)
    verse_mark_regex_ptrn = re.compile(r"[\d()]")
    waikanna = ["وَيْكَأَنّ", "وَيْكَأَنَّهُۥ"]

    def __init__(self, thread_id=0, count_waw_as_a_word=True, count_waikaana_as_two_words=True):
        super().__init__()
        self._thread_id = thread_id
        self.text_iter = None
        self.count_waw_as_a_word = count_waw_as_a_word
        self.count_waikaana_as_two_words = count_waikaana_as_two_words
        self.info = SpanInfo()

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
        for word in self.text_iter:
            if not self.verse_mark_regex_ptrn.search(word):
                if not is_diacritic(word):
                    if self.count_waw_as_a_word and word.startswith("و") and not MyDataLoader.is_waw_part_of_word(word):
                        self.info.words_in_selection += 2
                    elif self.count_waikaana_as_two_words and word in SpanInfoThread.waikanna:
                        self.info.words_in_selection += 2
                    else:
                        self.info.words_in_selection += 1

                for ch in word:
                    if not is_diacritic(ch):
                        self.info.letters_in_selection += 1

        try:
            self.result_ready.emit(self.info, self)
            # try catch is for debug only - exception isn't thrown in non-debug mode
        except RuntimeError as e:
            print(e)


