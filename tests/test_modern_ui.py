"""Exercise the real Qt form without the separately distributed Quran dataset."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QEvent, QTranslator, Qt
from PySide6.QtGui import QFontDatabase
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
            self.window.resize(940, 780)
            self.app.processEvents()
            for widget in (self.ui.searchWord, self.ui.tabWidget, self.ui.foundVerses,
                           self.ui.browse_button, self.ui.matchesNumber):
                with self.subTest(language=language, widget=widget.objectName()):
                    top_left = widget.mapTo(self.window, widget.rect().topLeft())
                    bottom_right = widget.mapTo(self.window, widget.rect().bottomRight())
                    self.assertTrue(self.window.rect().contains(top_left))
                    self.assertTrue(self.window.rect().contains(bottom_right))
            self.ui.sidebar.ensureWidgetVisible(self.ui.regexRadioButton)
            self.app.processEvents()
            center = self.ui.regexRadioButton.mapTo(self.ui.sidebar.viewport(), self.ui.regexRadioButton.rect().center())
            self.assertTrue(self.ui.sidebar.viewport().rect().contains(center))

    def test_all_result_tabs_and_controller_visibility_remain_available(self):
        self.assertEqual(self.ui.tabWidget.count(), 4)
        self.window.resize(940, 780)
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
