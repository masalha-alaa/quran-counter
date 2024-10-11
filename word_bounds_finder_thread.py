from PySide6.QtCore import Signal, QThread
from collections import defaultdict


class WordBoundsFinderThread(QThread):
    result_ready = Signal(list, QThread)

    def __init__(self):
        super().__init__()
        self._matches = None

    def set_matches(self, matches):
        self._matches = matches

    def run(self):
        counts = defaultdict(int)
        for surah_num, verse_num, verse, spans in self._matches:
            for span in spans:
                word_start = verse.rfind(" ", 0, span[0]) + 1
                word_end = verse.find(" ", span[1], -1)
                counts[verse[word_start:word_end]] += 1
        self._matches = None
        self.result_ready.emit([f"{i + 1}. {w}:\t{c}" for i,(w,c) in enumerate(counts.items())], self)
