import re
from PySide6.QtCore import Signal, QThread
from collections import defaultdict
from lazy_list_widget import CustomRow


class SurahFinderThread(QThread):
    result_ready = Signal(list, QThread)

    def __init__(self, surah_index: dict, include_zeros=False):
        super().__init__()
        self._matches = None
        self._surah_index = surah_index
        self._include_zeros = include_zeros

    def set_data(self, matches, include_zeros):
        self._matches = matches
        self._include_zeros = include_zeros

    def run(self):
        # print(f"surah start {id(self)}")
        count_by_surah = defaultdict(int)
        for surah_num, verse_num, verse, spans in self._matches:
            count_by_surah[surah_num] += len(spans)

        rows = []
        for surah_num, surah_name in self._surah_index.items():
            count = count_by_surah.get(surah_num, 0)
            if count == 0 and not self._include_zeros:
                continue
            rows.append(CustomRow(f"{surah_name} <{surah_num}>:\t\t{count}"))

        self._matches = None
        self.result_ready.emit(rows, self)
        # print(f"surah end {id(self)}")
