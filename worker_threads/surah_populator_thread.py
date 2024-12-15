from typing import List
from PySide6.QtCore import Signal, QThread, Qt
from PySide6.QtWidgets import QTableWidgetItem
from collections import defaultdict
from my_widgets.lazy_table_widget import CustomTableRow, TableDataType
from tabs_management.table_headers import SurahTableHeaders
from models.match_item import MatchItem


class SurahPopulatorThread(QThread):
    result_ready = Signal(list, float, QThread)

    def __init__(self, surah_index: dict, include_zeros=False, thread_id=None):
        super().__init__()
        self._thread_id = thread_id
        self._matches: List[MatchItem]= []
        self._surah_index = surah_index
        self._include_zeros = include_zeros

    def set_data(self, matches, include_zeros):
        self._matches = matches
        self._include_zeros = include_zeros

    def run(self):
        # print(f"surah start {id(self)}")
        count_by_surah = defaultdict(list)
        for match_item in self._matches:
            surah_num = match_item.surah_num
            verse_num = match_item.verse_num
            spans = match_item.spans
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
            row_results = [None] * len(SurahTableHeaders)
            row_results[SurahTableHeaders.SURAH_NAME_HEADER.value] = surah_name
            row_results[SurahTableHeaders.SURAH_NUM_HEADER.value] = int(surah_num)
            row_results[SurahTableHeaders.RESULTS_HEADER.value] = int(matches_num)
            rows.append(CustomTableRow(row_results, verse_nums_and_spans))

        self._matches = []
        self.result_ready.emit(rows, self._thread_id, self)
        # print(f"surah end {id(self)}")
