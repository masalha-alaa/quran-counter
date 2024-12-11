import pandas as pd
from my_utils.my_data_loader import MyDataLoader
from PySide6.QtCore import Signal, QThread, QMutex
from models.topic_embeddings_model import TopicEmbeddingsModel


class TopicFinderThread(QThread):

    MY_CACHE_MUTEX = QMutex()
    initialization_ready = Signal(float, QThread)
    result_ready = Signal(str, tuple, float, QThread)

    def __init__(self, thread_id=None):
        super().__init__()
        self._thread_id = thread_id
        self.df = MyDataLoader.get_data()
        self.model = TopicEmbeddingsModel()
        self._working_col = MyDataLoader.get_working_col()
        self.topic = None

    def set_data(self, topic):
        self.topic = topic

    def get_details(self, results):
        total_number_of_matches = total_number_of_verses = results.shape[0]
        surah_verse = pd.DataFrame(results.str.split(":").tolist())
        surahs, verses = surah_verse[0], surah_verse[1]
        number_of_surahs = surahs.nunique()
        spans = []
        for s, v in zip(surahs.values, verses.values):
            verse_txt = MyDataLoader.get_verse(s, v)
            # span = (0, len(verse_txt))
            span = (0, 0)  # i don't want to color...
            spans.append((int(s), int(v), verse_txt, span))
        return spans, total_number_of_matches, number_of_surahs, total_number_of_verses

    def is_model_initialized(self):
        return self.model.is_initialized

    def run(self):
        if self.topic:
            if not self.model.is_initialized:
                self.model.initialize()
                self.initialization_ready.emit(self._thread_id, self)
            result = self.model.get_relevant_verses(self.topic)
            detailed_results = self.get_details(result)
            self.result_ready.emit(self.topic, detailed_results, self._thread_id, self)
        # print(f"topic finder end {id(self)}")
