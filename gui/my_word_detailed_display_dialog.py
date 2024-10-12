from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QEvent
from gui.word_detailed_display import Ui_DetailedWordDisplayDialog
from lazy_list_widget import CustomRow
from my_data_loader import MyDataLoader
from PySide6.QtCore import Qt
from arabic_reformer import reform_text
from emphasizer import emphasize_span, CssColors


class MyWordDetailedDisplayDialog(QDialog, Ui_DetailedWordDisplayDialog):
    ITEM_LOAD = 25
    _exhausted = object()

    def __init__(self):
        super(MyWordDetailedDisplayDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowMaximizeButtonHint |
                            Qt.WindowType.WindowMinimizeButtonHint)
        self._row_data: CustomRow | None = None
        self._data_iter = None
        self._adding_items = False
        self._prev_scrolling_value = 0
        self.colorizeCheckbox.stateChanged.connect(self._toggle_colorize)
        self.textBrowser.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self.textBrowser.verticalScrollBar().valueChanged.connect(self.after_scroll)
        # TODO: Make dialog title as the word in self._row_data.label

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        if self._row_data:
            self.load_more_items(MyWordDetailedDisplayDialog.ITEM_LOAD, prevent_scrolling=True)

    def set_data(self, row_data: CustomRow):
        self._clear()
        self._row_data = row_data
        self._reset_iter()

    def _reset_iter(self):
        self._data_iter = iter(self._row_data.metadata.items())

    def load_more_items(self, items_to_load, prevent_scrolling=False):
        def _done():
            if prevent_scrolling:
                scrollbar.setValue(current_scroll_value)
            self._adding_items = False
            return

        self._adding_items = True
        scrollbar = self.textBrowser.verticalScrollBar()
        current_scroll_value = scrollbar.value()
        for _ in range(items_to_load):
            if (row_metadata := next(self._data_iter, MyWordDetailedDisplayDialog._exhausted)) is MyWordDetailedDisplayDialog._exhausted:
                return _done()

            (surah_num, verse_num), spans = row_metadata
            verse = MyDataLoader.get_verse(surah_num, verse_num)
            if self.colorizeCheckbox.isChecked():
                verse = self._reform_and_color(verse, spans)
            ref = f"{surah_num}:{verse_num}"
            line = f"<p>{ref}: {verse}</p>"
            # line = f"{ref}: {verse}"
            self.textBrowser.append(line)

        return _done()

    def _reform_and_color(self, verse, spans):
        verse = reform_text(verse, text_may_contain_diacritics=True)
        verse = emphasize_span(verse, spans, capitalize=False, underline=False, color=CssColors.CYAN, css=True)
        return verse

    def _clear(self):
        self.textBrowser.clear()
        self.textBrowser.verticalScrollBar().setValue(0)

    # SIGNALS
    def _toggle_colorize(self, state):
        self._clear()
        self._reset_iter()
        self.load_more_items(MyWordDetailedDisplayDialog.ITEM_LOAD, prevent_scrolling=True)

    def before_scroll(self):
        scrollbar = self.textBrowser.verticalScrollBar()
        self._prev_scrolling_value = scrollbar.value()

    def after_scroll(self):
        if self._adding_items or ((scrollbar := self.textBrowser.verticalScrollBar()).value() < self._prev_scrolling_value):
            return "break"
        current_val = scrollbar.value()
        # print(f"{scrollbar.value()}/{scrollbar.maximum()}")
        if scrollbar.value() > 0.85 * scrollbar.maximum():  # At the bottom
            self.load_more_items(MyWordDetailedDisplayDialog.ITEM_LOAD)
            scrollbar.setValue(min(scrollbar.maximum(), current_val))

    def resizeEvent(self, event):
        scrollbar = self.textBrowser.verticalScrollBar()
        if scrollbar.value() > 0.85 * scrollbar.maximum():
            self._prev_scrolling_value = scrollbar.value()
            self.load_more_items(MyWordDetailedDisplayDialog.ITEM_LOAD, prevent_scrolling=True)
        super().resizeEvent(event)
