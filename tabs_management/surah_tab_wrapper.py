from yaml import safe_load
from datetime import datetime
from my_widgets.surah_lazy_table_widget import SurahLazyTableWidget
from tabs_management.table_headers import SurahTableHeaders
from my_widgets.tab_wrapper import TabWrapper
from my_utils.shared_data import SharedData
from worker_threads.surah_finder_thread import SurahFinderThread
from my_utils.utils import resource_path, load_translation
from gui.detailed_display_dialog.my_surah_detailed_display_dialog import MySurahDetailedDisplayDialog
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem



class SurahTabWrapper(TabWrapper):
    def __init__(self, parent, latest_search_word='', latest_radio_button=''):
        super().__init__(parent, latest_search_word, latest_radio_button)
        self._last_thread_id = -1
        self._surah_index = safe_load(open(resource_path("surah_index.yml"), encoding='utf-8', mode='r'))
        self.detailed_surah_display_dialog = MySurahDetailedDisplayDialog(SharedData.app_language)
        self.lazy_surah_results_table:SurahLazyTableWidget|None = None
        self._setup_events()

    def init(self):

        self.lazy_surah_results_table = SharedData.ui.surahResultsTableWidget
        self.lazy_surah_results_table.set_item_selection_changed_callback(self.surah_results_selection_changed)
        self.lazy_surah_results_table.set_item_double_clicked_callback(self.surah_results_item_double_clicked)

    def _setup_events(self):
        SharedData.ui.allResultsCheckbox.stateChanged.connect(self._toggle_all_surah_results)

    def clear(self):
        self.lazy_surah_results_table.clear()
        self.lazy_surah_results_table.save_values([])

    def retranslate_ui(self):
        self.lazy_surah_results_table.retranslate_ui()

    def _toggle_all_surah_results(self, state):
        self.populate_results()

    def populate_results(self):
        self.update_config(SharedData.search_word, SharedData.ui.searchOptionsButtonGroup.checkedId())
        thread_id = datetime.now().timestamp()
        surah_finder_thread = SurahFinderThread(self._surah_index, SharedData.ui.allResultsCheckbox.isChecked(), thread_id)
        surah_finder_thread.set_data(SharedData.all_matches, SharedData.ui.allResultsCheckbox.isChecked())
        surah_finder_thread.result_ready.connect(self.on_find_surahs_completed)
        self._add_thread(surah_finder_thread)
        surah_finder_thread.start()

    def on_find_surahs_completed(self, counts, thread_id, caller_thread):
        caller_thread.result_ready.disconnect(self.on_find_surahs_completed)
        self._remove_thread(caller_thread)
        # reject older threads?
        if thread_id < self._last_thread_id:
            return

        self._last_thread_id = thread_id
        self.lazy_surah_results_table.clear()
        self.lazy_surah_results_table.save_values(counts)
        self.lazy_surah_results_table.sort(SurahTableHeaders.SURAH_NAME_HEADER)

    def surah_results_selection_changed(self, selected_items: list[list]):
        total = sum(int(row[SurahTableHeaders.RESULTS_HEADER.value].text()) for row in selected_items)
        SharedData.ui.surahResultsSum.setText(str(total))

    def surah_results_item_double_clicked(self, item: QTableWidgetItem):
        metadata = SharedData.ui.surahResultsTableWidget.item(item.row(), SurahTableHeaders.METADATA_POSITION.value).data(Qt.ItemDataRole.UserRole)
        if load_translation(SharedData.translator, resource_path(f"translations/word_detailed_display_{SharedData.app_language.value}.qm")):
            self.detailed_surah_display_dialog.set_language(SharedData.app_language)
        self.detailed_surah_display_dialog.set_data(metadata)
        # self.detailed_word_display_dialog.open()
        self.detailed_surah_display_dialog.exec()
