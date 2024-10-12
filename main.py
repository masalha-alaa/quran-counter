import sys
import re
from enum import Enum
from yaml import safe_load
import uuid
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt, QTranslator, QThread
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QFontDatabase
from gui.main_screen import Ui_MainWindow
from validators import ArabicOnlyValidator
from finder import Finder
from emphasizer import emphasize_span, CssColors
from arabic_reformer import reform_text, reform_regex, is_alif, alif_maksura
from gui.my_disambiguation_dialog import MyDidsambiguationDialog
from gui.my_waiting_dialog import MyWaitingDialog
from disambiguator import Disambiguator
from ask_gpt_thread import AskGptThread
from word_bounds_finder_thread import WordBoundsFinderThread
from surah_finder_thread import SurahFinderThread
from lazy_list_widget import LazyListWidgetWrapper, CustomListWidgetItem, CustomResultsSortEnum
from word_bounds_results_subtext_getter import WordBoundsResultsSubtextGetter
from surah_results_subtext_getter import SurahResultsSubtextGetter


class AppLang(Enum):
    ARABIC = "ar"
    ENGLISH = "en"


class MainWindow(QMainWindow):
    ITEM_LOAD = 20
    _exhausted = object()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        # TODO: Settings dialog...
        self._translator = QTranslator()
        self._font_ptrn = re.compile(r"(font:) .* \"[a-zA-Z \-]+\"([\s\S]*)")
        self._verse_ref_pattern = re.compile(r"\d{,3}:\d{,3}")
        self._surah_index = safe_load(open("surah_index.yml", encoding='utf-8', mode='r'))
        self._surah_results_list_uuid = uuid.uuid4().hex
        self._word_results_list_uuid = uuid.uuid4().hex
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self._current_lang = None
        self._apply_language(AppLang.ARABIC)
        self.cursor = None
        # self.set_text_with_cursor()
        self._setup_events()
        self._setup_validators()
        # self._setup_fonts()
        self._finder = Finder()
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

        self.lazy_surah_results_list = LazyListWidgetWrapper(self.ui.surahResultsListWidget, subtext_getter=SurahResultsSubtextGetter(), supported_methods=[CustomResultsSortEnum.BY_NUMBER, CustomResultsSortEnum.BY_NAME, CustomResultsSortEnum.BY_RESULT_ASCENDING, CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.surah_finder_thread = SurahFinderThread(self._surah_index, self.ui.allResultsCheckbox.isChecked())
        self.surah_finder_thread.result_ready.connect(self.on_find_surahs_completed)
        self.lazy_surah_results_list.set_item_selection_changed_signal(self.surah_results_selection_changed)
        self.ui.surahResultsSum.setText(str(0))

        self.lazy_word_results_list = LazyListWidgetWrapper(self.ui.wordResultsListWidget, subtext_getter=WordBoundsResultsSubtextGetter(), supported_methods=[CustomResultsSortEnum.BY_NAME, CustomResultsSortEnum.BY_RESULT_ASCENDING, CustomResultsSortEnum.BY_RESULT_DESCENDING])
        self.word_bounds_finder_thread = WordBoundsFinderThread(self.ui.diacriticsCheckbox.isChecked())
        self.word_bounds_finder_thread.result_ready.connect(self.on_find_word_bounds_completed)
        self.lazy_word_results_list.set_item_selection_changed_signal(self.word_bounds_results_selection_changed)
        self.ui.wordSum.setText(str(0))

    def _apply_language(self, lang):
        if lang != self._current_lang and self._translator.load(f"gui/translations/{lang.value}.qm"):
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
        self.ui.fullWordcheckbox.stateChanged.connect(self._full_word_checkbox_state_changed)
        self.ui.beginningOfWordCheckbox.stateChanged.connect(self._beginning_of_word_checkbox_state_changed)
        self.ui.endOfWordCheckbox.stateChanged.connect(self._end_of_word_checkbox_state_changed)
        self.ui.finalTaCheckbox.stateChanged.connect(self._final_ta_state_changed)
        self.ui.yaAlifMaksuraCheckbox.stateChanged.connect(self._ya_alif_maksura_state_changed)
        self.ui.alifAlifMaksuraCheckbox.stateChanged.connect(self._alif_variations_state_changed)
        self.ui.searchWord.textChanged.connect(self._search_word_text_changed)
        self.ui.foundVerses.verticalScrollBar().valueChanged.connect(self.after_scroll)
        self.ui.foundVerses.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self.ui.arabicLangButton.triggered.connect(lambda: self._apply_language(AppLang.ARABIC))
        self.ui.englishLangButton.triggered.connect(lambda: self._apply_language(AppLang.ENGLISH))
        self.ui.englishLangButton.triggered.connect(lambda: self._apply_language(AppLang.ENGLISH))
        self.ui.colorizeCheckbox.stateChanged.connect(self._toggle_colorize)
        self.ui.diacriticsCheckbox.stateChanged.connect(self._toggle_diacritics)
        self.ui.allResultsCheckbox.stateChanged.connect(self._toggle_all_surah_results)
        self.ui.filterButton.clicked.connect(self._filter_button_clicked)
        self.ui.clearFilterButton.clicked.connect(self._clear_filter_button_clicked)
        self.ui.sortPushButton.clicked.connect(self._sort_surah_results_clicked)
        self.ui.wordsSortPushButton.clicked.connect(self._sort_word_results_clicked)

    def _setup_validators(self):
        self.ui.searchWord.setValidator(ArabicOnlyValidator())

    def _setup_fonts(self):
        # Load the custom font
        font_id = QFontDatabase.addApplicationFont("gui/NotoNaskhArabic-VariableFont_wght.ttf")

        # Retrieve the font family name (you can get the exact name of the font family using QFontDatabase.families())
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            print(f"Loaded font: {font_family}")  # Print the font family name to verify

            self.ui.foundVerses.setStyleSheet(f"font-family: '{font_family}'; font-size: 14pt;")
            # naskh_font = QFont(font_family, 14)
            # self.ui.foundVerses.setFont(naskh_font)

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
        return self.ui.matchesNumber.toPlainText()

    @matches_number.setter
    def matches_number(self, match_count):
        self.ui.matchesNumber.setText(match_count)

    @property
    def matches_number_surahs(self):
        return self.ui.matchesNumberSurahs.toPlainText()

    @matches_number_surahs.setter
    def matches_number_surahs(self, match_count):
        self.ui.matchesNumberSurahs.setText(match_count)

    @property
    def matches_number_verses(self):
        return self.ui.matchesNumberVerses.toPlainText()

    @matches_number_verses.setter
    def matches_number_verses(self, match_count):
        self.ui.matchesNumberVerses.setText(match_count)

    def clear_results(self, clear_verses=False):
        self.matches_number = ""
        self.matches_number_surahs = ""
        self.matches_number_verses = ""
        if clear_verses:
            self.found_verses = ""

    # found verses
    @property
    def found_verses(self):
        return self.ui.foundVerses.toPlainText()

    @found_verses.setter
    def found_verses(self, verses):
        # self.ui.foundVerses.setHtml(verses)
        self.ui.foundVerses.addItems(verses)

    # full word
    @property
    def full_word_checkbox(self):
        return self.ui.fullWordcheckbox.isChecked()

    # start of word
    @property
    def beginning_of_word_checkbox(self):
        return self.ui.beginningOfWordCheckbox.isChecked()

    # end of word
    @property
    def ending_of_word_checkbox(self):
        return self.ui.endOfWordCheckbox.isChecked()

    # EVENTS
    def _toggle_colorize(self, state):
        # self._search_word_text_changed(self.search_word)
        # return
        self.ui.foundVerses.clear()
        self._filtered_matches_iter = iter([self._all_matches[idx] for idx in self._filtered_matches_idx])
        self.load_more_items(MainWindow.ITEM_LOAD, prevent_scrolling=True)

    def _toggle_diacritics(self, state):
        # self._search_word_text_changed(self.search_word)
        # return
        self.word_bounds_finder_thread.set_diacritics_sensitive(state)
        self._populate_word_results()

    def _toggle_all_surah_results(self, state):
        self.surah_finder_thread.set_include_zeros(state)
        self._populate_surah_results()

    def _final_ta_state_changed(self, state):
        if any(word.endswith(("ت", "ة")) for word in self.search_word.split()):
            self._search_word_text_changed(self.search_word)

    def _ya_alif_maksura_state_changed(self, state):
        # if any(word.endswith(("ي", "يء", "ى", "ىء")) for word in self.search_word.split()):
        if any(ch in ['ي', 'ى'] for ch in self.search_word):
            self._search_word_text_changed(self.search_word)

    def _alif_variations_state_changed(self, state):
        if any((is_alif(ch) or alif_maksura == ch) for ch in self.search_word):
            self._search_word_text_changed(self.search_word)

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
        self.lazy_surah_results_list.switch_order()
        self.lazy_surah_results_list.sort()
        current_sorting = self.lazy_surah_results_list.get_current_sorting()
        self.ui.sortMethodLabel.setText(current_sorting.to_string())

    def _sort_word_results_clicked(self):
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
        self._all_matches = None
        self._filtered_matches_iter = None
        self.ui.foundVerses.clear()
        if not new_text.strip():
            self.clear_results()
            self.ui.filterButton.setEnabled(False)
            self.ui.sortPushButton.setEnabled(False)
            self.ui.wordsSortPushButton.setEnabled(False)
            self.ui.surahResultsListWidget.clear()
            self.lazy_word_results_list.clear()
            return

        # if any(word.endswith(("ت", "ة")) for word in new_text.split()):
        #     self.ui.finalTaCheckbox.setEnabled(True)
        # else:
        #     self.ui.finalTaCheckbox.setEnabled(False)

        # ignore diacritics
        # TODO: make checkbox?
        new_text = reform_regex(new_text,
                                alif_alif_maksura_variations=self.ui.alifAlifMaksuraCheckbox.isChecked(),
                                ya_variations=self.ui.yaAlifMaksuraCheckbox.isChecked(),
                                ta_variations=self.ui.finalTaCheckbox.isChecked())

        # NOT WORKING WITH TASHKEEL
        # if self.full_word_checkbox:
        #     new_text = rf"\b{new_text}\b"
        # elif self.beginning_of_word_checkbox:
        #     new_text = rf"\b{new_text}"
        # elif self.ending_of_word_checkbox:
        #     new_text = rf"{new_text}\b"

        search_words = len(new_text.split())
        new_text = f"({new_text})"  # capturing group
        beginning_of_word = r"[ ^]"
        end_of_word = r"[ ,$]"
        if self.full_word_checkbox:
            new_text = beginning_of_word + rf"{new_text}" + end_of_word
        else:
            if self.beginning_of_word_checkbox:
                new_text = beginning_of_word + rf"{new_text}"
            if self.ending_of_word_checkbox:
                new_text = rf"{new_text}" + end_of_word

        self._all_matches, number_of_matches, number_of_surahs, number_of_verses = self._finder.find_word(new_text)
        self._filtered_matches_idx = range(len(self._all_matches))
        self._filtered_matches_iter = iter(self._all_matches)
        self.ui.filterButton.setEnabled((number_of_matches > 0) and search_words == 1)
        # for _, row in results.iterrows():
        #     surah_cnt += 1
        #     for v, spans in row['spans'].items():
        #         verse_cnt += 1
        #         wrd_sum += len(spans)
        #         self._all_matches.append((int(row.name) + 1, v + 1, row['verses_clean_split'][v], spans))
        self.matches_number = str(number_of_matches)
        self.matches_number_surahs = str(number_of_surahs)
        self.matches_number_verses = str(number_of_verses)
        self.load_more_items(MainWindow.ITEM_LOAD, prevent_scrolling=True)
        self._populate_surah_results()
        self._populate_word_results()

    def _populate_surah_results(self):
        self.surah_finder_thread.set_matches(self._all_matches)
        self.surah_finder_thread.set_include_zeros(self.ui.allResultsCheckbox.isChecked())
        self.surah_finder_thread.start()

    def on_find_surahs_completed(self, counts, caller_thread):
        self.lazy_surah_results_list.clear()
        self.lazy_surah_results_list.save_values(counts)
        self.lazy_surah_results_list.load_more_items()
        self.lazy_surah_results_list.sort()
        current_sorting = self.lazy_surah_results_list.get_current_sorting()
        self.ui.sortMethodLabel.setText(current_sorting.to_string())
        self.ui.sortPushButton.setEnabled(len(self._all_matches) > 0)

    def surah_results_selection_changed(self, selected_items: list[CustomListWidgetItem]):
        total = sum(int(SurahResultsSubtextGetter.ptrn.search(item.text()).group(3)) for item in selected_items)
        self.ui.surahResultsSum.setText(str(total))

    def _populate_word_results(self):
        self.word_bounds_finder_thread.set_matches(self._all_matches)
        self.word_bounds_finder_thread.set_diacritics_sensitive(self.ui.diacriticsCheckbox.isChecked())
        self.word_bounds_finder_thread.start()

    def on_find_word_bounds_completed(self, counts, caller_thread):
        self.lazy_word_results_list.clear()
        self.lazy_word_results_list.save_values(counts)
        self.lazy_word_results_list.load_more_items()
        self.lazy_word_results_list.sort()
        current_sorting = self.lazy_word_results_list.get_current_sorting()
        self.ui.wordSortMethodLabel.setText(current_sorting.to_string())
        self.ui.wordsSortPushButton.setEnabled(len(self._all_matches) > 0)

    def word_bounds_results_selection_changed(self, selected_items: list[CustomListWidgetItem]):
        total = sum(int(WordBoundsResultsSubtextGetter.ptrn.search(item.text()).group(2)) for item in selected_items)
        self.ui.wordSum.setText(str(total))

    def _full_word_checkbox_state_changed(self, state):
        def _set_enabled_others(enabled):
            # self.ui.beginningOfWordCheckbox.setEnabled(enabled)
            # self.ui.endOfWordCheckbox.setEnabled(enabled)
            # self.ui.aiPushButton.setEnabled(enabled)
            pass

        qt_state = Qt.CheckState(state)
        if qt_state == Qt.CheckState.Checked:
            # uncheck
            self.ui.beginningOfWordCheckbox.setChecked(False)
            self.ui.endOfWordCheckbox.setChecked(False)

        # enable / disable
        _set_enabled_others(qt_state != Qt.CheckState.Checked)

        # search
        # TODO: caching
        self._search_word_text_changed(self.search_word)

    def _beginning_of_word_checkbox_state_changed(self, state):
        def _set_enabled_others(enabled):
            # self.ui.fullWordcheckbox.setEnabled(enabled)
            # self.ui.aiPushButton.setEnabled(enabled)
            pass

        qt_state = Qt.CheckState(state)
        if qt_state == Qt.CheckState.Checked:
            # uncheck
            self.ui.fullWordcheckbox.setChecked(False)

        # enable / disable
        _set_enabled_others(qt_state != Qt.CheckState.Checked)

        # search
        # TODO: caching
        self._search_word_text_changed(self.search_word)

    def _end_of_word_checkbox_state_changed(self, state):
        def _set_enabled_others(enabled):
            # self.ui.fullWordcheckbox.setEnabled(enabled)
            # self.ui.aiPushButton.setEnabled(enabled)
            pass

        qt_state = Qt.CheckState(state)
        if qt_state == Qt.CheckState.Checked:
            # uncheck
            self.ui.fullWordcheckbox.setChecked(False)

        # enable / disable
        _set_enabled_others(qt_state != Qt.CheckState.Checked)

        # search
        # TODO: caching
        self._search_word_text_changed(self.search_word)

    def _ai_button_clicked(self, state):
        def _set_enabled_others(enabled):
            self.ui.fullWordcheckbox.setEnabled(enabled)
            self.ui.beginningOfWordCheckbox.setEnabled(enabled)
            self.ui.endOfWordCheckbox.setEnabled(enabled)

        qt_state = Qt.CheckState(state)
        if qt_state == Qt.CheckState.Checked:
            # uncheck
            self.ui.fullWordcheckbox.setChecked(False)
            self.ui.beginningOfWordCheckbox.setChecked(False)
            self.ui.endOfWordCheckbox.setChecked(False)

        # enable / disable
        # _set_enabled_others(qt_state != Qt.CheckState.Checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
