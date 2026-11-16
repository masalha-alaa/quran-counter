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
from PySide6.QtWidgets import QApplication, QAbstractButton, QLineEdit, QTabWidget, QGridLayout, QBoxLayout, QWidget
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
                self.assertEqual(dialog.layoutDirection(), Qt.LeftToRight if kind == "mushaf" or language == AppLang.ENGLISH else Qt.RightToLeft)
                if kind == "mushaf":
                    self.assertFalse(hasattr(dialog, "_modern_title"))
                else:
                    self.assertEqual(dialog._modern_title.text(), dialog.windowTitle())
                for widget in dialog.findChildren(QAbstractButton) + dialog.findChildren(QLineEdit):
                    if widget.isVisible() and widget.parent() is not ui.__dict__.get("textBrowser"):
                        with self.subTest(kind=kind, language=language, control=widget.objectName()):
                            self.assertTrue(dialog.rect().contains(widget.mapTo(dialog, widget.rect().topLeft())))
                            self.assertTrue(dialog.rect().contains(widget.mapTo(dialog, widget.rect().bottomRight())))
            dialog.hide()

    def test_mushaf_preserves_original_designer_layouts(self):
        original, original_ui = create_dialog("mushaf", original=True)
        self.dialogs.append(original)
        dialog, ui = self.create("mushaf")

        def layout_snapshot(layout):
            items = []
            for index in range(layout.count()):
                item = layout.itemAt(index)
                if item.widget():
                    value = ("widget", item.widget().objectName())
                elif item.layout():
                    value = layout_snapshot(item.layout())
                else:
                    spacer = item.spacerItem()
                    value = ("spacer", spacer.sizeHint(), spacer.sizePolicy())
                position = layout.getItemPosition(index) if isinstance(layout, QGridLayout) else None
                stretch = layout.stretch(index) if isinstance(layout, QBoxLayout) else None
                items.append((value, position, stretch))
            margins = layout.contentsMargins()
            return (layout.objectName(), layout.spacing(),
                    (margins.left(), margins.top(), margins.right(), margins.bottom()), items)

        self.assertEqual(layout_snapshot(dialog.layout()), layout_snapshot(original.layout()))
        # Frames have their own layouts; compare these too, not only the root.
        for name, old_widget in vars(original_ui).items():
            if isinstance(old_widget, QWidget):
                new_widget = getattr(ui, name)
                self.assertEqual(new_widget.parentWidget().objectName(), old_widget.parentWidget().objectName(), name)
                self.assertEqual(new_widget.layoutDirection(), old_widget.layoutDirection(), name)
                self.assertEqual(new_widget.minimumSize(), old_widget.minimumSize(), name)
                self.assertEqual(new_widget.maximumSize(), old_widget.maximumSize(), name)
                if old_widget.layout():
                    self.assertEqual(layout_snapshot(new_widget.layout()), layout_snapshot(old_widget.layout()), name)
        self.assertEqual(dialog.size(), original.size())
        self.assertFalse(dialog.findChildren(QTabWidget))
        self.assertFalse(hasattr(dialog, "_modern_title"))

        for language in (AppLang.ARABIC, AppLang.ENGLISH):
            self.language("mushaf", dialog, ui, language)
            for size in ((1920, 1110), (1116, 853)):
                dialog.resize(*size)
                dialog.show()
                self.app.processEvents()
                def rect(widget):
                    return widget.rect().translated(widget.mapTo(dialog, widget.rect().topLeft()))
                with self.subTest(language=language, size=size):
                    self.assertLess(rect(ui.frame_2).right(), rect(ui.pageInput).left())
                    self.assertLess(rect(ui.frame_2).bottom(), rect(ui.textBrowser).top())
                    self.assertLess(rect(ui.textBrowser).bottom(), rect(ui.frame_4).top() + 1)
                    self.assertLess(rect(ui.frame_4).bottom(), rect(ui.frame).top())
                    self.assertLess(rect(ui.frame).bottom(), rect(ui.lettersHistogram).top())
                    self.assertLess(rect(ui.exclusiveWordsFrame).right(), rect(ui.frame_3).left())
                    self.assertLess(rect(ui.lettersSumTableWidget).right(), rect(ui.lettersHistogram).left() + 1)
                    self.assertLess(rect(ui.pageNumDisplay).right(), rect(ui.juzzNumDisplay).left())
                    self.assertTrue(ui.selectionStartButton.isVisible())
                    self.assertTrue(ui.selectionEndButton.isVisible())

    def test_mushaf_keeps_stats_visible_and_original_controls_usable(self):
        dialog, ui = self.create("mushaf")
        dialog.resize(1920, 1110)
        dialog.show()
        self.app.processEvents()
        self.assertTrue(ui.frame.isVisible())
        self.assertFalse(hasattr(ui, "stats_toggle"))
        navigation = QSignalSpy(ui.goToPageButton.clicked)
        ui.pageInput.setText("23")
        ui.goToPageButton.click()
        self.assertEqual(navigation.count(), 1)
        ui.textBrowser.setPlainText("نص للاختبار")
        cursor = ui.textBrowser.textCursor()
        cursor.select(cursor.SelectionType.Document)
        ui.textBrowser.setTextCursor(cursor)
        selected = cursor.selectedText()
        histogram_rect = ui.lettersHistogram.geometry()
        ui.differentRootCheckBox.click()
        self.app.processEvents()
        self.assertTrue(ui.frame.isVisible())
        self.assertTrue(ui.lettersHistogram.isVisible())
        self.assertTrue(ui.lettersSumTableWidget.isVisible())
        self.assertTrue(ui.frame_2.isVisible())
        self.assertEqual(ui.lettersHistogram.geometry(), histogram_rect)
        self.assertEqual(ui.textBrowser.textCursor().selectedText(), selected)
        selection = QSignalSpy(ui.selectionStartButton.clicked)
        ui.selectionStartButton.click()
        self.assertEqual(selection.count(), 1)
        self.language("mushaf", dialog, ui, AppLang.ENGLISH)
        self.assertTrue(ui.frame.isVisible())
        self.assertEqual(ui.pageInput.text(), "23")
        self.app.processEvents()
        self.assertTrue(ui.frame.isVisible())
        self.assertTrue(ui.differentRootCheckBox.isChecked())
        self.assertEqual(ui.textBrowser.toPlainText(), "نص للاختبار")
        self.assertEqual(ui.lettersHistogram.geometry(), histogram_rect)

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
