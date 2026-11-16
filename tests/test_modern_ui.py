"""Exercise the real Qt form without the separately distributed Quran dataset."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QEvent, QTranslator, Qt
from PySide6.QtGui import QFontDatabase, QKeyEvent
from PySide6.QtTest import QSignalSpy, QTest
from PySide6.QtWidgets import QApplication, QMainWindow

from gui.main_window.modern_main_window import Ui_MainWindow
from my_utils.my_enums import AppLang
from text_validators.arabic_with_regex_validator import ArabicWithRegexValidator


class ModernUiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        QFontDatabase.addApplicationFont("fonts/NotoNaskhArabic-VariableFont_wght.ttf")
        cls.temp = tempfile.TemporaryDirectory()
        cls.translation = Path(cls.temp.name) / "main_screen_en.qm"
        executable = "pyside6-lrelease.exe" if sys.platform == "win32" else "pyside6-lrelease"
        subprocess.run([str(Path(sys.executable).with_name(executable)),
                        "translations/main_screen_en.ts", "-qm", str(cls.translation)], check=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.translator = QTranslator()
        self.window.show()
        # The former central widget is deliberately destroyed. All controller
        # controls must still work after this event, including retranslation.
        self.app.sendPostedEvents(None, QEvent.Type.DeferredDelete)
        self.app.processEvents()

    def tearDown(self):
        self.app.removeTranslator(self.translator)
        self.window.close()
        self.window.deleteLater()
        self.app.sendPostedEvents(None, QEvent.Type.DeferredDelete)

    def english(self):
        self.assertTrue(self.translator.load(str(self.translation)))
        self.app.installTranslator(self.translator)
        self.ui.retranslateUi(self.window)
        self.ui.set_language(self.window, AppLang.ENGLISH)
        self.app.processEvents()

    def test_language_switch_preserves_query_selection_and_counts(self):
        self.ui.searchWord.setText("الرحمة")
        self.ui.fullWordRadioButton.click()
        self.ui.matchesNumber.setText("1234")
        self.english()
        self.assertEqual(self.window.layoutDirection(), Qt.LayoutDirection.LeftToRight)
        self.assertEqual(self.ui.fullWordRadioButton.text(), "Full word")
        self.assertEqual(self.ui.searchWord.layoutDirection(), Qt.LayoutDirection.RightToLeft)
        self.app.removeTranslator(self.translator)
        self.ui.retranslateUi(self.window)
        self.ui.set_language(self.window, AppLang.ARABIC)
        self.assertEqual(self.window.layoutDirection(), Qt.LayoutDirection.RightToLeft)
        self.assertEqual(self.ui.fullWordRadioButton.text(), "كلمة كاملة")
        self.assertEqual(self.ui.searchWord.text(), "الرحمة")
        self.assertTrue(self.ui.fullWordRadioButton.isChecked())
        self.assertEqual(self.ui.matchesNumber.text(), "1234")

    def test_existing_search_controls_and_signals_survive_reparenting(self):
        group = self.ui.searchOptionsButtonGroup
        spy = QSignalSpy(group.buttonToggled)
        self.assertEqual(len(group.buttons()), 9)
        for button in self.ui.mode_buttons:
            button.click()
            self.assertIs(group.checkedButton(), button)
            self.assertEqual(sum(b.isChecked() for b in group.buttons()), 1)
        self.assertGreater(spy.count(), 0)
        self.ui.similarityThresholdSlider.setValue(3)
        self.assertEqual(self.ui.similarityThresholdSlider.value(), 3)
        self.ui.optionalAlTarifCheckbox.click()
        self.assertTrue(self.ui.optionalAlTarifCheckbox.isChecked())
        self.ui.searchWord.setValidator(ArabicWithRegexValidator())
        self.ui.searchWord.setText("الرحمة")
        QTest.keyClicks(self.ui.searchWord, "abc")
        self.assertEqual(self.ui.searchWord.text(), "الرحمة")

    def test_browse_button_triggers_existing_action(self):
        spy = QSignalSpy(self.ui.mushafNavigationButton.triggered)
        self.ui.browse_button.click()
        self.assertEqual(spy.count(), 1)

    def test_search_shortcut_and_read_only_counts(self):
        self.ui.searchWord.setText("الرحمة")
        self.ui.fullWordRadioButton.setFocus()
        self.window.activateWindow()
        self.app.processEvents()
        QTest.keyClick(self.window, Qt.Key.Key_F, Qt.KeyboardModifier.ControlModifier)
        self.assertTrue(self.ui.searchWord.hasFocus())
        self.assertEqual(self.ui.searchWord.selectedText(), "الرحمة")
        self.ui.matchesNumber.setText("42")
        QTest.keyClicks(self.ui.matchesNumber, "9")
        self.assertEqual(self.ui.matchesNumber.text(), "42")

    def test_both_layouts_fit_small_window_and_sidebar_scrolls(self):
        for language in (AppLang.ARABIC, AppLang.ENGLISH):
            if language == AppLang.ENGLISH:
                self.english()
            self.window.resize(940, 640)
            self.app.processEvents()
            for widget in (self.ui.searchWord, self.ui.tabWidget, self.ui.foundVerses,
                           self.ui.browse_button, self.ui.matchesNumber):
                with self.subTest(language=language, widget=widget.objectName()):
                    top_left = widget.mapTo(self.window, widget.rect().topLeft())
                    bottom_right = widget.mapTo(self.window, widget.rect().bottomRight())
                    self.assertTrue(self.window.rect().contains(top_left))
                    self.assertTrue(self.window.rect().contains(bottom_right))
            self.ui.options_button.setChecked(True)
            self.app.processEvents()
            self.ui.sidebar.ensureWidgetVisible(self.ui.regexRadioButton)
            self.app.processEvents()
            center = self.ui.regexRadioButton.mapTo(self.ui.sidebar.viewport(), self.ui.regexRadioButton.rect().center())
            self.assertTrue(self.ui.sidebar.viewport().rect().contains(center))
            self.ui.options_button.setChecked(False)

    def test_results_have_priority_in_both_languages(self):
        for language in (AppLang.ARABIC, AppLang.ENGLISH):
            if language == AppLang.ENGLISH:
                self.english()
            self.window.resize(1220, 860)
            self.app.processEvents()
            with self.subTest(language=language):
                self.assertTrue(self.ui.sidebar.isVisible())
                self.assertTrue(self.ui.options_button.isChecked())
                self.assertGreater(self.ui.foundVerses.width(), self.window.width() * 0.70)
                self.assertGreater(self.ui.foundVerses.height(), self.window.height() * 0.55)
                self.ui.options_button.setChecked(False)
                self.app.processEvents()
                self.assertFalse(self.ui.sidebar.isVisible())
                self.assertGreater(self.ui.foundVerses.width(), self.window.width() * 0.95)
                self.ui.options_button.setChecked(True)

    def test_query_is_physically_right_aligned_in_both_languages(self):
        for language in (AppLang.ARABIC, AppLang.ENGLISH):
            if language == AppLang.ENGLISH:
                self.english()
            for query in ("الرحمة", "123", "^الله$"):
                self.ui.searchWord.setText(query)
                self.ui.searchWord.setCursorPosition(len(query))
                self.app.processEvents()
                with self.subTest(language=language, query=query):
                    self.assertGreater(self.ui.searchWord.cursorRect().left(), self.ui.searchWord.width() * 0.65)
                    self.assertTrue(self.ui.searchWord.alignment() & Qt.AlignAbsolute)

    def test_matching_options_stay_next_to_query_and_remain_visible(self):
        for language in (AppLang.ARABIC, AppLang.ENGLISH):
            if language == AppLang.ENGLISH:
                self.english()
            self.window.resize(940, 640)
            self.app.processEvents()
            query_bottom = self.ui.searchWord.mapTo(self.window, self.ui.searchWord.rect().bottomLeft()).y()
            query_left = self.ui.searchWord.mapTo(self.window, self.ui.searchWord.rect().topLeft()).x()
            options_left = self.ui.matching_options.mapTo(self.window, self.ui.matching_options.rect().topLeft()).x()
            self.assertEqual(options_left, query_left)
            self.assertEqual(self.ui.matching_options.width(), self.ui.searchWord.width())
            for checkbox in self.ui.refinements:
                self.assertTrue(checkbox.isVisible())
                top = checkbox.mapTo(self.window, checkbox.rect().topLeft()).y()
                self.assertGreater(top, query_bottom)
                self.assertLess(top - query_bottom, 35)
            self.ui.options_button.setChecked(False)
            self.assertTrue(self.ui.matching_options.isVisible())
            self.ui.options_button.setChecked(True)

    def test_space_keeps_caret_at_visual_end_after_keyboard_direction_change(self):
        field = self.ui.searchWord
        for language in (AppLang.ARABIC, AppLang.ENGLISH):
            if language == AppLang.ENGLISH:
                self.english()
            field.clear()
            field.setFocus()
            # This is the direction event delivered by native keyboard-layout
            # changes. Widget layoutDirection alone does not govern the caret.
            QTest.keyClick(field, Qt.Key_Direction_L)
            typed = ""
            for char in "بسم الله الرحمن":
                before = field.cursorRect().x()
                if char == " ":
                    QTest.keyClick(field, Qt.Key_Space)
                else:
                    self.app.sendEvent(field, QKeyEvent(QEvent.KeyPress, Qt.Key_unknown, Qt.NoModifier, char))
                typed += char
                self.app.processEvents()
                self.assertEqual(field.text(), typed)
                self.assertEqual(field.cursorPosition(), len(typed))
                if char == " ":
                    self.assertLess(field.cursorRect().x(), before)
                    self.assertLess(before - field.cursorRect().x(), field.fontMetrics().height())
                    QTest.keyClick(field, Qt.Key_Direction_L)

    def test_english_hints_are_left_aligned_but_query_stays_right_aligned(self):
        self.english()
        field = self.ui.searchWord
        hint = self.ui.results_placeholder.label
        self.assertTrue(field.alignment() & Qt.AlignLeft)
        self.assertTrue(hint.alignment() & Qt.AlignLeft)
        self.assertTrue(hint.alignment() & Qt.AlignAbsolute)
        browser = self.ui.foundVerses
        browser.append("<p>رحمة الله</p>")
        self.app.processEvents()
        self.assertFalse(hint.isVisible())
        self.assertGreater(browser.cursorRect().x(), browser.viewport().width() * 0.65)
        browser.clear()
        self.assertTrue(hint.isVisible())
        self.assertTrue(hint.alignment() & Qt.AlignLeft)
        field.insert("الرحمة")
        self.assertTrue(field.alignment() & Qt.AlignRight)
        field.clear()
        self.assertTrue(field.alignment() & Qt.AlignLeft)
        self.app.removeTranslator(self.translator)
        self.ui.retranslateUi(self.window)
        self.ui.set_language(self.window, AppLang.ARABIC)
        self.assertTrue(field.alignment() & Qt.AlignRight)
        self.assertTrue(hint.alignment() & Qt.AlignRight)

    def test_query_editing_preserves_selection_undo_and_validators(self):
        from text_validators.composite_validator import CompositeValidator
        field = self.ui.searchWord
        field.setValidator(CompositeValidator(None))
        field.insert("بسم الله")
        field.setSelection(4, 4)
        field.insert("الرحمن")
        self.assertEqual(field.text(), "بسم الرحمن")
        field.undo()
        self.assertEqual(field.text(), "بسم الله")
        field.deselect()
        field.setCursorPosition(3)
        QTest.keyClick(field, Qt.Key_Space)
        self.assertEqual(field.text(), "بسم الله")  # double spaces remain invalid
        field.setCursorPosition(len(field.text()))
        QTest.keyClick(field, Qt.Key_Backspace)
        self.assertEqual(field.text(), "بسم الل")
        field.undo()
        field.insert("abc")
        self.assertEqual(field.text(), "بسم الله")
        field.setValidator(ArabicWithRegexValidator())
        field.selectAll()
        field.insert("^(الله|رحمة)$")
        self.assertEqual(field.text(), "^(الله|رحمة)$")

    def test_results_hint_is_right_aligned_and_never_becomes_result_content(self):
        label = self.ui.results_placeholder.label
        self.assertTrue(label.isVisible())
        self.assertTrue(label.alignment() & Qt.AlignRight)
        self.assertTrue(label.alignment() & Qt.AlignAbsolute)
        self.assertTrue(label.testAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents))
        self.assertTrue(self.ui.foundVerses.document().isEmpty())
        self.ui.foundVerses.setPlainText("نتيجة تجريبية")
        self.assertFalse(label.isVisible())
        self.english()
        self.assertFalse(label.isVisible())
        self.assertEqual(self.ui.foundVerses.toPlainText(), "نتيجة تجريبية")
        self.ui.foundVerses.clear()
        self.assertTrue(label.isVisible())
        self.window.resize(940, 640)
        self.app.processEvents()
        self.assertTrue(self.ui.foundVerses.viewport().rect().contains(label.geometry()))

    def test_options_panel_preserves_search_and_results(self):
        self.ui.searchWord.setText("الرحمة")
        self.ui.foundVerses.setPlainText("نتيجة تجريبية")
        self.ui.matchesNumber.setText("1234567")
        query_changes = QSignalSpy(self.ui.searchWord.textChanged)
        self.assertTrue(self.ui.sidebar.isVisible())
        self.ui.fullWordRadioButton.click()
        self.ui.optionalAlTarifCheckbox.click()
        self.assertIn(self.ui.fullWordRadioButton.text(), self.ui.options_button.accessibleName())
        self.assertIn("(+1)", self.ui.options_button.accessibleName())
        self.english()
        self.assertTrue(self.ui.sidebar.isVisible())
        self.assertIn("Full word", self.ui.options_button.accessibleName())
        QTest.mouseClick(self.ui.options_button, Qt.MouseButton.LeftButton)
        self.app.processEvents()
        self.assertFalse(self.ui.sidebar.isVisible())
        self.assertTrue(self.ui.fullWordRadioButton.isChecked())
        self.assertTrue(self.ui.optionalAlTarifCheckbox.isChecked())
        self.assertEqual(self.ui.searchWord.text(), "الرحمة")
        self.assertEqual(self.ui.foundVerses.toPlainText(), "نتيجة تجريبية")
        self.assertEqual(self.ui.matchesNumber.text(), "1234567")
        self.assertGreater(self.ui.matchesNumber.width(), self.ui.matchesNumber.fontMetrics().horizontalAdvance("1234567"))
        self.assertEqual(query_changes.count(), 0)
        self.assertTrue(self.ui.searchWord.hasFocus())

    def test_all_result_tabs_and_controller_visibility_remain_available(self):
        self.assertEqual(self.ui.tabWidget.count(), 4)
        self.window.resize(940, 640)
        for index in range(4):
            self.ui.tabWidget.setCurrentIndex(index)
            self.app.processEvents()
            self.assertTrue(self.ui.tabWidget.currentWidget().isVisible())
        self.ui.tabWidget.setCurrentIndex(2)
        self.app.processEvents()
        for checkbox in (self.ui.diacriticsCheckbox, self.ui.wordTransliterationCheckbox,
                         self.ui.wordMeaningCheckbox):
            self.assertGreaterEqual(checkbox.height(), checkbox.minimumSizeHint().height())
            self.assertGreaterEqual(checkbox.width(), checkbox.minimumSizeHint().width())
        self.ui.tabWidget.setTabVisible(3, False)
        self.assertFalse(self.ui.tabWidget.isTabVisible(3))
        self.ui.tabWidget.setTabVisible(3, True)
        self.assertTrue(self.ui.tabWidget.isTabVisible(3))


if __name__ == "__main__":
    unittest.main()
