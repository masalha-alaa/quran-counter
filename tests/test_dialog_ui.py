"""Exercise all dialog layouts and local interactions without starting workers."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from PySide6.QtCore import QEvent, QTranslator, Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtTest import QSignalSpy
from PySide6.QtWidgets import QApplication, QAbstractButton, QLineEdit
from gui.dialog_style import set_dialog_language
from my_utils.my_enums import AppLang
from tools.render_dialog_previews import FORMS, create_dialog


class DialogUiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        QFontDatabase.addApplicationFont("fonts/NotoNaskhArabic-VariableFont_wght.ttf")
        cls.temp = tempfile.TemporaryDirectory()
        subprocess.run([sys.executable, "tools/compile_translations.py", "--output-dir", cls.temp.name], check=True, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.dialogs = []
        self.translator = QTranslator()

    def tearDown(self):
        self.app.removeTranslator(self.translator)
        for dialog in self.dialogs:
            dialog.close()
            dialog.deleteLater()
        self.app.sendPostedEvents(None, QEvent.DeferredDelete)

    def create(self, kind):
        dialog, ui = create_dialog(kind)
        self.dialogs.append(dialog)
        return dialog, ui

    def language(self, kind, dialog, ui, language):
        self.app.removeTranslator(self.translator)
        catalog = FORMS[kind][2]
        self.assertTrue(self.translator.load(str(Path(self.temp.name) / f"{catalog}_{language.value}.qm")))
        self.app.installTranslator(self.translator)
        ui.retranslateUi(dialog)
        set_dialog_language(dialog, language)
        self.app.processEvents()

    def test_every_dialog_translates_and_visible_controls_fit(self):
        for kind in FORMS:
            dialog, ui = self.create(kind)
            dialog.show()
            for language in (AppLang.ENGLISH, AppLang.ARABIC):
                self.language(kind, dialog, ui, language)
                self.assertEqual(dialog.layoutDirection(), Qt.LeftToRight if language == AppLang.ENGLISH else Qt.RightToLeft)
                self.assertEqual(dialog._modern_title.text(), dialog.windowTitle())
                for widget in dialog.findChildren(QAbstractButton) + dialog.findChildren(QLineEdit):
                    if widget.isVisible() and widget.parent() is not ui.__dict__.get("textBrowser"):
                        with self.subTest(kind=kind, language=language, control=widget.objectName()):
                            self.assertTrue(dialog.rect().contains(widget.mapTo(dialog, widget.rect().topLeft())))
                            self.assertTrue(dialog.rect().contains(widget.mapTo(dialog, widget.rect().bottomRight())))
            dialog.hide()

    def test_reader_navigation_selection_and_statistics_stay_usable(self):
        dialog, ui = self.create("mushaf")
        dialog.show()
        self.app.processEvents()
        self.assertGreater(ui.textBrowser.height(), dialog.height() * 0.50)
        navigation = QSignalSpy(ui.goToPageButton.clicked)
        ui.pageInput.setText("23")
        ui.goToPageButton.click()
        self.assertEqual(navigation.count(), 1)
        ui.textBrowser.setPlainText("نص للاختبار")
        cursor = ui.textBrowser.textCursor()
        cursor.select(cursor.SelectionType.Document)
        ui.textBrowser.setTextCursor(cursor)
        selected = cursor.selectedText()
        ui.selection_toggle.click()
        self.assertTrue(ui.frame_2.isVisible())
        self.assertEqual(ui.textBrowser.textCursor().selectedText(), selected)
        selection = QSignalSpy(ui.selectionStartButton.clicked)
        ui.selectionStartButton.click()
        self.assertEqual(selection.count(), 1)
        ui.reader_tabs.setCurrentIndex(1)
        self.app.processEvents()
        self.assertTrue(ui.lettersHistogram.isVisible())
        self.assertTrue(ui.differentRootCheckBox.isVisible())
        ui.differentRootCheckBox.click()
        self.language("mushaf", dialog, ui, AppLang.ENGLISH)
        self.assertEqual(ui.pageInput.text(), "23")
        self.assertTrue(ui.differentRootCheckBox.isChecked())
        self.assertEqual(ui.reader_tabs.currentIndex(), 1)
        self.assertEqual(ui.reader_tabs.tabText(0), "Reading")
        ui.reader_tabs.setCurrentIndex(0)
        ui.selection_toggle.click()
        self.assertFalse(ui.frame_2.isVisible())
        self.assertEqual(ui.textBrowser.toPlainText(), "نص للاختبار")

    def test_detail_content_survives_language_and_close_works(self):
        dialog, ui = self.create("details")
        dialog.show()
        ui.textBrowser.setPlainText("نتيجة")
        colorized = QSignalSpy(ui.colorizeCheckbox.toggled)
        ui.colorizeCheckbox.click()
        self.assertEqual(colorized.count(), 1)
        self.language("details", dialog, ui, AppLang.ENGLISH)
        self.assertEqual(ui.textBrowser.toPlainText(), "نتيجة")
        self.assertEqual(dialog._modern_close.text(), "Close")
        self.language("details", dialog, ui, AppLang.ARABIC)
        self.assertEqual(dialog._modern_close.text(), "إغلاق")
        rejected = QSignalSpy(dialog.rejected)
        dialog._modern_close.click()
        self.assertEqual(rejected.count(), 1)

    def test_key_translation_and_input_direction(self):
        dialog, ui = self.create("key")
        dialog.show()
        ui.enterKeyLineEdit.setText("sample-key")
        self.language("key", dialog, ui, AppLang.ENGLISH)
        self.assertEqual(dialog.windowTitle(), "Key Setup")
        self.assertEqual(ui.okButton.text(), "Apply")
        self.assertEqual(ui.label_2.text(), "You can obtain a key from the website:")
        self.language("key", dialog, ui, AppLang.ARABIC)
        self.assertEqual(ui.enterKeyLineEdit.text(), "sample-key")
        self.assertEqual(ui.enterKeyLineEdit.layoutDirection(), Qt.LeftToRight)
        self.assertTrue(ui.enterKeyLineEdit.alignment() & Qt.AlignAbsolute)

    def test_meaning_selection_and_progress_survive_translation(self):
        dialog, ui = self.create("disambiguation")
        dialog.show()
        ui.resultsListWidget.addItems(["one", "two"])
        ui.resultsListWidget.setCurrentRow(1)
        self.language("disambiguation", dialog, ui, AppLang.ENGLISH)
        self.assertEqual(ui.resultsListWidget.currentItem().text(), "two")
        self.assertEqual(ui.resultsListWidget.layoutDirection(), Qt.LeftToRight)
        dialog, ui = self.create("download")
        ui.progressBar.setValue(47)
        self.language("download", dialog, ui, AppLang.ENGLISH)
        self.assertEqual(ui.progressBar.value(), 47)


if __name__ == "__main__":
    unittest.main()
