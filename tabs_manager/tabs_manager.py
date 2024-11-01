from enum import Enum
from yaml import safe_load
from my_widgets.lazy_list_widget import LazyListWidgetWrapper, CustomListWidgetItem, CustomResultsSortEnum, CustomRow
from word_bounds_results_subtext_getter import WordBoundsResultsSubtextGetter
from surah_results_subtext_getter import SurahResultsSubtextGetter
from gui.detailed_display_dialog.my_word_detailed_display_dialog import MyWordDetailedDisplayDialog
from gui.detailed_display_dialog.my_surah_detailed_display_dialog import MySurahDetailedDisplayDialog
from my_widgets.tab_wrapper import TabWrapper
from my_utils.shared_data import SharedData
from chat_gpt.disambiguator import Disambiguator
from gui.disambiguation_dialog.my_disambiguation_dialog import MyDidsambiguationDialog
from worker_threads.surah_finder_thread import SurahFinderThread
from worker_threads.word_bounds_finder_thread import WordBoundsFinderThread
from PySide6.QtCore import Slot
from PySide6.QtCore import QTranslator, QThread, QTimer
from my_utils.utils import AppLang, translate_text, resource_path, load_translation
from PySide6.QtWidgets import QDialog
from gui.waiting_dialog.my_waiting_dialog import MyWaitingDialog
from chat_gpt.ask_gpt_thread import AskGptThread
from gui.openai_key_setup_dialog.my_openai_key_setup_dialog import MyOpenAiKeySetupDialog



class TabIndex(Enum):
    VERSES = 0
    SURAHS = 1
    WORDS = 2


