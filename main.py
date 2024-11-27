import sys
import re
from datetime import datetime
import uuid
from PySide6.QtGui import QValidator
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from my_utils.my_data_loader import MyDataLoader
from  my_utils.shared_data import SharedData
from gui.main_window.main_screen import Ui_MainWindow
from text_validators.composite_validator import CompositeValidator
from text_validators.arabic_with_regex_validator import ArabicWithRegexValidator
from worker_threads.my_finder_thread import FinderThread
from arabic_reformer import is_alif, alif_maksura
from gui.mushaf_view_dialog.my_mushaf_view_dialog_ import MyMushafViewDialog
from my_widgets.spinning_loader import SpinningLoader
from my_utils.utils import AppLang, resource_path, load_translation, scale, ScaleRounding, translate_text
from tabs_management.tabs_manager import TabsManager


class MainWindow(QMainWindow):
    ITEM_LOAD = 20
    MAX_WORDS_IF_NOT_MAINTAIN_ORDER = 2
    MAX_WORDS_IF_ROOT = 1
    MAX_WORDS_IF_SIMILAR_WORD = 1
    _exhausted = object()
    REMOVE_THREAD_AFTER_MS = 500
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self):
        super(MainWindow, self).__init__()
        self._setup_fonts()
        SharedData.ui = Ui_MainWindow()
        self.running_threads = set()
        self._last_thread_id = -1
        self.spinner = SpinningLoader()
        # TODO: Settings dialog...
        self._font_ptrn = re.compile(r"(font:) .* \"[a-zA-Z \-]+\"([\s\S]*)")
        self._verse_ref_pattern = re.compile(r"\d{,3}:\d{,3}")
        self._surah_results_list_uuid = uuid.uuid4().hex
        self._word_results_list_uuid = uuid.uuid4().hex
        SharedData.ui.setupUi(self)

        SharedData.ui.similarityThresholdSlider.setEnabled(SharedData.ui.similarWordRadioButton.isChecked())
        SharedData.ui.similarityThresholdLabel.setText(str(SharedData.ui.similarityThresholdSlider.value()))
        max_words = self._get_max_words_for_search_option()
        self._composite_validator = CompositeValidator(max_words)
        self._regex_validator = ArabicWithRegexValidator()
        self._apply_language(AppLang.DEFAULT_LANGUAGE)
        SharedData.ui.regexRadioButton.setToolTip(f"regex: {ArabicWithRegexValidator.SUPPORTED_REGEX_CHARS}")
        self.tabs_manager = TabsManager()
        self.cursor = None
        self._setup_events()
        self._set_validator(self._composite_validator if not SharedData.ui.regexRadioButton.isChecked() else self._regex_validator)

        self._prev_scrolling_value = 0
        SharedData.all_matches = []

        self.mushaf_view_display = MyMushafViewDialog(SharedData.app_language)

        SharedData.ui.surahResultsSum.setText(str(0))
        SharedData.ui.wordSum.setText(str(0))

    def _apply_language(self, lang):
        if lang != SharedData.app_language and load_translation(SharedData.translator, resource_path(f"translations/main_screen_{lang.value}.qm")) and load_translation(SharedData.dynamic_translator, resource_path(f"translations/dynamic_translations_{lang.value}.qm")):
            app.installTranslator(SharedData.translator)
            app.installTranslator(SharedData.dynamic_translator)
            SharedData.ui.retranslateUi(self)
            self.tabs_manager.retranslate_ui()
            self.set_font_for_language(lang)
            SharedData.app_language = lang

    def set_font_for_language(self, lang):
        styleSheet = self.styleSheet()
        font = "Calibri"
        size = 10
        weight = 400
        if lang == AppLang.ARABIC:
            size = 18
        elif lang == AppLang.ENGLISH:
            size = 16

        styleSheet = self._font_ptrn.sub(rf'\1 {weight} {size}pt "{font}"\2', styleSheet)
        self.setStyleSheet(styleSheet)

    def _setup_events(self):
        SharedData.ui.searchOptionsButtonGroup.buttonToggled.connect(self._search_options_radio_buttons_changed)
        # SharedData.ui.tabWidget.currentChanged.connect(self._tab_changed)
        SharedData.ui.wordPermutationsCheckbox.stateChanged.connect(self._maintain_words_order_state_changed)
        SharedData.ui.finalTaCheckbox.stateChanged.connect(self._final_ta_state_changed)
        SharedData.ui.yaAlifMaksuraCheckbox.stateChanged.connect(self._ya_alif_maksura_state_changed)
        SharedData.ui.alifAlifMaksuraCheckbox.stateChanged.connect(self._alif_variations_state_changed)
        SharedData.ui.optionalAlTarifCheckbox.stateChanged.connect(self._optional_al_tarif_state_changed)
        SharedData.ui.searchWord.textChanged.connect(self._search_word_text_changed)
        SharedData.ui.arabicLangButton.triggered.connect(lambda: self._apply_language(AppLang.ARABIC))
        SharedData.ui.englishLangButton.triggered.connect(lambda: self._apply_language(AppLang.ENGLISH))
        SharedData.ui.mushafNavigationButton.triggered.connect(self._view_mushaf)
        SharedData.ui.similarityThresholdSlider.valueChanged.connect(self._similarity_threshold_changed)

    def _set_validator(self, validator):
        SharedData.ui.searchWord.setValidator(validator)

    def _setup_fonts(self):
        # Load the custom font
        QFontDatabase.addApplicationFont(resource_path("fonts/NotoNaskhArabic-VariableFont_wght.ttf"))

    def _get_max_words_for_search_option(self):
        match SharedData.ui.searchOptionsButtonGroup.checkedButton():
            case SharedData.ui.rootRadioButton:
                max_words = MainWindow.MAX_WORDS_IF_ROOT
            case SharedData.ui.similarWordRadioButton:
                max_words = MainWindow.MAX_WORDS_IF_SIMILAR_WORD
            case _:
                if SharedData.ui.wordPermutationsCheckbox.isChecked():
                    max_words = MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER
                else:
                    max_words = None
        return max_words

    def _view_mushaf(self):
        if load_translation(SharedData.translator, resource_path(f"translations/mushaf_view_{SharedData.app_language.value}.qm")):
            self.mushaf_view_display.set_language(SharedData.app_language)
        self.mushaf_view_display.exec()

    def clear_results(self):
        SharedData.matches_number = ""
        SharedData.matches_number_surahs = ""
        SharedData.matches_number_verses = ""

    # EVENTS

    def _optional_al_tarif_state_changed(self, state):
        self._search_word_text_changed(SharedData.search_word)
        SharedData.ui.searchWord.setFocus()

    def _maintain_words_order_state_changed(self, state):
        new_max_words = self._composite_validator.get_max_words() if (qt_state := Qt.CheckState(state)) == Qt.CheckState.Unchecked else MainWindow.MAX_WORDS_IF_NOT_MAINTAIN_ORDER
        self._composite_validator.set_max_words(new_max_words)
        self._finetune_search_text()
        SharedData.ui.searchWord.setFocus()

    def _finetune_search_text(self, max_words:str|int|None='auto'):
        if max_words == 'auto':
            max_words = self._get_max_words_for_search_option()
        if max_words is not None and len((words := SharedData.search_word.split())) > max_words:
            SharedData.ui.searchWord.setText(' '.join(words[:max_words]))
        else:
            self._search_word_text_changed(SharedData.search_word)

    def _final_ta_state_changed(self, state):
        # ['\u062a', '\u0629'] == ["ت", "ة"]
        if any(word.endswith(('\u062a', '\u0629')) for word in SharedData.search_word.split()):
            self._search_word_text_changed(SharedData.search_word)
        SharedData.ui.searchWord.setFocus()

    def _ya_alif_maksura_state_changed(self, state):
        # if any(word.endswith(("ي", "يء", "ى", "ىء")) for word in SharedData.search_word.split()):
        #['\u064a', '\u0649'] == ["ي", "ى"]
        if any(ch in ['\u064a', '\u0649'] for ch in SharedData.search_word):
            self._search_word_text_changed(SharedData.search_word)
        SharedData.ui.searchWord.setFocus()

    def _alif_variations_state_changed(self, state):
        if any((is_alif(ch) or alif_maksura == ch) for ch in SharedData.search_word):
            self._search_word_text_changed(SharedData.search_word)
        SharedData.ui.searchWord.setFocus()

    def _add_thread(self, thread):
        # MainWindow.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.add(thread)
        # MainWindow.RUNNING_THREADS_MUTEX.unlock()

    def _remove_thread(self, thread):
        # MainWindow.RUNNING_THREADS_MUTEX.lock()
        QTimer.singleShot(MainWindow.REMOVE_THREAD_AFTER_MS, lambda: self.running_threads.remove(thread))
        # MainWindow.RUNNING_THREADS_MUTEX.unlock()

    def is_valid_regex(self, pattern):
        try:
            re.compile(pattern)
            # not in SUPPORTED REGEX means do not allow one regex character
            return not (pattern.startswith(("|", "(|",)) or pattern.endswith(("|", "|)")) or pattern in ArabicWithRegexValidator.SUPPORTED_REGEX_CHARS or "||" in pattern or "??" in pattern)
        except re.error:
            return False

    def _search_word_text_changed(self, new_text):
        SharedData.ui.filterButton.setEnabled(False)
        SharedData.all_matches = []
        if (not (stripped := new_text.strip())) or ((SharedData.ui.rootRadioButton.isChecked() or SharedData.ui.similarWordRadioButton.isChecked()) and (len(stripped) < 2 or len(stripped.split()) != 1)):
            self.clear_results()
            self.tabs_manager.refresh_tabs_config()
            SharedData.ui.filterButton.setEnabled(False)
            self.tabs_manager.clear_tabs_results()
            if SharedData.ui.regexRadioButton.isChecked():
                SharedData.ui.searchWord.setStyleSheet("")
            return

        if SharedData.ui.regexRadioButton.isChecked():
            if self.is_valid_regex(new_text):
                SharedData.ui.searchWord.setStyleSheet("")
            else:
                SharedData.ui.searchWord.setStyleSheet("background-color: rgba(255, 0, 0, 50);")
                return

        if SharedData.ui.rootRadioButton.isChecked() or SharedData.ui.similarWordRadioButton.isChecked():
            self.waiting()

        thread_id = datetime.now().timestamp()
        finder_thread = FinderThread(thread_id)
        finder_thread.set_data(new_text,
                               SharedData.ui.alifAlifMaksuraCheckbox.isChecked() and SharedData.ui.alifAlifMaksuraCheckbox.isEnabled(),
                               SharedData.ui.yaAlifMaksuraCheckbox.isChecked() and SharedData.ui.yaAlifMaksuraCheckbox.isEnabled(),
                               SharedData.ui.finalTaCheckbox.isChecked() and SharedData.ui.finalTaCheckbox.isEnabled(),
                               not (SharedData.ui.wordPermutationsCheckbox.isChecked() and SharedData.ui.wordPermutationsCheckbox.isEnabled()),
                               SharedData.ui.optionalAlTarifCheckbox.isChecked() and SharedData.ui.optionalAlTarifCheckbox.isEnabled(),
                               SharedData.full_word_checkbox,
                               SharedData.beginning_of_word_checkbox,
                               SharedData.ending_of_word_checkbox,
                               SharedData.ui.rootRadioButton.isChecked(),
                               SharedData.ui.regexRadioButton.isChecked(),
                               SharedData.ui.similarWordRadioButton.isChecked(),
                               scale(int(SharedData.ui.similarityThresholdLabel.text()),
                                     SharedData.ui.similarityThresholdSlider.minimum(),
                                     SharedData.ui.similarityThresholdSlider.maximum(),
                                     FinderThread.MIN_CLOSE_MATCH_RAW_THRESHOLD,
                                     FinderThread.MAX_CLOSE_MATCH_RAW_THRESHOLD,
                                     rounding=ScaleRounding.FLOOR) if SharedData.ui.similarWordRadioButton.isChecked() else None)
        finder_thread.result_ready.connect(self.on_txt_found_complete)
        self._add_thread(finder_thread)
        finder_thread.start()

    def on_txt_found_complete(self, initial_word, words_num, result, thread_id, caller_thread: FinderThread):
        caller_thread.result_ready.disconnect(self.on_txt_found_complete)
        self._remove_thread(caller_thread)
        # reject older threads
        if thread_id < self._last_thread_id:
            return
        self._last_thread_id = thread_id

        SharedData.all_matches, number_of_matches, number_of_surahs, number_of_verses = result
        SharedData.matches_number = str(number_of_matches)
        SharedData.matches_number_surahs = str(number_of_surahs)
        SharedData.matches_number_verses = str(number_of_verses)

        self.tabs_manager.on_txt_found_complete(initial_word, number_of_matches)
        self.finished_waiting()

    def waiting(self):
        SharedData.ui.searchWord.setEnabled(False)
        SharedData.ui.similarityThresholdSlider.setEnabled(False)
        self.spinner.start()

    def finished_waiting(self):
        self.spinner.stop()
        SharedData.ui.searchWord.setEnabled(True)
        SharedData.ui.similarityThresholdSlider.setEnabled(SharedData.ui.similarWordRadioButton.isChecked())
        if SharedData.ui.similarityThresholdSlider.isEnabled():
            # a trick to restore the blue color on the slider handle (setFocus() didn't work)
            self._simulate_click_on_slider_handle(SharedData.ui.similarityThresholdSlider)
        SharedData.ui.searchWord.setFocus()

    def _simulate_click_on_slider_handle(self, slider):
        # Get the slider handle position based on its current value
        handle_pos = slider.rect().center()  # Default to center if no other method is available

        # For horizontal sliders
        if slider.orientation() == Qt.Orientation.Horizontal:
            # Map the value to the x-coordinate of the handle within the slider's range
            handle_x = int((slider.value() - slider.minimum()) / (slider.maximum() - slider.minimum()) * slider.width())
            handle_pos = slider.mapToGlobal(slider.rect().topLeft()) + slider.rect().topLeft()
            handle_pos.setX(handle_x)

        # For vertical sliders
        elif slider.orientation() == Qt.Orientation.Vertical:
            # Map the value to the y-coordinate of the handle within the slider's range
            handle_y = int(
                (slider.value() - slider.minimum()) / (slider.maximum() - slider.minimum()) * slider.height())
            handle_pos = slider.mapToGlobal(slider.rect().topLeft()) + slider.rect().topLeft()
            handle_pos.setY(handle_y)

        # Simulate the click at the handle position
        QTest.mouseClick(slider, Qt.MouseButton.LeftButton, pos=handle_pos)

    def _search_options_radio_buttons_changed(self, button, is_checked: bool):
        if button == SharedData.ui.rootRadioButton:
            SharedData.ui.alifAlifMaksuraCheckbox.setEnabled(not is_checked)
            SharedData.ui.yaAlifMaksuraCheckbox.setEnabled(not is_checked)
            SharedData.ui.finalTaCheckbox.setEnabled(not is_checked)
            SharedData.ui.optionalAlTarifCheckbox.setEnabled(not is_checked)
            SharedData.ui.wordPermutationsCheckbox.setEnabled(not is_checked)
        elif button == SharedData.ui.similarWordRadioButton:
            SharedData.ui.similarityThresholdSlider.setEnabled(is_checked)
            SharedData.ui.alifAlifMaksuraCheckbox.setEnabled(not is_checked)
            SharedData.ui.yaAlifMaksuraCheckbox.setEnabled(not is_checked)
            SharedData.ui.finalTaCheckbox.setEnabled(not is_checked)
            SharedData.ui.optionalAlTarifCheckbox.setEnabled(not is_checked)
            SharedData.ui.wordPermutationsCheckbox.setEnabled(not is_checked)
        elif button == SharedData.ui.regexRadioButton:
            self._set_validator(self._regex_validator if is_checked else self._composite_validator)
            if not is_checked:
                SharedData.ui.searchWord.setStyleSheet("")
                if self._composite_validator.validate(SharedData.search_word, 0)[0] != QValidator.State.Acceptable:
                    SharedData.ui.searchWord.clear()

            SharedData.ui.alifAlifMaksuraCheckbox.setEnabled(not is_checked)
            SharedData.ui.yaAlifMaksuraCheckbox.setEnabled(not is_checked)
            SharedData.ui.finalTaCheckbox.setEnabled(not is_checked)
            SharedData.ui.wordPermutationsCheckbox.setEnabled(not is_checked)
            SharedData.ui.optionalAlTarifCheckbox.setEnabled(not is_checked)

        if not is_checked:
            return

        new_max_words = self._get_max_words_for_search_option()
        self._composite_validator.set_max_words(new_max_words)
        self._finetune_search_text(new_max_words)
        SharedData.ui.searchWord.setFocus()

    def _similarity_threshold_changed(self, value):
        SharedData.ui.similarityThresholdLabel.setText(str(value))
        self._search_word_text_changed(SharedData.search_word)


# import faulthandler
if __name__ == "__main__":
    # faulthandler.enable()

    print("Starting...")

    app = QApplication(sys.argv)

    MyDataLoader()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
