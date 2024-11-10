import re
from functools import lru_cache
from PySide6.QtCore import Signal, QThread
from collections import defaultdict
from arabic_reformer import diacritics_regex
from tabs_management.table_headers import WordTableHeaders
from my_widgets.lazy_table_widget import CustomTableRow


class WordBoundsFinderThread(QThread):
    result_ready = Signal(list, float, QThread)
    _diacritics_regex = re.compile(diacritics_regex)

    def __init__(self, diacritics_sensitive=True, thread_id=None):
        super().__init__()
        self._thread_id = thread_id
        self._matches = []
        self._diacritics_sensitive = diacritics_sensitive

    def set_data(self, matches, diacritics_sensitive):
        self._matches = matches
        self._diacritics_sensitive = diacritics_sensitive

    @lru_cache(maxsize=1000)
    def remove_diacritics(self, word):
        return WordBoundsFinderThread._diacritics_regex.sub("", word)

    def run(self):
        # print(f"word bounds start {id(self)}")
        counts = defaultdict(list)
        for surah_num, verse_num, verse, spans in self._matches:
            for span in spans:
                word_start = verse.rfind(" ", 0, span[0]) + 1
                word_end = verse.find(" ", span[1])
                if word_end == -1:
                    word_end = len(verse)
                word = verse[word_start:word_end]
                if not self._diacritics_sensitive:
                    word = self.remove_diacritics(word)
                if word in counts and surah_num == counts[word][-1][0] and verse_num == counts[word][-1][1]:
                    counts[word][-1].extend((word_start, word_end))
                else:
                    counts[word].append([surah_num, verse_num, word_start, word_end])

        rows = []
        for w, data in counts.items():
            row_results = [None] * len(WordTableHeaders)
            row_results[WordTableHeaders.WORD_TEXT_HEADER.value] = w
            row_results[WordTableHeaders.RESULTS_HEADER.value] = sum(((len(lst) - 2) // 2) for lst in data)
            rows.append(CustomTableRow(row_results, data))

        self._matches = []
        self.result_ready.emit(rows, self._thread_id, self)
        # print(f"word bounds end {id(self)}")
