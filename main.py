import sys
import re
from enum import Enum
from yaml import safe_load
import uuid
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt, QTranslator, QThread, QMutex, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QFontDatabase
from my_data_loader import MyDataLoader
from gui.main_screen import Ui_MainWindow
from validators import ArabicOnlyValidator, MaxWordsValidator
from my_finder_thread import FinderThread
from emphasizer import emphasize_span, CssColors
from arabic_reformer import reform_text, is_alif, alif_maksura
from gui.my_disambiguation_dialog import MyDidsambiguationDialog
from gui.my_waiting_dialog import MyWaitingDialog
from gui.my_word_detailed_display_dialog import MyWordDetailedDisplayDialog
from gui.my_surah_detailed_display_dialog import MySurahDetailedDisplayDialog
from gui.my_mushaf_view_dialog_ import MyMushafViewDialog
from disambiguator import Disambiguator
from ask_gpt_thread import AskGptThread
from word_bounds_finder_thread import WordBoundsFinderThread
from surah_finder_thread import SurahFinderThread
from lazy_list_widget import LazyListWidgetWrapper, CustomListWidgetItem, CustomResultsSortEnum, CustomRow
from word_bounds_results_subtext_getter import WordBoundsResultsSubtextGetter
from surah_results_subtext_getter import SurahResultsSubtextGetter
from tab_wrapper import TabWrapper
from gui.spinning_loader import SpinningLoader


class AppLang(Enum):
    ARABIC = "ar"
    ENGLISH = "en"


class TabIndex(Enum):
    VERSES = 0
    SURAHS = 1
    WORDS = 2


