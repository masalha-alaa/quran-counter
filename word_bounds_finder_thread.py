import re
from PySide6.QtCore import Signal, QThread
from collections import defaultdict
from arabic_reformer import diacritics_regex


class WordBoundsFinderThread(QThread):
    result_ready = Signal(list, QThread)

    def __init__(self, diacritics_sensitive=True):
        super().__init__()
        self._matches = None
        self._diacritics_sensitive = diacritics_sensitive
        self._diacritics_regex = re.compile(diacritics_regex)

    def set_matches(self, matches):
        self._matches = matches

    def set_diacritics_sensitive(self, sensitive):
        self._diacritics_sensitive = sensitive

    def run(self):
        counts = defaultdict(int)
        for surah_num, verse_num, verse, spans in self._matches:
            for span in spans:
                word_start = verse.rfind(" ", 0, span[0]) + 1
                word_end = verse.find(" ", span[1], -1)
                word = verse[word_start:word_end]
                if not self._diacritics_sensitive:
                    word = self._diacritics_regex.sub("", word)
                counts[word] += 1
        self._matches = None
        self.result_ready.emit([f"{w}:\t\t{c}" for i,(w,c) in enumerate(counts.items())], self)
