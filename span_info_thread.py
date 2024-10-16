import re
from PySide6.QtCore import Signal, QThread
from PySide6.QtGui import QTextCursor
from arabic_reformer import is_diacritic


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

    def __init__(self, huroof_maani_are_words=True, waw_is_a_word=True):
        super().__init__()
        self.text = None
        self.cursor: None | QTextCursor = None
        self.huroof_maani_are_words = huroof_maani_are_words
        self.waw_is_a_word = waw_is_a_word
        self.info = SpanInfo()

    def set_text(self, text: str):
        self.text = text
        self.cursor = None

    def set_text_cursor(self, cursor: QTextCursor):
        self.text = None
        self.cursor = cursor

    def run(self):
        if self.cursor is not None:
            self.text = self.cursor.selection().toPlainText()
        for word in self.text.split():
            if not self.verse_mark_regex_ptrn.search(word):
                self.info.words_in_selection += 1
                for ch in word:
                    if not is_diacritic(ch):
                        self.info.letters_in_selection += 1

        self.result_ready.emit(self.info, self)


