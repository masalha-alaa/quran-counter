from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer


class TabWrapper(QWidget):
    REMOVE_THREAD_AFTER_MS = 500
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self, parent, latest_search_word='', latest_radio_button='', radio_threshold=None):
        super().__init__(parent)
        self.parent = parent
        self.latest_search_word = latest_search_word
        self.latest_radio_button = latest_radio_button
        self.radio_threshold = radio_threshold
        self.running_threads = set()

    def init(self):
        raise NotImplementedError

    def update_config(self, word, radio, radio_threshold=None):
        self.latest_search_word = word
        self.latest_radio_button = radio
        self.radio_threshold = radio_threshold

    def config_changed(self, word, radio, radio_threshold = None) -> bool:
        return self.latest_search_word != word or self.latest_radio_button != radio or (radio_threshold is not None and self.radio_threshold != radio_threshold)

    def _add_thread(self, thread):
        # TabWrapper.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.add(thread)
        # TabWrapper.RUNNING_THREADS_MUTEX.unlock()

    def _remove_thread(self, thread, after:int|None=None):
        # TabWrapper.RUNNING_THREADS_MUTEX.lock()
        QTimer.singleShot(TabWrapper.REMOVE_THREAD_AFTER_MS if after is None else after, lambda: self.running_threads.remove(thread))
        # TabWrapper.RUNNING_THREADS_MUTEX.unlock()

    def populate_results(self):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError
