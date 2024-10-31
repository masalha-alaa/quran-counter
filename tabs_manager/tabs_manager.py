from my_widgets.lazy_list_widget import LazyListWidgetWrapper, CustomListWidgetItem, CustomResultsSortEnum, CustomRow
from word_bounds_results_subtext_getter import WordBoundsResultsSubtextGetter
from surah_results_subtext_getter import SurahResultsSubtextGetter
from gui.detailed_display_dialog.my_word_detailed_display_dialog import MyWordDetailedDisplayDialog
from gui.detailed_display_dialog.my_surah_detailed_display_dialog import MySurahDetailedDisplayDialog
from my_widgets.tab_wrapper import TabWrapper
from PySide6.QtCore import Slot


class TabsManager:
    def __init__(self, ui,  language):
        self.lazy_text_browser_verses_results = ui.foundVerses
        self.lazy_surah_results_list = None
        self.lazy_word_results_list = None

        self._init_surah_results_tab(ui.surahResultsListWidget)
        self._init_words_results_tab(ui.wordResultsListWidget)

        self.detailed_word_display_dialog = MyWordDetailedDisplayDialog(language)
        self.detailed_surah_display_dialog = MySurahDetailedDisplayDialog(language)

        ui.found_verses.set_colorize(ui.colorizeCheckbox.isChecked())
        self.verse_tab_wrapper = TabWrapper(ui.ayatTab, latest_radio_button=ui.searchOptionsButtonGroup.checkedId())
        self.surah_tab_wrapper = TabWrapper(ui.surahTab, latest_radio_button=ui.searchOptionsButtonGroup.checkedId())
        self.word_tab_wrapper = TabWrapper(ui.wordsTab, latest_radio_button=ui.searchOptionsButtonGroup.checkedId())

        ui.tabWidget.setCurrentIndex(0)

        self._setup_events(ui)

    def _setup_events(self, ui):
        ui.tabWidget.currentChanged.connect(self._tab_changed)
        ui.colorizeCheckbox.stateChanged.connect(self._colorize_toggled)
        ui.diacriticsCheckbox.stateChanged.connect(self._toggle_diacritics)
        ui.allResultsCheckbox.stateChanged.connect(self._toggle_all_surah_results)
        ui.filterButton.clicked.connect(self._filter_button_clicked)
        ui.clearFilterButton.clicked.connect(self._clear_filter_button_clicked)
        ui.sortPushButton.clicked.connect(self._sort_surah_results_clicked)
        ui.wordsSortPushButton.clicked.connect(self._sort_word_results_clicked)

    def _init_surah_results_tab(self, surahResultsListWidget):
        self.lazy_surah_results_list = LazyListWidgetWrapper(surahResultsListWidget, subtext_getter=SurahResultsSubtextGetter(), supported_methods=[CustomResultsSortEnum.BY_NUMBER, CustomResultsSortEnum.BY_NAME, CustomResultsSortEnum.BY_RESULT_ASCENDING, CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.lazy_surah_results_list.set_item_selection_changed_callback(self.surah_results_selection_changed)
        self.lazy_surah_results_list.set_item_double_clicked_callback(self.surah_results_item_double_clicked)

    def _init_words_results_tab(self, wordResultsListWidget):
        self.lazy_word_results_list = LazyListWidgetWrapper(wordResultsListWidget,
                                                            subtext_getter=WordBoundsResultsSubtextGetter(),
                                                            supported_methods=[CustomResultsSortEnum.BY_NAME,
                                                                               CustomResultsSortEnum.BY_RESULT_ASCENDING,
                                                                               CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.lazy_word_results_list.set_item_selection_changed_callback(self.word_bounds_results_selection_changed)
        self.lazy_word_results_list.set_item_double_clicked_callback(self.word_bounds_results_item_double_clicked)

    def _colorize_toggled(self, state):
        self.found_verses.reset_iter_and_refresh(self._all_matches, state)

    def _toggle_diacritics(self, state):
        self._populate_word_results(self.search_word)

    def _toggle_all_surah_results(self, state):
        self._populate_surah_results()

    @Slot()
    def _clear_filter_button_clicked(self):
        self.filter_text_browser(range(len(self._all_matches)))
        self.ui.clearFilterButton.setEnabled(False)

    @Slot()
    def _filter_button_clicked(self):
        if self._disambiguator.is_activated():
            self.show_disambiguation_dialog()
        else:
            self.show_gpt_activation_dialog()

    def filter_text_browser(self, indices: list | range):
        self.clear_results()
        matches_num, matched_verses_num, surah_count = self.found_verses.save_values_and_refresh(self._all_matches, indices)
        self.matches_number = str(matches_num)
        self.matches_number_surahs = str(surah_count)
        self.matches_number_verses = str(matched_verses_num)

    def _sort_surah_results_clicked(self):
        def _surah_sorting_done():
            self.ui.sortPushButton.setEnabled(True)
            current_sorting = self.lazy_surah_results_list.get_current_sorting()
            self.ui.sortMethodLabel.setText(translate_text(current_sorting.to_string()))

        self.ui.sortPushButton.setEnabled(False)
        self.lazy_surah_results_list.set_sorting_done_callback(_surah_sorting_done)
        self.lazy_surah_results_list.switch_order()
        self.lazy_surah_results_list.sort()

    def _sort_word_results_clicked(self):
        def _word_sorting_done():
            self.ui.wordsSortPushButton.setEnabled(True)
            current_sorting = self.lazy_word_results_list.get_current_sorting()
            self.ui.wordSortMethodLabel.setText(translate_text(current_sorting.to_string()))

        self.ui.wordsSortPushButton.setEnabled(False)
        self.lazy_word_results_list.set_sorting_done_callback(_word_sorting_done)
        self.lazy_word_results_list.switch_order()
        self.lazy_word_results_list.sort()
        current_sorting = self.lazy_word_results_list.get_current_sorting()
        self.ui.wordSortMethodLabel.setText(translate_text(current_sorting.to_string()))

    def on_word_found_complete(self):
        match self.ui.tabWidget.currentIndex():
            case TabIndex.VERSES.value:
                self._populate_verses_results(number_of_matches)
            case TabIndex.SURAHS.value:
                self._populate_surah_results()
            case TabIndex.WORDS.value:
                self._populate_word_results(initial_word)

    def _tab_changed(self, tab_index):
        current_word, current_radio = self.search_word, self.ui.searchOptionsButtonGroup.checkedId()
        match tab_index:
            case TabIndex.VERSES.value:
                if self.verse_tab_wrapper.config_changed(current_word, current_radio):
                    self._populate_verses_results(self.matches_number)
            case TabIndex.SURAHS.value:
                if self.surah_tab_wrapper.config_changed(current_word, current_radio):
                    self._populate_surah_results()
            case TabIndex.WORDS.value:
                if self.word_tab_wrapper.config_changed(current_word, current_radio):
                    self._populate_word_results(self.search_word)