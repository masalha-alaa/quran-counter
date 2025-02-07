from typing import List
from PySide6.QtCore import Signal, QThread
from collections import defaultdict
from my_widgets.lazy_table_widget import CustomTableRow
from tabs_management.table_headers import TopicTableHeaders
from models.match_item import MatchItem


class TopicPopulatorThread(QThread):
    result_ready = Signal(list, float, QThread)

    def __init__(self, surah_index: dict, include_zeros=False, thread_id=None):
        super().__init__()
        self._thread_id = thread_id
        self._matches: List[MatchItem]= []

    def set_data(self, matches):
        self._matches = matches

    def run(self):
        # print(f"topic start {id(self)}")
        count_by_topic = defaultdict(list)
        for match_item in self._matches:
            topic, score = match_item.other['topic'], match_item.other['score']
            # score should be the same for all similar topics
            # if it's not, then it's probably a bug.
            # it came from exploding the verses list...
            count_by_topic[(topic, score)].append((match_item.surah_num, match_item.verse_num))

        rows = []
        for (topic, score), data in count_by_topic.items():
            row_results = [None] * len(TopicTableHeaders)
            row_results[TopicTableHeaders.TOPIC_NAME_HEADER.value] = topic
            row_results[TopicTableHeaders.SCORE_HEADER.value] = round(score * 100)
            row_results[TopicTableHeaders.RESULTS_HEADER.value] = len(data)
            rows.append(CustomTableRow(row_results, data))

        self._matches = []
        self.result_ready.emit(rows, self._thread_id, self)
        # print(f"topic end {id(self)}")
