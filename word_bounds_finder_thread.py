import re
from PySide6.QtCore import Signal, QThread
from collections import defaultdict
from arabic_reformer import diacritics_regex
from lazy_list_widget import CustomRow


class WordBoundsFinderThread(QThread):
    result_ready = Signal(defaultdict, QThread)

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
        counts = defaultdict(lambda: defaultdict(list))
        for surah_num, verse_num, verse, spans in self._matches:
            for span in spans:
                word_start = verse.rfind(" ", 0, span[0]) + 1
                word_end = verse.find(" ", span[1], -1)
                word = verse[word_start:word_end]
                if not self._diacritics_sensitive:
                    word = self._diacritics_regex.sub("", word)
                ref = (surah_num, verse_num)
                counts[word][ref].append((word_start, word_end))
        self._matches = None
        self.result_ready.emit([CustomRow(f"{w}:\t\t{sum(len(spans) for spans in data.values())}", data) for w,data in counts.items()], self)
