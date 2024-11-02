from my_widgets.tab_wrapper import TabWrapper
from my_utils.utils import  translate_text, resource_path, load_translation
from my_utils.shared_data import SharedData
from gui.detailed_display_dialog.my_word_detailed_display_dialog import MyWordDetailedDisplayDialog
from my_widgets.lazy_list_widget import LazyListWidgetWrapper, CustomListWidgetItem, CustomResultsSortEnum, CustomRow
from word_bounds_results_subtext_getter import WordBoundsResultsSubtextGetter
from worker_threads.word_bounds_finder_thread import WordBoundsFinderThread


class WordTabWrapper(TabWrapper):
    def __init__(self, parent, latest_search_word='', latest_radio_button=''):
        super().__init__(parent, latest_search_word, latest_radio_button)
        self.detailed_word_display_dialog = MyWordDetailedDisplayDialog(SharedData.app_language)
        self.lazy_word_results_list = None
        self.minimum_letters_restriction_lbl_stylesheet = SharedData.ui.minimum_letters_restriction_lbl.styleSheet()
        self._setup_events()

    def init(self):
        self.lazy_word_results_list = LazyListWidgetWrapper(SharedData.ui.wordResultsListWidget,
                                                            subtext_getter=WordBoundsResultsSubtextGetter(),
                                                            supported_methods=[CustomResultsSortEnum.BY_NAME,
                                                                               CustomResultsSortEnum.BY_RESULT_ASCENDING,
                                                                               CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.lazy_word_results_list.set_item_selection_changed_callback(self.word_bounds_results_selection_changed)
        self.lazy_word_results_list.set_item_double_clicked_callback(self.word_bounds_results_item_double_clicked)

    def clear(self):
        self.lazy_word_results_list.clear()
        self.lazy_word_results_list.save_values([])

    def _setup_events(self):
        SharedData.ui.diacriticsCheckbox.stateChanged.connect(self._toggle_diacritics)
        SharedData.ui.wordsSortPushButton.clicked.connect(self._sort_word_results_clicked)

    def _toggle_diacritics(self, state):
        self.populate_results(SharedData.search_word)

    def _sort_word_results_clicked(self):
        def _word_sorting_done():
            SharedData.ui.wordsSortPushButton.setEnabled(True)
            current_sorting_method = self.lazy_word_results_list.get_current_sorting()
            SharedData.ui.wordSortMethodLabel.setText(translate_text(current_sorting_method.to_string()))

        SharedData.ui.wordsSortPushButton.setEnabled(False)
        self.lazy_word_results_list.set_sorting_done_callback(_word_sorting_done)
        self.lazy_word_results_list.switch_order()
        self.lazy_word_results_list.sort()
        current_sorting = self.lazy_word_results_list.get_current_sorting()
        SharedData.ui.wordSortMethodLabel.setText(translate_text(current_sorting.to_string()))

    def populate_results(self, initial_word=''):
        if len(initial_word.strip()) < 2:
            self.lazy_word_results_list.clear()
            self.lazy_word_results_list.save_values([])
            SharedData.ui.minimum_letters_restriction_lbl.setStyleSheet(f"{self.minimum_letters_restriction_lbl_stylesheet} color: red;")
            return
        SharedData.ui.minimum_letters_restriction_lbl.setStyleSheet(self.minimum_letters_restriction_lbl_stylesheet)

        self.update_config(SharedData.search_word, SharedData.ui.searchOptionsButtonGroup.checkedId())
        word_bounds_finder_thread = WordBoundsFinderThread(SharedData.ui.diacriticsCheckbox.isChecked())
        word_bounds_finder_thread.set_data(SharedData.all_matches, SharedData.ui.diacriticsCheckbox.isChecked())
        word_bounds_finder_thread.result_ready.connect(self.on_find_word_bounds_completed)
        self._add_thread(word_bounds_finder_thread)
        word_bounds_finder_thread.start()

    def on_find_word_bounds_completed(self, counts, caller_thread: WordBoundsFinderThread):
        caller_thread.result_ready.disconnect(self.on_find_word_bounds_completed)
        self._remove_thread(caller_thread)
        # TODO: reject older threads?

        # self.lazy_word_results_list.clear()
        self.lazy_word_results_list.save_values(counts)
        # self.lazy_word_results_list.load_more_items()
        self.lazy_word_results_list.sort()
        current_sorting = self.lazy_word_results_list.get_current_sorting()
        SharedData.ui.wordSortMethodLabel.setText(translate_text(current_sorting.to_string()))
        SharedData.ui.wordsSortPushButton.setEnabled(counts is not None and len(counts) > 0)

    def word_bounds_results_selection_changed(self, selected_items: list[CustomListWidgetItem]):
        total = sum(int(WordBoundsResultsSubtextGetter.ptrn.search(item.text()).group(2)) for item in selected_items)
        SharedData.ui.wordSum.setText(str(total))

    def word_bounds_results_item_double_clicked(self, item: CustomRow):
        if load_translation(SharedData.translator, resource_path(f"translations/word_detailed_display_{SharedData.app_language.value}.qm")):
            self.detailed_word_display_dialog.set_language(SharedData.app_language)
        self.detailed_word_display_dialog.set_data(item)
        # self.detailed_word_display_dialog.open()
        self.detailed_word_display_dialog.exec()
