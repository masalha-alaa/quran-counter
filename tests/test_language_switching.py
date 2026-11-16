"""Exercise the actual MainWindow language actions without starting data workers."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QEvent, QSignalBlocker, QTranslator, Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtTest import QSignalSpy, QTest
from PySide6.QtWidgets import QApplication, QMainWindow


class LanguageSwitchingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        import main
        cls.main = main
        cls.temp = tempfile.TemporaryDirectory()
        cls.catalogs = Path(cls.temp.name) / "translations"
        # Use the same compiler called by convert_to_exe.bat, including the
        # dynamic catalogs that the old UI-only preview tests did not load.
        subprocess.run([sys.executable, "tools/compile_translations.py",
                        "--output-dir", str(cls.catalogs)], check=True, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.shared = self.main.SharedData
        self.original = {name: getattr(self.shared, name) for name in (
            "ui", "app_language", "translator", "ar_to_en_dynamic_translator", "en_to_ar_dynamic_translator",
        )}
        self.shared.app_language = self.main.AppLang.ARABIC
        for name in ("translator", "ar_to_en_dynamic_translator", "en_to_ar_dynamic_translator"):
            setattr(self.shared, name, QTranslator())

        # Skip the constructor that creates data-backed dialogs and checks for
        # updates. Keep the production action wiring and _apply_language method.
        self.window = self.main.MainWindow.__new__(self.main.MainWindow)
        QMainWindow.__init__(self.window)
        self.window.spinner = Mock()
        self.window.running_threads = set()
        self.window._last_thread_id = -1
        self.window._active_search_id = None
        self.ui = self.main.Ui_MainWindow()
        self.shared.ui = self.ui
        self.ui.setupUi(self.window)
        self.tables = (self.ui.surahResultsTableWidget, self.ui.wordResultsTableWidget,
                       self.ui.topicResultsTableWidget)
        for table in self.tables:
            table.setColumnCount(len(table.get_translated_headers()))
        self.window.tabs_manager = SimpleNamespace(retranslate_ui=self._retranslate_tables)
        self.window._setup_events()
        self.resources = patch.object(self.main, "resource_path", side_effect=lambda path: str(Path(self.temp.name) / path))
        self.resources.start()
        self.window.show()
        self.app.sendPostedEvents(None, QEvent.Type.DeferredDelete)
        self.app.processEvents()

    def tearDown(self):
        self.resources.stop()
        for name in ("translator", "ar_to_en_dynamic_translator", "en_to_ar_dynamic_translator"):
            self.app.removeTranslator(getattr(self.shared, name))
        for name, value in self.original.items():
            setattr(self.shared, name, value)
        self.window.close()
        self.window.deleteLater()
        self.app.sendPostedEvents(None, QEvent.Type.DeferredDelete)

    def _retranslate_tables(self):
        for table in self.tables:
            table.retranslate_ui()

    def test_real_language_actions_switch_back_and_forth(self):
        with QSignalBlocker(self.ui.searchWord):
            self.ui.searchWord.setText("الرحمة")
        self.ui.foundVerses.setPlainText("نتيجة تجريبية")
        for action, language, title, column, direction in (
            (self.ui.englishLangButton, self.main.AppLang.ENGLISH, "Quran Counter", "Surah", Qt.LeftToRight),
            (self.ui.arabicLangButton, self.main.AppLang.ARABIC, "عدّاد القرآن الكريم", "اسم السورة", Qt.RightToLeft),
            (self.ui.englishLangButton, self.main.AppLang.ENGLISH, "Quran Counter", "Surah", Qt.LeftToRight),
        ):
            action.trigger()
            self.app.processEvents()
            self.assertEqual(self.shared.app_language, language)
            self.assertEqual(self.ui.title.text(), title)
            self.assertEqual(self.ui.surahResultsTableWidget.horizontalHeaderItem(0).text(), column)
            self.assertEqual(self.window.layoutDirection(), direction)
            self.assertEqual(self.ui.searchWord.text(), "الرحمة")
            self.assertEqual(self.ui.foundVerses.toPlainText(), "نتيجة تجريبية")
            self.assertGreater(self.ui.searchWord.cursorRect().left(), self.ui.searchWord.width() * 0.65)

    def test_missing_catalog_reports_error_without_partial_language_change(self):
        self.ui.englishLangButton.trigger()
        installed = [getattr(self.shared, name) for name in (
            "translator", "ar_to_en_dynamic_translator", "en_to_ar_dynamic_translator",
        )]
        catalog = self.catalogs / "dynamic_translations_ar_src_ar.qm"
        backup = catalog.with_suffix(".backup")
        catalog.rename(backup)
        try:
            with patch.object(self.main.QMessageBox, "warning") as warning:
                self.ui.arabicLangButton.trigger()
                warning.assert_called_once()
            self.assertEqual(self.shared.app_language, self.main.AppLang.ENGLISH)
            self.assertEqual(self.ui.title.text(), "Quran Counter")
            self.assertEqual(self.ui.surahResultsTableWidget.horizontalHeaderItem(0).text(), "Surah")
            self.assertEqual(installed, [getattr(self.shared, name) for name in (
                "translator", "ar_to_en_dynamic_translator", "en_to_ar_dynamic_translator",
            )])
        finally:
            backup.rename(catalog)
        self.ui.arabicLangButton.trigger()
        self.assertEqual(self.shared.app_language, self.main.AppLang.ARABIC)

    def test_modes_still_enable_matching_controls_in_their_new_location(self):
        self.window._composite_validator = self.main.CompositeValidator(None)
        # Exercise the production mode handler, excluding the data search it
        # schedules after changing the allowed query length.
        with patch.object(self.window, "_finetune_search_text"):
            self.ui.rootRadioButton.click()
            for checkbox in self.ui.refinements:
                self.assertFalse(checkbox.isEnabled())
                self.assertTrue(checkbox.isVisible())
            self.ui.noRestrictionsRadioButton.click()
            for checkbox in self.ui.refinements:
                self.assertTrue(checkbox.isEnabled())
                self.assertTrue(checkbox.isVisible())

    def test_mouse_mode_switches_preserve_query_focus_and_geometry(self):
        self.window._composite_validator = self.main.CompositeValidator(None)
        self.window._regex_validator = self.main.ArabicWithRegexValidator()
        self.window.tabs_manager = Mock()
        with patch.object(self.window, "_finetune_search_text"), \
                patch("worker_threads.my_topic_finder_thread.TopicFinderThread") as worker:
            worker.return_value.is_model_initialized.return_value = True
            for action in (self.ui.arabicLangButton, self.ui.englishLangButton):
                action.trigger()
                for size in ((1220, 860), (940, 640)):
                    self.window.resize(*size)
                    self.ui.searchWord.setFocus()
                    self.app.processEvents()
                    geometry = self.ui.searchWord.geometry()
                    changes = QSignalSpy(self.app.focusChanged)
                    for button in self.ui.mode_buttons:
                        self.ui.sidebar.ensureWidgetVisible(button)
                        QTest.mouseClick(button, Qt.LeftButton)
                        self.app.processEvents()
                        with self.subTest(mode=button.text(), size=size):
                            self.assertTrue(button.isChecked())
                            self.assertTrue(self.ui.searchWord.hasFocus())
                            self.assertEqual(changes.count(), 0)
                            self.assertEqual(self.ui.searchWord.geometry(), geometry)

    def test_keyboard_mode_selection_keeps_keyboard_focus(self):
        self.window._composite_validator = self.main.CompositeValidator(None)
        with patch.object(self.window, "_finetune_search_text"):
            self.ui.fullWordRadioButton.setFocus()
            QTest.keyClick(self.ui.fullWordRadioButton, Qt.Key_Space)
            self.assertTrue(self.ui.fullWordRadioButton.isChecked())
            self.assertTrue(self.ui.fullWordRadioButton.hasFocus())

    def test_waiting_locks_text_without_focus_flashes_or_slider_clicks(self):
        self.window.spinner = Mock()
        self.ui.searchWord.setFocus()
        self.app.processEvents()
        focus = QSignalSpy(self.app.focusChanged)
        changed = QSignalSpy(self.ui.searchWord.textChanged)
        slider = QSignalSpy(self.ui.similarityThresholdSlider.sliderPressed)
        self.window.waiting("Working")
        QTest.keyClicks(self.ui.searchWord, "123")
        self.assertTrue(self.ui.searchWord.isReadOnly())
        self.assertTrue(self.ui.searchWord.isEnabled())
        self.assertEqual(changed.count(), 0)
        self.window.finished_waiting()
        self.assertFalse(self.ui.searchWord.isReadOnly())
        self.assertTrue(self.ui.searchWord.hasFocus())
        self.assertEqual(focus.count(), 0)
        self.assertEqual(slider.count(), 0)

    def test_typing_and_result_callbacks_keep_the_caret_and_filter_steady(self):
        self.window.tabs_manager = Mock()
        self.window._composite_validator = self.main.CompositeValidator(None)
        self.window._regex_validator = self.main.ArabicWithRegexValidator()
        self.window._set_validator(self.window._composite_validator)
        field = self.ui.searchWord
        result = self.main.FinderResultObject([], 1, 1, 1)
        with patch.object(self.main, "FinderThread"), \
                patch.object(self.main, "TopicFinderThread"), \
                patch("worker_threads.my_topic_finder_thread.TopicFinderThread"), \
                patch.object(self.window, "_remove_thread"):
            for action in (self.ui.arabicLangButton, self.ui.englishLangButton):
                action.trigger()
                for mode in self.ui.mode_buttons:
                    field.clear()
                    mode.click()
                    self.window.finished_waiting()
                    field.setFocus()
                    QTest.keyClick(field, Qt.Key_Direction_L)
                    for char in "بسم ":
                        self.app.processEvents()
                        was_enabled = self.ui.filterButton.isEnabled()
                        appearance = self.ui.filterButton.grab().toImage()
                        before = field.cursorRect().x()
                        if char == " ":
                            QTest.keyClick(field, Qt.Key_Space)
                        else:
                            self.app.sendEvent(field, QKeyEvent(QEvent.KeyPress, Qt.Key_unknown, Qt.NoModifier, char))
                        self.app.processEvents()
                        search_id = self.window._active_search_id
                        if search_id is not None:
                            with self.subTest(language=action.text(), mode=mode.text(), char=char):
                                self.assertFalse(self.ui.filterButton.isEnabled())
                                if was_enabled:
                                    self.assertEqual(self.ui.filterButton.grab().toImage(), appearance)
                            if mode is self.ui.topicsRadioButton:
                                self.window.on_topics_found_complete(field.text(), result, search_id, Mock())
                            else:
                                self.window.on_txt_found_complete(field.text(), 1, result, search_id, Mock())
                        self.app.processEvents()
                        if char == " ":
                            self.assertLess(field.cursorRect().x(), before)
                        self.assertEqual(field.cursorPosition(), len(field.text()))
                        self.assertTrue(field.hasFocus())
                    self.assertEqual(field.text(), "بسم ")

    def test_outdated_search_cannot_enable_filter_for_the_current_query(self):
        self.window.tabs_manager = Mock()
        result = self.main.FinderResultObject([], 1, 1, 1)
        with patch.object(self.main, "FinderThread"), patch.object(self.window, "_remove_thread"):
            self.ui.searchWord.setText("رحمة")
            previous = self.window._active_search_id
            self.ui.searchWord.insert("ا")
            current = self.window._active_search_id
            self.window.on_txt_found_complete("رحمة", 1, result, previous, Mock())
            self.assertTrue(self.ui.search_filter.pending)
            self.assertFalse(self.ui.filterButton.isEnabled())
            self.window.tabs_manager.on_txt_found_complete.assert_not_called()
            self.window.on_txt_found_complete(self.ui.searchWord.text(), 1, result, current, Mock())
            self.assertTrue(self.ui.filterButton.isEnabled())
            self.ui.searchWord.clear()
            self.window.on_txt_found_complete("رحمةا", 1, result, current, Mock())
            self.assertFalse(self.ui.filterButton.isEnabled())
            self.assertFalse(self.ui.search_filter.pending)
            self.window.spinner.stop.assert_called()

    def test_filter_becomes_unavailable_for_no_matches_or_multiple_words(self):
        self.window.tabs_manager = Mock()
        with patch.object(self.main, "FinderThread"), patch.object(self.window, "_remove_thread"):
            for query, count, available in (("رحمة", 2, True), ("رحمةا", 0, False),
                                            ("رحمة الله", 2, False)):
                self.ui.searchWord.setText(query)
                result = self.main.FinderResultObject([], count, 1, 1)
                self.window.on_txt_found_complete(query, len(query.split()), result, self.window._active_search_id, Mock())
                self.assertEqual(self.ui.filterButton.isEnabled(), available)
                self.assertFalse(self.ui.filterButton.property("pendingSearch"))


if __name__ == "__main__":
    unittest.main()
