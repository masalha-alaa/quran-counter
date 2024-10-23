from PySide6.QtCore import Signal, QThread
from collections import defaultdict
from lazy_list_widget import CustomRow


class SurahFinderThread(QThread):
    result_ready = Signal(list, QThread)

    def __init__(self, surah_index: dict, include_zeros=False):
        super().__init__()
        self._matches = []
        self._surah_index = surah_index
        self._include_zeros = include_zeros

    def set_data(self, matches, include_zeros):
        self._matches = matches
        self._include_zeros = include_zeros

    def run(self):
        # print(f"surah start {id(self)}")
        count_by_surah = defaultdict(list)
        for surah_num, verse_num, verse, spans in self._matches:
            if surah_num not in count_by_surah:
                count_by_surah[surah_num] = [len(spans), [(surah_num, verse_num, spans)]]
            else:
                count_by_surah[surah_num][0] += len(spans)
                count_by_surah[surah_num][1].append((surah_num, verse_num, spans))

        rows = []
        for surah_num, surah_name in self._surah_index.items():
            count = count_by_surah.get(surah_num, [0, []])
            if count[0] == 0 and not self._include_zeros:
                continue
            matches_num, verse_nums_and_spans = count
            rows.append(CustomRow(f"{surah_name} <{surah_num}>:\t\t{matches_num}", verse_nums_and_spans))

        self._matches = []
        self.result_ready.emit(rows, self)
        # print(f"surah end {id(self)}")
