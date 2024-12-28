from my_utils.my_data_loader import MyDataLoader
from PySide6.QtCore import Signal, QThread, QMutex
from models.topic_embeddings_model import TopicEmbeddingsModel
from models.match_item import MatchItem


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
        # topics, scores, verses = results['relevant_topics'], results['score'], results['verses']
        total_number_of_matches = total_number_of_verses = results.shape[0]
        if total_number_of_matches > 0:
            unique_surahs = set()
            spans = []
            for _, row in results.iterrows():
                topic, score, refs = row['relevant_topics'], row['score'], row['verses']
                surah, verse = refs.split(":")
                unique_surahs.add(surah)

                verse_txt = MyDataLoader.get_verse(surah, verse)
                # span = (0, len(verse_txt))
                span = (0, 0)  # i don't want to color...
                match_item = MatchItem(surah_num=int(surah),
                                       verse_num = int(verse),
                                       verse_text=verse_txt,
                                       other={"topic": topic, "score": score},
                                       spans=[span])
                spans.append(match_item)
            number_of_surahs = len(unique_surahs)
        else:
            spans = []
            number_of_surahs = 0
        return spans, total_number_of_matches, number_of_surahs, total_number_of_verses

    def is_model_initialized(self):
        return self.model.is_initialized

    def run(self):
        if self.topic:
            if not self.model.is_initialized:
                self.model.initialize()
                self.initialization_ready.emit(self._thread_id, self)
            result = self.model.get_relevant_verses(self.topic, 2, True)
            detailed_results = self.get_details(result)
            self.result_ready.emit(self.topic, detailed_results, self._thread_id, self)
