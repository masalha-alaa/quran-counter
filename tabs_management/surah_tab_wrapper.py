from yaml import safe_load
from my_widgets.lazy_table_widget import LazyTableWidgetWrapper, CustomTableWidgetItem
from tabs_management.surah_table_headers import SurahTableHeaders
from PySide6.QtWidgets import QTableWidgetItem
from tabs_management.surah_results_subtext_getter import SurahResultsSubtextGetter
from my_widgets.tab_wrapper import TabWrapper
from my_utils.shared_data import SharedData
from worker_threads.surah_finder_thread import SurahFinderThread
from my_utils.utils import  translate_text, resource_path, load_translation
from gui.detailed_display_dialog.my_surah_detailed_display_dialog import MySurahDetailedDisplayDialog


class SurahTabWrapper(TabWrapper):
    def __init__(self, parent, latest_search_word='', latest_radio_button=''):
        super().__init__(parent, latest_search_word, latest_radio_button)
        self._surah_index = safe_load(open(resource_path("surah_index.yml"), encoding='utf-8', mode='r'))
        self.detailed_surah_display_dialog = MySurahDetailedDisplayDialog(SharedData.app_language)
        self.lazy_surah_results_table:LazyTableWidgetWrapper|None = None
        self._setup_events()

    def init(self):
        headers = [None] * len(SurahTableHeaders)
        headers[SurahTableHeaders.SURAH_NAME_HEADER.value] = "اسم السورة"
        headers[SurahTableHeaders.SURAH_NUM_HEADER.value] = "رقم السورة"
        headers[SurahTableHeaders.RESULTS_HEADER.value] =  "عدد النتائج"
        self.lazy_surah_results_table = LazyTableWidgetWrapper(SharedData.ui.surahResultsTableWidget,
                                                               headers=headers)
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
        surah_finder_thread = SurahFinderThread(self._surah_index, SharedData.ui.allResultsCheckbox.isChecked())
        surah_finder_thread.set_data(SharedData.all_matches, SharedData.ui.allResultsCheckbox.isChecked())
        surah_finder_thread.result_ready.connect(self.on_find_surahs_completed)
        self._add_thread(surah_finder_thread)
        surah_finder_thread.start()

    def on_find_surahs_completed(self, counts, caller_thread):
        caller_thread.result_ready.disconnect(self.on_find_surahs_completed)
        self._remove_thread(caller_thread)
        # TODO: reject older threads?

        self.lazy_surah_results_table.clear()
        self.lazy_surah_results_table.save_values(counts)
        self.lazy_surah_results_table.sort(SurahTableHeaders.SURAH_NAME_HEADER)

        SharedData.ui.sortPushButton.setEnabled(counts is not None and len(counts) > 0)

    def surah_results_selection_changed(self, selected_items: list):
        total = sum(int(item) for item in selected_items)
        SharedData.ui.surahResultsSum.setText(str(total))

    def surah_results_item_double_clicked(self, item):
        if load_translation(SharedData.translator, resource_path(f"translations/word_detailed_display_{SharedData.app_language.value}.qm")):
            self.detailed_surah_display_dialog.set_language(SharedData.app_language)
        self.detailed_surah_display_dialog.set_data(item)
        # self.detailed_word_display_dialog.open()
        self.detailed_surah_display_dialog.exec()