class TabsManager:
    REMOVE_THREAD_AFTER_MS = 500
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self, ui):
        self.ui = ui
        self._translator = QTranslator()
        self.activate_gpt_dialog = MyOpenAiKeySetupDialog(SharedData.app_language)
        self.running_threads = set()

        self.lazy_text_browser_verses_results = self.ui.foundVerses
        self.lazy_surah_results_list = None
        self.lazy_word_results_list = None

        self._init_surah_results_tab()
        self._init_words_results_tab()

        self.detailed_word_display_dialog = MyWordDetailedDisplayDialog(SharedData.app_language)
        self.detailed_surah_display_dialog = MySurahDetailedDisplayDialog(SharedData.app_language)

        self.found_verses.set_colorize(self.ui.colorizeCheckbox.isChecked())
        self.verse_tab_wrapper = TabWrapper(self.ui.ayatTab, latest_radio_button=self.ui.searchOptionsButtonGroup.checkedId())
        self.surah_tab_wrapper = TabWrapper(self.ui.surahTab, latest_radio_button=self.ui.searchOptionsButtonGroup.checkedId())
        self.word_tab_wrapper = TabWrapper(self.ui.wordsTab, latest_radio_button=self.ui.searchOptionsButtonGroup.checkedId())

        self.ui.tabWidget.setCurrentIndex(0)
        self._init_surah_results_tab()
        self._init_words_results_tab()

        self._disambiguator = Disambiguator("open_ai_key.txt")
        # self._disambiguator = Disambiguator("TEST")
        self.disambiguation_dialog = MyDidsambiguationDialog(self._disambiguator, SharedData.app_language)

        self.ask_gpt_thread = AskGptThread(self._disambiguator)
        self.waiting_dialog = MyWaitingDialog(SharedData.app_language)

        self._surah_index = safe_load(open(resource_path("surah_index.yml"), encoding='utf-8', mode='r'))
        self.minimum_letters_restriction_lbl_stylesheet = self.ui.minimum_letters_restriction_lbl.styleSheet()

        self._setup_events()

    def _setup_events(self):
        self.ui.tabWidget.currentChanged.connect(self._tab_changed)
        self.ui.colorizeCheckbox.stateChanged.connect(self._colorize_toggled)
        self.ui.diacriticsCheckbox.stateChanged.connect(self._toggle_diacritics)
        self.ui.allResultsCheckbox.stateChanged.connect(self._toggle_all_surah_results)
        self.ui.filterButton.clicked.connect(self._filter_button_clicked)
        self.ui.clearFilterButton.clicked.connect(self._clear_filter_button_clicked)
        self.ui.sortPushButton.clicked.connect(self._sort_surah_results_clicked)
        self.ui.wordsSortPushButton.clicked.connect(self._sort_word_results_clicked)

    def _add_thread(self, thread):
        # TabsManager.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.add(thread)
        # TabsManager.RUNNING_THREADS_MUTEX.unlock()

    def _remove_thread(self, thread):
        # TabsManager.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.remove(thread)
        # TabsManager.RUNNING_THREADS_MUTEX.unlock()

    @property
    def found_verses(self):
        return self.ui.foundVerses

    @property
    def search_word(self):
        return self.ui.searchWord.text()

    @property
    def matches_number(self):
        if s := self.ui.matchesNumber.text():
            return int(s)
        return 0

    @property
    def matches_number_surahs(self):
        if s := self.ui.matchesNumberSurahs.text():
            return int(s)
        return 0

    @property
    def matches_number_verses(self):
        if s := self.ui.matchesNumberVerses.text():
            return int(s)
        return 0

    def _init_surah_results_tab(self):
        self.lazy_surah_results_list = LazyListWidgetWrapper(self.ui.surahResultsListWidget, subtext_getter=SurahResultsSubtextGetter(), supported_methods=[CustomResultsSortEnum.BY_NUMBER, CustomResultsSortEnum.BY_NAME, CustomResultsSortEnum.BY_RESULT_ASCENDING, CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.lazy_surah_results_list.set_item_selection_changed_callback(self.surah_results_selection_changed)
        self.lazy_surah_results_list.set_item_double_clicked_callback(self.surah_results_item_double_clicked)

    def _init_words_results_tab(self):
        self.lazy_word_results_list = LazyListWidgetWrapper(self.ui.wordResultsListWidget,
                                                            subtext_getter=WordBoundsResultsSubtextGetter(),
                                                            supported_methods=[CustomResultsSortEnum.BY_NAME,
                                                                               CustomResultsSortEnum.BY_RESULT_ASCENDING,
                                                                               CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.lazy_word_results_list.set_item_selection_changed_callback(self.word_bounds_results_selection_changed)
        self.lazy_word_results_list.set_item_double_clicked_callback(self.word_bounds_results_item_double_clicked)

    def refresh_tabs_config(self):
        self.verse_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
        self.surah_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
        self.word_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())

    def clear_tabs_results(self):
        # self.found_verses.clear()  # it's done inside
        self.found_verses.save_values_and_refresh([], [])
        self.lazy_surah_results_list.clear()
        self.lazy_surah_results_list.save_values([])
        self.lazy_word_results_list.clear()
        self.lazy_word_results_list.save_values([])

    def _colorize_toggled(self, state):
        self.found_verses.reset_iter_and_refresh(SharedData.all_matches, state)

    def _toggle_diacritics(self, state):
        self._populate_word_results(self.search_word)

    def _toggle_all_surah_results(self, state):
        self._populate_surah_results()

    @Slot()
    def _clear_filter_button_clicked(self):
        self.filter_text_browser(range(len(SharedData.all_matches)))
        self.ui.clearFilterButton.setEnabled(False)

    @Slot()
    def _filter_button_clicked(self):
        if self._disambiguator.is_activated():
            self.show_disambiguation_dialog()
        else:
            self.show_gpt_activation_dialog()

    def show_gpt_activation_dialog(self):
        if load_translation(self._translator, resource_path(f"translations/openai_key_setup_dialog_{SharedData.app_language.value}.qm")):
            self.activate_gpt_dialog.set_language(SharedData.app_language)
        if self.activate_gpt_dialog.exec() == QDialog.DialogCode.Accepted:
            self._disambiguator.set_activated(True)
            self.show_disambiguation_dialog()

    def filter_text_browser(self, indices: list | range):
        # self.clear_results()
        matches_num, matched_verses_num, surah_count = self.found_verses.save_values_and_refresh(SharedData.all_matches, indices)
        # self.matches_number = str(matches_num)
        # self.matches_number_surahs = str(surah_count)
        # self.matches_number_verses = str(matched_verses_num)

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

    def on_word_found_complete(self, initial_word, number_of_matches):
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

    def show_disambiguation_dialog(self):
        if load_translation(self._translator, resource_path(f"translations/disambig_dlg_{SharedData.app_language.value}.qm")):
            self.disambiguation_dialog.set_language(SharedData.app_language)

        self.disambiguation_dialog.set_data(self.search_word)
        self.disambiguation_dialog.response_signal.connect(self._handle_disambiguation_dialog_response)
        if self.disambiguation_dialog.exec() == QDialog.DialogCode.Accepted:
            pass
        else:
            pass

    @Slot(str)
    def _handle_disambiguation_dialog_response(self, selected_meaning):
        # print("_handle_disambiguation_dialog_response")
        self.disambiguation_dialog.response_signal.disconnect(self._handle_disambiguation_dialog_response)
        if selected_meaning.strip():
            if load_translation(self._translator, resource_path(f"translations/waiting_dlg_{SharedData.app_language.value}.qm")):
                self.waiting_dialog.set_language(SharedData.app_language)
            self.waiting_dialog.open()
            self.ask_gpt_for_relevant_verses(self.search_word, SharedData.all_matches, selected_meaning)

    def ask_gpt_for_relevant_verses(self, word, verses, meaning):
        self.ask_gpt_thread.set_command_get_relevant_verses(word,
                                                verses,
                                                meaning)
        self.ask_gpt_thread.relevant_verses_result_ready.connect(self.on_ask_gpt_for_relevant_verses_completed)
        self.ask_gpt_thread.start()

    @Slot(list, QThread)
    def on_ask_gpt_for_relevant_verses_completed(self, results, caller_thread: AskGptThread):
        # print("FINAL RESULTS:")
        # print(results)
        # TODO: One time GPT returned the verse refs as they appear in the Holy Quran (x:y, x:y, ...)
        #       Need to put an eye on this
        caller_thread.relevant_verses_result_ready.disconnect(self.on_ask_gpt_for_relevant_verses_completed)
        self.waiting_dialog.reject()
        self.filter_text_browser(results)
        self.ui.clearFilterButton.setEnabled(True)

    def _populate_verses_results(self, number_of_matches):
        self.verse_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
        self.found_verses.save_values_and_refresh(SharedData.all_matches, range(len(SharedData.all_matches)))
        self.ui.filterButton.setEnabled((number_of_matches > 0) and len(self.search_word.split()) == 1)

    def _populate_surah_results(self):
        self.surah_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
        surah_finder_thread = SurahFinderThread(self._surah_index, self.ui.allResultsCheckbox.isChecked())
        surah_finder_thread.set_data(SharedData.all_matches, self.ui.allResultsCheckbox.isChecked())
        surah_finder_thread.result_ready.connect(self.on_find_surahs_completed)
        self._add_thread(surah_finder_thread)
        surah_finder_thread.start()

    def on_find_surahs_completed(self, counts, caller_thread):
        caller_thread.result_ready.disconnect(self.on_find_surahs_completed)
        QTimer.singleShot(TabsManager.REMOVE_THREAD_AFTER_MS, lambda: self._remove_thread(caller_thread))
        # TODO: reject older threads?

        # self.lazy_surah_results_list.clear()
        self.lazy_surah_results_list.save_values(counts)
        # self.lazy_surah_results_list.load_more_items()
        self.lazy_surah_results_list.sort()
        current_sorting = self.lazy_surah_results_list.get_current_sorting()
        self.ui.sortMethodLabel.setText(translate_text(current_sorting.to_string()))
        self.ui.sortPushButton.setEnabled(counts is not None and len(counts) > 0)

    def surah_results_selection_changed(self, selected_items: list[CustomListWidgetItem]):
        total = sum(int(SurahResultsSubtextGetter.ptrn.search(item.text()).group(3)) for item in selected_items)
        self.ui.surahResultsSum.setText(str(total))

    def _populate_word_results(self, initial_word):
        if len(initial_word.strip()) < 2:
            self.lazy_word_results_list.clear()
            self.lazy_word_results_list.save_values([])
            self.ui.minimum_letters_restriction_lbl.setStyleSheet(f"{self.minimum_letters_restriction_lbl_stylesheet} color: red;")
            return
        self.ui.minimum_letters_restriction_lbl.setStyleSheet(self.minimum_letters_restriction_lbl_stylesheet)

        self.word_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
        word_bounds_finder_thread = WordBoundsFinderThread(self.ui.diacriticsCheckbox.isChecked())
        word_bounds_finder_thread.set_data(SharedData.all_matches, self.ui.diacriticsCheckbox.isChecked())
        word_bounds_finder_thread.result_ready.connect(self.on_find_word_bounds_completed)
        self._add_thread(word_bounds_finder_thread)
        word_bounds_finder_thread.start()

    def on_find_word_bounds_completed(self, counts, caller_thread: WordBoundsFinderThread):
        caller_thread.result_ready.disconnect(self.on_find_word_bounds_completed)
        QTimer.singleShot(TabsManager.REMOVE_THREAD_AFTER_MS, lambda: self._remove_thread(caller_thread))
        # TODO: reject older threads?

        # self.lazy_word_results_list.clear()
        self.lazy_word_results_list.save_values(counts)
        # self.lazy_word_results_list.load_more_items()
        self.lazy_word_results_list.sort()
        current_sorting = self.lazy_word_results_list.get_current_sorting()
        self.ui.wordSortMethodLabel.setText(translate_text(current_sorting.to_string()))
        self.ui.wordsSortPushButton.setEnabled(counts is not None and len(counts) > 0)

    def word_bounds_results_selection_changed(self, selected_items: list[CustomListWidgetItem]):
        total = sum(int(WordBoundsResultsSubtextGetter.ptrn.search(item.text()).group(2)) for item in selected_items)
        self.ui.wordSum.setText(str(total))

    def word_bounds_results_item_double_clicked(self, item: CustomRow):
        if load_translation(self._translator, resource_path(f"translations/word_detailed_display_{SharedData.app_language.value}.qm")):
            self.detailed_word_display_dialog.set_language(SharedData.app_language)
        self.detailed_word_display_dialog.set_data(item)
        # self.detailed_word_display_dialog.open()
        self.detailed_word_display_dialog.exec()

    def surah_results_item_double_clicked(self, item: CustomRow):
        if load_translation(self._translator, resource_path(f"translations/word_detailed_display_{SharedData.app_language.value}.qm")):
            self.detailed_surah_display_dialog.set_language(SharedData.app_language)
        self.detailed_surah_display_dialog.set_data(item)
        # self.detailed_word_display_dialog.open()
        self.detailed_surah_display_dialog.exec()
