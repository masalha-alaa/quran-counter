from yaml import safe_load
from datetime import datetime

from my_widgets.lazy_table_widget.my_lazy_table_widget import SortingOrder
from my_widgets.topic_lazy_table_widget import TopicLazyTableWidget
from tabs_management.table_headers import TopicTableHeaders
from my_widgets.tab_wrapper import TabWrapper
from my_utils.shared_data import SharedData
from my_utils.utils import resource_path, load_translation
from gui.detailed_display_dialog.my_topic_detailed_display_dialog import MyTopicDetailedDisplayDialog
from worker_threads.topic_populator_thread import TopicPopulatorThread
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem



class TopicTabWrapper(TabWrapper):
    def __init__(self, parent, latest_search_word='', latest_radio_button=''):
        super().__init__(parent, latest_search_word, latest_radio_button)
        self._last_thread_id = -1
        # self._surah_index = safe_load(open(resource_path("surah_index.yml"), encoding='utf-8', mode='r'))
        self.detailed_topic_display_dialog = MyTopicDetailedDisplayDialog(SharedData.app_language)
        self.lazy_topic_results_table:TopicLazyTableWidget|None = None
        SharedData.ui.allResultsCheckbox.setVisible(False)
        self._setup_events()

    def init(self):
        self.lazy_topic_results_table = SharedData.ui.topicResultsTableWidget
        self.lazy_topic_results_table.set_item_selection_changed_callback(self.topic_results_selection_changed)
        self.lazy_topic_results_table.set_item_double_clicked_callback(self.topic_results_item_double_clicked)

    def _setup_events(self):
        pass

    def clear(self):
        self.lazy_topic_results_table.clear()
        self.lazy_topic_results_table.save_values([])

    def retranslate_ui(self):
        self.lazy_topic_results_table.retranslate_ui()

    def switch_colorize_state_without_firing(self, checked, enabled):
        self.detailed_topic_display_dialog.switch_colorize_state_without_firing(checked, enabled)

    def populate_results(self):
        self.update_config(SharedData.search_word, SharedData.ui.searchOptionsButtonGroup.checkedId())
        thread_id = datetime.now().timestamp()
        topic_finder_thread = TopicPopulatorThread(SharedData.ui.allResultsCheckbox.isChecked(), thread_id)
        topic_finder_thread.set_data(SharedData.all_matches)
        topic_finder_thread.result_ready.connect(self.on_find_topics_completed)
        self._add_thread(topic_finder_thread)
        topic_finder_thread.start()

    def on_find_topics_completed(self, counts, thread_id, caller_thread):
        caller_thread.result_ready.disconnect(self.on_find_topics_completed)
        self._remove_thread(caller_thread)
        # reject older threads?
        if thread_id < self._last_thread_id:
            return

        self._last_thread_id = thread_id
        self.lazy_topic_results_table.clear()
        self.lazy_topic_results_table.save_values(counts)
        self.lazy_topic_results_table.sort(TopicTableHeaders.SCORE_HEADER, SortingOrder.DESCENDING)

    def topic_results_selection_changed(self, selected_items: list[list]):
        total = sum(int(row[TopicTableHeaders.RESULTS_HEADER.value].text()) for row in selected_items)
        SharedData.ui.topicSum.setText(str(total))

    def topic_results_item_double_clicked(self, item: QTableWidgetItem):
        metadata = SharedData.ui.topicResultsTableWidget.item(item.row(), TopicTableHeaders.METADATA_POSITION.value).data(Qt.ItemDataRole.UserRole)
        if load_translation(SharedData.translator, resource_path(f"translations/word_detailed_display_{SharedData.app_language.value}.qm")):
            self.detailed_topic_display_dialog.set_language(SharedData.app_language)
        self.detailed_topic_display_dialog.set_data(metadata)
        # self.detailed_topic_display_dialog.open()
        self.detailed_topic_display_dialog.exec()
