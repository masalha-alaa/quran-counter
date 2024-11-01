import sys
import re
from datetime import datetime
import uuid
from PySide6.QtCore import Qt, QTranslator, QThread, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QFontDatabase
from my_utils.my_data_loader import MyDataLoader
from  my_utils.shared_data import SharedData
from gui.main_window.main_screen import Ui_MainWindow
from text_validators.composite_validator import CompositeValidator
from worker_threads.my_finder_thread import FinderThread
from arabic_reformer import is_alif, alif_maksura
from gui.mushaf_view_dialog.my_mushaf_view_dialog_ import MyMushafViewDialog
from my_widgets.spinning_loader import SpinningLoader
from my_utils.utils import AppLang, resource_path, load_translation
from tabs_manager.tabs_manager import TabsManager


class MainWindow(QMainWindow):
    ITEM_LOAD = 20
    MAX_WORDS_IF_NOT_MAINTAIN_ORDER = 2
    _exhausted = object()
    REMOVE_THREAD_AFTER_MS = 500
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self):
        super(MainWindow, self).__init__()
        self._setup_fonts()
        self.ui = Ui_MainWindow()
        self.running_threads = set()
        self._thread_id = -1
        self._last_thread_id = -1
        self.spinner = SpinningLoader()
        # TODO: Settings dialog...
        self._translator = QTranslator()
        self._dynamic_translator = QTranslator()
        self._font_ptrn = re.compile(r"(font:) .* \"[a-zA-Z \-]+\"([\s\S]*)")
        self._verse_ref_pattern = re.compile(r"\d{,3}:\d{,3}")
        self._surah_results_list_uuid = uuid.uuid4().hex
        self._word_results_list_uuid = uuid.uuid4().hex
        self.ui.setupUi(self)

        self.ui.optionalAlTarifCheckbox.setVisible(False)  # TODO: Enable and implement functionality
        self.ui.line_8.setVisible(False)  # TODO: Remove

        self._composite_validator = CompositeValidator(None if not self.ui.wordPermutationsCheckbox.isChecked() else MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER)
        self.tabs_manager = TabsManager(self.ui)
        self._apply_language(AppLang.DEFAULT_LANGUAGE)
        self.cursor = None
        self._setup_events()
        self._setup_validators()

        self._prev_scrolling_value = 0
        SharedData.all_matches = []

        self.mushaf_view_display = MyMushafViewDialog(SharedData.app_language)

        self.ui.surahResultsSum.setText(str(0))
        self.ui.wordSum.setText(str(0))

    def _apply_language(self, lang):
        if lang != SharedData.app_language and load_translation(self._translator, resource_path(f"translations/main_screen_{lang.value}.qm")) and load_translation(self._dynamic_translator, resource_path(f"translations/dynamic_translations_{lang.value}.qm")):
            app.installTranslator(self._translator)
            app.installTranslator(self._dynamic_translator)
            self.ui.retranslateUi(self)
            self.set_font_for_language(lang)
            SharedData.app_language = lang

    def set_font_for_language(self, lang):
        styleSheet = self.styleSheet()
        font = "Calibri"
        size = 10
        weight = 400
        if lang == AppLang.ARABIC:
            size = 20
        elif lang == AppLang.ENGLISH:
            size = 14

        styleSheet = self._font_ptrn.sub(rf'\1 {weight} {size}pt "{font}"\2', styleSheet)
        self.setStyleSheet(styleSheet)

    def _setup_events(self):
        self.ui.searchOptionsButtonGroup.buttonToggled.connect(self._search_options_radio_buttons_changed)
        # self.ui.tabWidget.currentChanged.connect(self._tab_changed)
        self.ui.wordPermutationsCheckbox.stateChanged.connect(self._maintain_words_order_state_changed)
        self.ui.finalTaCheckbox.stateChanged.connect(self._final_ta_state_changed)
        self.ui.yaAlifMaksuraCheckbox.stateChanged.connect(self._ya_alif_maksura_state_changed)
        self.ui.alifAlifMaksuraCheckbox.stateChanged.connect(self._alif_variations_state_changed)
        self.ui.optionalAlTarifCheckbox.stateChanged.connect(self._optional_al_tarif_state_changed)
        self.ui.searchWord.textChanged.connect(self._search_word_text_changed)
        self.ui.arabicLangButton.triggered.connect(lambda: self._apply_language(AppLang.ARABIC))
        self.ui.englishLangButton.triggered.connect(lambda: self._apply_language(AppLang.ENGLISH))
        self.ui.mushafNavigationButton.triggered.connect(self._view_mushaf)

    def _setup_validators(self):
        self.ui.searchWord.setValidator(self._composite_validator)
        # self.ui.searchWord.setValidator(ArabicOnlyValidator())
        # self.ui.searchWord.setValidator(self._max_words_validator)

    def _setup_fonts(self):
        # Load the custom font
        QFontDatabase.addApplicationFont(resource_path("fonts/NotoNaskhArabic-VariableFont_wght.ttf"))

    def _view_mushaf(self):
        if load_translation(self._translator, resource_path(f"translations/mushaf_view_{SharedData.app_language.value}.qm")):
            self.mushaf_view_display.set_language(SharedData.app_language)
        self.mushaf_view_display.exec()

    # search word
    @property
    def search_word(self):
        return self.ui.searchWord.text()

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

    def clear_results(self):
        self.matches_number = ""
        self.matches_number_surahs = ""
        self.matches_number_verses = ""

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

    def _optional_al_tarif_state_changed(self, state):
        # TODO: implement
        # self._search_word_text_changed(self.search_word)
        self.ui.searchWord.setFocus()

    def _maintain_words_order_state_changed(self, state):
        self._composite_validator.set_max_words(None if (qt_state := Qt.CheckState(state)) == Qt.CheckState.Unchecked else MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER)
        self.ui.searchWord.setFocus()
        if qt_state == Qt.CheckState.Checked and len((words := self.search_word.split())) > MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER:
            self.ui.searchWord.setText(' '.join(words[:MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER]))
        else:
            self._search_word_text_changed(self.search_word)

    def _final_ta_state_changed(self, state):
        # ['\u062a', '\u0629'] == ["ت", "ة"]
        if any(word.endswith(('\u062a', '\u0629')) for word in self.search_word.split()):
            self._search_word_text_changed(self.search_word)
        self.ui.searchWord.setFocus()

    def _ya_alif_maksura_state_changed(self, state):
        # if any(word.endswith(("ي", "يء", "ى", "ىء")) for word in self.search_word.split()):
        #['\u064a', '\u0649'] == ["ي", "ى"]
        if any(ch in ['\u064a', '\u0649'] for ch in self.search_word):
            self._search_word_text_changed(self.search_word)
        self.ui.searchWord.setFocus()

    def _alif_variations_state_changed(self, state):
        if any((is_alif(ch) or alif_maksura == ch) for ch in self.search_word):
            self._search_word_text_changed(self.search_word)
        self.ui.searchWord.setFocus()

    def _add_thread(self, thread):
        # MainWindow.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.add(thread)
        # MainWindow.RUNNING_THREADS_MUTEX.unlock()

    def _remove_thread(self, thread):
        # MainWindow.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.remove(thread)
        # MainWindow.RUNNING_THREADS_MUTEX.unlock()

    def _search_word_text_changed(self, new_text):
        self.ui.filterButton.setEnabled(False)
        SharedData.all_matches = []
        if (not (stripped := new_text.strip())) or (self.ui.rootRadioButton.isChecked() and (len(stripped) < 2 or len(stripped.split()) != 1)):
            self.clear_results()
            self.tabs_manager.refresh_tabs_config()
            self.ui.filterButton.setEnabled(False)
            self.ui.sortPushButton.setEnabled(False)
            self.ui.wordsSortPushButton.setEnabled(False)
            self.tabs_manager.clear_tabs_results()
            return

        if self.ui.rootRadioButton.isChecked():
            self.waiting()

        self._thread_id = datetime.now().timestamp()
        finder_thread = FinderThread(self._thread_id)
        finder_thread.set_data(new_text,
                               self.ui.alifAlifMaksuraCheckbox.isChecked() and self.ui.alifAlifMaksuraCheckbox.isEnabled(),
                               self.ui.yaAlifMaksuraCheckbox.isChecked() and self.ui.yaAlifMaksuraCheckbox.isEnabled(),
                               self.ui.finalTaCheckbox.isChecked() and self.ui.finalTaCheckbox.isEnabled(),
                               not (self.ui.wordPermutationsCheckbox.isChecked() and self.ui.wordPermutationsCheckbox.isEnabled()),
                               self.ui.optionalAlTarifCheckbox.isChecked() and self.ui.optionalAlTarifCheckbox.isEnabled(),
                               self.full_word_checkbox,
                               self.beginning_of_word_checkbox,
                               self.ending_of_word_checkbox,
                               self.ui.rootRadioButton.isChecked())
        finder_thread.result_ready.connect(self.on_word_found_complete)
        self._add_thread(finder_thread)
        finder_thread.start()

    def on_word_found_complete(self, initial_word, words_num, result, thread_id, caller_thread: FinderThread):
        caller_thread.result_ready.disconnect(self.on_word_found_complete)
        QTimer.singleShot(MainWindow.REMOVE_THREAD_AFTER_MS, lambda: self._remove_thread(caller_thread))
        if thread_id < self._last_thread_id:
            return
        self._last_thread_id = thread_id

        SharedData.all_matches, number_of_matches, number_of_surahs, number_of_verses = result
        self.matches_number = str(number_of_matches)
        self.matches_number_surahs = str(number_of_surahs)
        self.matches_number_verses = str(number_of_verses)

        self.tabs_manager.on_word_found_complete(initial_word, number_of_matches)
        self.finished_waiting()

    def waiting(self):
        self.ui.searchWord.setEnabled(False)
        self.spinner.start()

    def finished_waiting(self):
        self.spinner.stop()
        self.ui.searchWord.setEnabled(True)
        self.ui.searchWord.setFocus()

    def _search_options_radio_buttons_changed(self, button, is_checked: bool):
        if button == self.ui.rootRadioButton:
            # self.ui.alifAlifMaksuraCheckbox.setEnabled(not is_checked)
            # self.ui.yaAlifMaksuraCheckbox.setEnabled(not is_checked)
            self.ui.finalTaCheckbox.setEnabled(not is_checked)
            self.ui.optionalAlTarifCheckbox.setEnabled(not is_checked)
            self.ui.wordPermutationsCheckbox.setEnabled(not is_checked)

        if not is_checked:
            return

        self._search_word_text_changed(self.search_word)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MyDataLoader()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
