from yaml import safe_load
from my_widgets.lazy_list_widget import LazyListWidgetWrapper, CustomListWidgetItem, CustomResultsSortEnum, CustomRow
from surah_results_subtext_getter import SurahResultsSubtextGetter
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
        self.lazy_surah_results_list = None
        self._setup_events()

    def init(self):
        self.lazy_surah_results_list = LazyListWidgetWrapper(SharedData.ui.surahResultsListWidget, subtext_getter=SurahResultsSubtextGetter(), supported_methods=[CustomResultsSortEnum.BY_NUMBER, CustomResultsSortEnum.BY_NAME, CustomResultsSortEnum.BY_RESULT_ASCENDING, CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.lazy_surah_results_list.set_item_selection_changed_callback(self.surah_results_selection_changed)
        self.lazy_surah_results_list.set_item_double_clicked_callback(self.surah_results_item_double_clicked)

    def _setup_events(self):
        SharedData.ui.allResultsCheckbox.stateChanged.connect(self._toggle_all_surah_results)
        SharedData.ui.sortPushButton.clicked.connect(self._sort_surah_results_clicked)

    def clear(self):
        self.lazy_surah_results_list.clear()
        self.lazy_surah_results_list.save_values([])

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

        # self.lazy_surah_results_list.clear()
        self.lazy_surah_results_list.save_values(counts)
        # self.lazy_surah_results_list.load_more_items()
        self.lazy_surah_results_list.sort()
        current_sorting = self.lazy_surah_results_list.get_current_sorting()
        SharedData.ui.sortMethodLabel.setText(translate_text(current_sorting.to_string()))
        SharedData.ui.sortPushButton.setEnabled(counts is not None and len(counts) > 0)

    def surah_results_selection_changed(self, selected_items: list[CustomListWidgetItem]):
        total = sum(int(SurahResultsSubtextGetter.ptrn.search(item.text()).group(3)) for item in selected_items)
        SharedData.ui.surahResultsSum.setText(str(total))

    def surah_results_item_double_clicked(self, item: CustomRow):
        if load_translation(SharedData.translator, resource_path(f"translations/word_detailed_display_{SharedData.app_language.value}.qm")):
            self.detailed_surah_display_dialog.set_language(SharedData.app_language)
        self.detailed_surah_display_dialog.set_data(item)
        # self.detailed_word_display_dialog.open()
        self.detailed_surah_display_dialog.exec()

    def _sort_surah_results_clicked(self):
        def _surah_sorting_done():
            SharedData.ui.sortPushButton.setEnabled(True)
            current_sorting_method = self.lazy_surah_results_list.get_current_sorting()
            SharedData.ui.sortMethodLabel.setText(translate_text(current_sorting_method.to_string()))

        SharedData.ui.sortPushButton.setEnabled(False)
        self.lazy_surah_results_list.set_sorting_done_callback(_surah_sorting_done)
        self.lazy_surah_results_list.switch_order()
        self.lazy_surah_results_list.sort()