class MainWindow(QMainWindow):
    ITEM_LOAD = 20
    MAX_WORDS_IF_NOT_MAINTAIN_ORDER = 2
    _exhausted = object()
    REMOVE_THREAD_AFTER_MS = 1000
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.running_threads = set()
        self.spinner = SpinningLoader()
        # TODO: Settings dialog...
        self._translator = QTranslator()
        self._font_ptrn = re.compile(r"(font:) .* \"[a-zA-Z \-]+\"([\s\S]*)")
        self._verse_ref_pattern = re.compile(r"\d{,3}:\d{,3}")
        self._surah_index = safe_load(open("surah_index.yml", encoding='utf-8', mode='r'))
        self._surah_results_list_uuid = uuid.uuid4().hex
        self._word_results_list_uuid = uuid.uuid4().hex
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self.verse_tab_wrapper = TabWrapper(self.ui.ayatTab, latest_radio_button=self.ui.searchOptionsButtonGroup.checkedId())
        self.surah_tab_wrapper = TabWrapper(self.ui.surahTab, latest_radio_button=self.ui.searchOptionsButtonGroup.checkedId())
        self.word_tab_wrapper = TabWrapper(self.ui.wordsTab, latest_radio_button=self.ui.searchOptionsButtonGroup.checkedId())
        self._max_words_validator = MaxWordsValidator(None if self.ui.maintainOrderCheckbox.isChecked() else MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER)
        self._current_lang = None
        self._apply_language(AppLang.ARABIC)
        self.cursor = None
        self.minimum_letters_restriction_lbl_stylesheet = self.ui.minimum_letters_restriction_lbl.styleSheet()
        # self.set_text_with_cursor()
        self._setup_events()
        self._setup_validators()
        # self._setup_fonts()
        # self._finder_thread = Finder()
        # self._finder_thread.result_ready.connect(self.on_word_found_complete)

        self._prev_scrolling_value = 0
        self._all_matches = None
        self._filtered_matches_iter = None
        self._filtered_matches_idx = None
        self._adding_items = False
        # [f"<span style=\"color: {c.value};\">" for c in color]

        self._disambiguator = Disambiguator(open("open_ai_key.txt", mode='r').read())
        self.disambiguation_dialog = MyDidsambiguationDialog(self._disambiguator)

        self.waiting_dialog = MyWaitingDialog()
        self.ask_gpt_thread = AskGptThread(self._disambiguator)

        self.detailed_word_display_dialog = MyWordDetailedDisplayDialog()
        self.detailed_surah_display_dialog = MySurahDetailedDisplayDialog()
        self.mushaf_view_display = MyMushafViewDialog()

        self.lazy_surah_results_list = LazyListWidgetWrapper(self.ui.surahResultsListWidget, subtext_getter=SurahResultsSubtextGetter(), supported_methods=[CustomResultsSortEnum.BY_NUMBER, CustomResultsSortEnum.BY_NAME, CustomResultsSortEnum.BY_RESULT_ASCENDING, CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.lazy_surah_results_list.set_item_selection_changed_callback(self.surah_results_selection_changed)
        self.lazy_surah_results_list.set_item_double_clicked_callback(self.surah_results_item_double_clicked)
        self.ui.surahResultsSum.setText(str(0))

        self.lazy_word_results_list = LazyListWidgetWrapper(self.ui.wordResultsListWidget, subtext_getter=WordBoundsResultsSubtextGetter(), supported_methods=[CustomResultsSortEnum.BY_NAME, CustomResultsSortEnum.BY_RESULT_ASCENDING, CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.lazy_word_results_list.set_item_selection_changed_callback(self.word_bounds_results_selection_changed)
        self.lazy_word_results_list.set_item_double_clicked_callback(self.word_bounds_results_item_double_clicked)
        self.ui.wordSum.setText(str(0))

    def _apply_language(self, lang):
        if lang != self._current_lang and self._translator.load(f"gui/translations/main_screen_{lang.value}.qm"):
            app.installTranslator(self._translator)
            self.ui.retranslateUi(self)
            self.set_font_for_language(lang)
            self._current_lang = lang

    def set_font_for_language(self, lang):
        styleSheet = self.styleSheet()
        font = "Calibri"
        size = 10
        weight = 400
        if lang == AppLang.ARABIC:
            size = 20
        elif lang == AppLang.ENGLISH:
            size = 12

        styleSheet = self._font_ptrn.sub(rf'\1 {weight} {size}pt "{font}"\2', styleSheet)
        self.setStyleSheet(styleSheet)

    def _setup_events(self):
        self.ui.searchOptionsButtonGroup.buttonToggled.connect(self._search_options_radio_buttons_changed)
        self.ui.tabWidget.currentChanged.connect(self._tab_changed)
        self.ui.maintainOrderCheckbox.stateChanged.connect(self._maintain_words_order_state_changed)
        self.ui.finalTaCheckbox.stateChanged.connect(self._final_ta_state_changed)
        self.ui.yaAlifMaksuraCheckbox.stateChanged.connect(self._ya_alif_maksura_state_changed)
        self.ui.alifAlifMaksuraCheckbox.stateChanged.connect(self._alif_variations_state_changed)
        self.ui.searchWord.textChanged.connect(self._search_word_text_changed)
        self.ui.foundVerses.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self.ui.foundVerses.verticalScrollBar().valueChanged.connect(self.after_scroll)
        self.ui.arabicLangButton.triggered.connect(lambda: self._apply_language(AppLang.ARABIC))
        self.ui.englishLangButton.triggered.connect(lambda: self._apply_language(AppLang.ENGLISH))
        self.ui.mushafNavigationButton.triggered.connect(self._view_mushaf)
        self.ui.colorizeCheckbox.stateChanged.connect(self._toggle_colorize)
        self.ui.diacriticsCheckbox.stateChanged.connect(self._toggle_diacritics)
        self.ui.allResultsCheckbox.stateChanged.connect(self._toggle_all_surah_results)
        self.ui.filterButton.clicked.connect(self._filter_button_clicked)
        self.ui.clearFilterButton.clicked.connect(self._clear_filter_button_clicked)
        self.ui.sortPushButton.clicked.connect(self._sort_surah_results_clicked)
        self.ui.wordsSortPushButton.clicked.connect(self._sort_word_results_clicked)

    def _setup_validators(self):
        self.ui.searchWord.setValidator(ArabicOnlyValidator())
        self.ui.searchWord.setValidator(self._max_words_validator)

    def _setup_fonts(self):
        # Load the custom font
        font_id = QFontDatabase.addApplicationFont("gui/NotoNaskhArabic-VariableFont_wght.ttf")

        # Retrieve the font family name (you can get the exact name of the font family using QFontDatabase.families())
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            print(f"Loaded font: {font_family}")  # Print the font family name to verify

            self.ui.foundVerses.setStyleSheet(f"font-family: '{font_family}'; font-size: 17;")
            # naskh_font = QFont(font_family, 14)
            # self.ui.foundVerses.setFont(naskh_font)

    def _view_mushaf(self):
        self.mushaf_view_display.exec()

    def before_scroll(self):
        scrollbar = self.ui.foundVerses.verticalScrollBar()
        self._prev_scrolling_value = scrollbar.value()

    def after_scroll(self):
        if self._adding_items or ((scrollbar := self.ui.foundVerses.verticalScrollBar()).value() < self._prev_scrolling_value):
            return "break"
        """Check if we need to load more widgets when scrolling."""
        current_val = scrollbar.value()
        # print(f"{scrollbar.value()}/{scrollbar.maximum()}")
        if scrollbar.value() > 0.85 * scrollbar.maximum():  # At the bottom
            self.load_more_items(MainWindow.ITEM_LOAD)
            scrollbar.setValue(min(scrollbar.maximum(), current_val))

    def load_more_items(self, items_to_load, prevent_scrolling=False):
        def _done():
            if prevent_scrolling:
                scrollbar.setValue(current_scroll_value)
            self._adding_items = False
            return

        self._adding_items = True
        scrollbar = self.ui.foundVerses.verticalScrollBar()
        current_scroll_value = scrollbar.value()
        for _ in range(items_to_load):
            if (item := next(self._filtered_matches_iter, MainWindow._exhausted)) is MainWindow._exhausted:
                return _done()
            surah_num, verse_num, verse, spans = item
            ref = f"{surah_num}:{verse_num}"
            if self.ui.colorizeCheckbox.isChecked():
                verse = self.reform_and_color(verse, spans)
            line = f"<p>{ref}: {verse}</p>"
            # line = f"{ref}: {verse}"
            self.ui.foundVerses.append(line)

        return _done()

    def reform_and_color(self, verse, spans):
        verse = reform_text(verse, text_may_contain_diacritics=True)
        # TODO: shouldn't we reform only span +-? See reformer.reform_span() -- didn't work so good
        # verse = self.reformer.reform_span(verse, spans, text_may_contain_diacritics=True)
        verse = emphasize_span(verse, spans, capitalize=False, underline=False, color=CssColors.CYAN, css=True)
        return verse

    # search word
    @property
    def search_word(self):
        return self.ui.searchWord.text()

    # @search_word.setter
    # def search_word(self, match_count):
    #     self.ui.searchWord.setText(match_count)

    # matches number
    @property
    def matches_number(self):
        if s := self.ui.matchesNumber.text():
            return int(s)
        return 0

    @matches_number.setter
    def matches_number(self, match_count):
        self.ui.matchesNumber.setText(match_count)

    @property
    def matches_number_surahs(self):
        if s := self.ui.matchesNumberSurahs.text():
            return int(s)
        return 0

    @matches_number_surahs.setter
    def matches_number_surahs(self, match_count):
        self.ui.matchesNumberSurahs.setText(match_count)

    @property
    def matches_number_verses(self):
        if s := self.ui.matchesNumberVerses.text():
            return int(s)
        return 0

    @matches_number_verses.setter
    def matches_number_verses(self, match_count):
        self.ui.matchesNumberVerses.setText(match_count)

    def clear_results(self, clear_verses=False):
        self.matches_number = ""
        self.matches_number_surahs = ""
        self.matches_number_verses = ""
        if clear_verses:
            self.ui.foundVerses.clear()

    # found verses
    @property
    def found_verses(self):
        return self.ui.foundVerses.toPlainText()

    @found_verses.setter
    def found_verses(self, verses):
        self.ui.foundVerses.setHtml(verses)
        # self.ui.foundVerses.addItems(verses)

    # full word
    @property
    def full_word_checkbox(self):
        return self.ui.fullWordRadioButton.isChecked()

    # start of word
    @property
    def beginning_of_word_checkbox(self):
        return self.ui.beginningOfWordRadioButton.isChecked()

    # end of word
    @property
    def ending_of_word_checkbox(self):
        return self.ui.endOfWordRadioButton.isChecked()

    # EVENTS
    def _toggle_colorize(self, state):
        # self._search_word_text_changed(self.search_word)
        # return
        self.ui.foundVerses.clear()
        self._filtered_matches_iter = iter([self._all_matches[idx] for idx in self._filtered_matches_idx])
        self.load_more_items(MainWindow.ITEM_LOAD, prevent_scrolling=True)

    def _toggle_diacritics(self, state):
        self._populate_word_results(self.search_word)

    def _toggle_all_surah_results(self, state):
        self._populate_surah_results()

    def _maintain_words_order_state_changed(self, state):
        self._max_words_validator.max_words = None if (qt_state := Qt.CheckState(state)) == Qt.CheckState.Checked else MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER
        self.ui.searchWord.setFocus()
        if qt_state == Qt.CheckState.Unchecked and len((words := self.search_word.split())) > 2:
            self.ui.searchWord.setText(' '.join(words[:MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER]))
        else:
            self._search_word_text_changed(self.search_word)

    def _final_ta_state_changed(self, state):
        if any(word.endswith(("ت", "ة")) for word in self.search_word.split()):
            self._search_word_text_changed(self.search_word)
        self.ui.searchWord.setFocus()

    def _ya_alif_maksura_state_changed(self, state):
        # if any(word.endswith(("ي", "يء", "ى", "ىء")) for word in self.search_word.split()):
        if any(ch in ['ي', 'ى'] for ch in self.search_word):
            self._search_word_text_changed(self.search_word)
        self.ui.searchWord.setFocus()

    def _alif_variations_state_changed(self, state):
        if any((is_alif(ch) or alif_maksura == ch) for ch in self.search_word):
            self._search_word_text_changed(self.search_word)
        self.ui.searchWord.setFocus()

    @Slot()
    def _filter_button_clicked(self):
        self.disambiguation_dialog.set_data(self.search_word)
        self.disambiguation_dialog.response_signal.connect(self._handle_disambiguation_dialog_response)
        if self.disambiguation_dialog.exec() == QDialog.DialogCode.Accepted:
            pass
        else:
            pass

    def _clear_filter_button_clicked(self):
        self._filtered_matches_idx = range(len(self._all_matches))
        self.filter_text_browser()
        self.ui.clearFilterButton.setEnabled(False)

    def _sort_surah_results_clicked(self):
        def _surah_sorting_done():
            self.ui.sortPushButton.setEnabled(True)
            current_sorting = self.lazy_surah_results_list.get_current_sorting()
            self.ui.sortMethodLabel.setText(current_sorting.to_string())

        self.ui.sortPushButton.setEnabled(False)
        self.lazy_surah_results_list.set_sorting_done_callback(_surah_sorting_done)
        self.lazy_surah_results_list.switch_order()
        self.lazy_surah_results_list.sort()

    def _sort_word_results_clicked(self):
        def _word_sorting_done():
            self.ui.wordsSortPushButton.setEnabled(True)
            current_sorting = self.lazy_word_results_list.get_current_sorting()
            self.ui.wordSortMethodLabel.setText(current_sorting.to_string())

        self.ui.wordsSortPushButton.setEnabled(False)
        self.lazy_word_results_list.set_sorting_done_callback(_word_sorting_done)
        self.lazy_word_results_list.switch_order()
        self.lazy_word_results_list.sort()
        current_sorting = self.lazy_word_results_list.get_current_sorting()
        self.ui.wordSortMethodLabel.setText(current_sorting.to_string())

    @Slot(str)
    def _handle_disambiguation_dialog_response(self, selected_meaning):
        # print("_handle_disambiguation_dialog_response")
        self.disambiguation_dialog.response_signal.disconnect(self._handle_disambiguation_dialog_response)
        if selected_meaning.strip():
            self.waiting_dialog.open()
            self.ask_gpt_for_relevant_verses(self.search_word, self._all_matches, selected_meaning)

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
        self._filtered_matches_idx = results
        self.ui.clearFilterButton.setEnabled(True)
        self.filter_text_browser()

    def filter_text_browser(self):
        # TODO: Maybe a numpy array would serve index selection better
        self._filtered_matches_iter = iter([self._all_matches[idx] for idx in self._filtered_matches_idx])
        self.ui.foundVerses.clear()
        self.clear_results()
        # self.ui.filterButton.setEnabled(False)
        self.refresh_matches()
        self.load_more_items(MainWindow.ITEM_LOAD, prevent_scrolling=True)

    def _add_thread(self, thread):
        # MainWindow.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.add(thread)
        # MainWindow.RUNNING_THREADS_MUTEX.unlock()

    def _remove_thread(self, thread):
        # MainWindow.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.remove(thread)
        # MainWindow.RUNNING_THREADS_MUTEX.unlock()

    def refresh_matches(self):
        # TODO: make background thread if takes too much time
        self.matches_number_verses = str(len(self._filtered_matches_idx))
        surahs = set()
        matches_num = 0
        for idx in self._filtered_matches_idx:
            surah_num, _, verse, spans = self._all_matches[idx]
            surahs.add(surah_num)
            matches_num += len(spans)

        self.matches_number = str(matches_num)
        self.matches_number_surahs = str(len(surahs))

    def _search_word_text_changed(self, new_text):
        self._all_matches = []
        self._filtered_matches_iter = None
        if (not (stripped := new_text.strip())) or (self.ui.rootRadioButton.isChecked() and (len(stripped) < 2 or len(stripped.split()) != 1)):
            self.clear_results()
            self.verse_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
            self.surah_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
            self.word_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
            match self.ui.tabWidget.currentIndex():
                case TabIndex.VERSES.value:
                    self.ui.filterButton.setEnabled(False)
                    self.ui.sortPushButton.setEnabled(False)
                    self.ui.wordsSortPushButton.setEnabled(False)
                    self.ui.foundVerses.clear()
                case TabIndex.SURAHS.value:
                    self.lazy_surah_results_list.clear()
                    self.lazy_surah_results_list.save_values([])
                case TabIndex.WORDS.value:
                    self.lazy_word_results_list.clear()
                    self.lazy_word_results_list.save_values([])
            return

        if self.ui.rootRadioButton.isChecked():
            self.waiting()

        # TODO: Need to verify threads finish in the right order!
        #       Test while removing characters from a long word
        #       ==> Tried and they do finish in the right order, but idk if we can count on it
        finder_thread = FinderThread()
        finder_thread.set_data(new_text,
                               self.ui.alifAlifMaksuraCheckbox.isChecked() and self.ui.alifAlifMaksuraCheckbox.isEnabled(),
                               self.ui.yaAlifMaksuraCheckbox.isChecked() and self.ui.yaAlifMaksuraCheckbox.isEnabled(),
                               self.ui.finalTaCheckbox.isChecked() and self.ui.finalTaCheckbox.isEnabled(),
                               self.ui.maintainOrderCheckbox.isChecked() and self.ui.maintainOrderCheckbox.isEnabled(),
                               self.full_word_checkbox,
                               self.beginning_of_word_checkbox,
                               self.ending_of_word_checkbox,
                               self.ui.rootRadioButton.isChecked())
        finder_thread.result_ready.connect(self.on_word_found_complete)
        self._add_thread(finder_thread)
        finder_thread.start()

    def on_word_found_complete(self, initial_word, words_num, result, caller_thread):
        # print(initial_word)
        caller_thread.result_ready.disconnect(self.on_word_found_complete)
        QTimer.singleShot(MainWindow.REMOVE_THREAD_AFTER_MS, lambda: self._remove_thread(caller_thread))
        self._all_matches, number_of_matches, number_of_surahs, number_of_verses = result
        self.matches_number = str(number_of_matches)
        self.matches_number_surahs = str(number_of_surahs)
        self.matches_number_verses = str(number_of_verses)

        match self.ui.tabWidget.currentIndex():
            case TabIndex.VERSES.value:
                self._populate_verses_results(number_of_matches)
            case TabIndex.SURAHS.value:
                self._populate_surah_results()
            case TabIndex.WORDS.value:
                self._populate_word_results(initial_word)

        self.finished_waiting()

    def waiting(self):
        self.ui.searchWord.setEnabled(False)
        self.spinner.start()

    def finished_waiting(self):
        self.spinner.stop()
        self.ui.searchWord.setEnabled(True)
        self.ui.searchWord.setFocus()

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

    def _populate_verses_results(self, number_of_matches):
        self.verse_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
        self._filtered_matches_idx = range(len(self._all_matches))
        self._filtered_matches_iter = iter(self._all_matches)
        self.ui.filterButton.setEnabled((number_of_matches > 0) and len(self.search_word.split()) == 1)

        self.ui.foundVerses.clear()
        self.load_more_items(MainWindow.ITEM_LOAD, prevent_scrolling=True)

    def _populate_surah_results(self):
        self.surah_tab_wrapper.update_config(self.search_word, self.ui.searchOptionsButtonGroup.checkedId())
        surah_finder_thread = SurahFinderThread(self._surah_index, self.ui.allResultsCheckbox.isChecked())
        surah_finder_thread.set_data(self._all_matches, self.ui.allResultsCheckbox.isChecked())
        surah_finder_thread.result_ready.connect(self.on_find_surahs_completed)
        self._add_thread(surah_finder_thread)
        surah_finder_thread.start()

    def on_find_surahs_completed(self, counts, caller_thread):
        caller_thread.result_ready.disconnect(self.on_find_surahs_completed)
        QTimer.singleShot(MainWindow.REMOVE_THREAD_AFTER_MS, lambda: self._remove_thread(caller_thread))

        # self.lazy_surah_results_list.clear()
        self.lazy_surah_results_list.save_values(counts)
        # self.lazy_surah_results_list.load_more_items()
        self.lazy_surah_results_list.sort()
        current_sorting = self.lazy_surah_results_list.get_current_sorting()
        self.ui.sortMethodLabel.setText(current_sorting.to_string())
        self.ui.sortPushButton.setEnabled(self._all_matches is not None and len(self._all_matches) > 0)

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
        word_bounds_finder_thread.set_data(self._all_matches, self.ui.diacriticsCheckbox.isChecked())
        word_bounds_finder_thread.result_ready.connect(self.on_find_word_bounds_completed)
        self._add_thread(word_bounds_finder_thread)
        word_bounds_finder_thread.start()

    def on_find_word_bounds_completed(self, counts, caller_thread: WordBoundsFinderThread):
        caller_thread.result_ready.disconnect(self.on_find_word_bounds_completed)
        QTimer.singleShot(MainWindow.REMOVE_THREAD_AFTER_MS, lambda: self._remove_thread(caller_thread))

        # self.lazy_word_results_list.clear()
        self.lazy_word_results_list.save_values(counts)
        # self.lazy_word_results_list.load_more_items()
        self.lazy_word_results_list.sort()
        current_sorting = self.lazy_word_results_list.get_current_sorting()
        self.ui.wordSortMethodLabel.setText(current_sorting.to_string())
        self.ui.wordsSortPushButton.setEnabled(self._all_matches is not None and len(self._all_matches) > 0)

    def word_bounds_results_selection_changed(self, selected_items: list[CustomListWidgetItem]):
        total = sum(int(WordBoundsResultsSubtextGetter.ptrn.search(item.text()).group(2)) for item in selected_items)
        self.ui.wordSum.setText(str(total))

    def word_bounds_results_item_double_clicked(self, item: CustomRow):
        self.detailed_word_display_dialog.set_data(item)
        # self.detailed_word_display_dialog.open()
        self.detailed_word_display_dialog.exec()

    def surah_results_item_double_clicked(self, item: CustomRow):
        self.detailed_surah_display_dialog.set_data(item)
        # self.detailed_word_display_dialog.open()
        self.detailed_surah_display_dialog.exec()

    def _search_options_radio_buttons_changed(self, button, is_checked: bool):
        if button == self.ui.rootRadioButton:
            self.ui.alifAlifMaksuraCheckbox.setEnabled(not is_checked)
            self.ui.yaAlifMaksuraCheckbox.setEnabled(not is_checked)
            self.ui.finalTaCheckbox.setEnabled(not is_checked)
            self.ui.maintainOrderCheckbox.setEnabled(not is_checked)

        if not is_checked:
            return

        self._search_word_text_changed(self.search_word)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MyDataLoader()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
