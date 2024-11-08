from typing import Any
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QDialog
from gui.detailed_display_dialog.word_detailed_display_dialog import Ui_DetailedWordDisplayDialog
from my_widgets.lazy_list_widget import CustomRow
from PySide6.QtCore import Qt
from arabic_reformer import reform_text
from my_utils.emphasizer import emphasize_span, CssColors
from my_utils.utils import AppLang


class BaseDetailedDisplayDialog(QDialog, Ui_DetailedWordDisplayDialog):
    def __init__(self, language: None | AppLang, items_to_load=25):
        super(BaseDetailedDisplayDialog, self).__init__()
        self.setupUi(self)
        self._current_lang = None
        self._apply_language(language)
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowMaximizeButtonHint |
                            Qt.WindowType.WindowMinimizeButtonHint)
        self.items_to_load = items_to_load
        self._row_metadata:Any = None
        self._data_iter = None
        self._adding_items = False
        self._prev_scrolling_value = 0
        self.colorizeCheckbox.stateChanged.connect(self._toggle_colorize)
        self.textBrowser.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self.textBrowser.verticalScrollBar().valueChanged.connect(self.after_scroll)
        # TODO: Make dialog title as the word in self._row_data.label

    def set_language(self, lang):
        self._apply_language(lang)

    def _apply_language(self, lang):
        if lang != self._current_lang:
            self.retranslateUi(self)
            # self.set_font_for_language(lang)
            self._current_lang = lang

    @property
    def _exhausted(self):
        raise NotImplementedError

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        if self._row_metadata:
            self.load_more_items(self.items_to_load, prevent_scrolling=True)

    def set_data(self, row_metadata:Any):
        self._clear()
        self._row_metadata = row_metadata
        self._reset_iter()

    def _reset_iter(self):
        self._data_iter = iter(self._row_metadata)

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
            if (row_metadata := next(self._data_iter, self._exhausted)) is self._exhausted:
                return _done()
            self._append(row_metadata)

        return _done()

    def _append(self, row_metadata):
        raise NotImplementedError

    # def _append(self, row_metadata):
    #     surah_num, verse_num = row_metadata[0], row_metadata[1]
    #     verse = MyDataLoader.get_verse(int(surah_num), int(verse_num))
    #     if self.colorizeCheckbox.isChecked():
    #         verse = self._reform_and_color(verse, [(row_metadata[idx], row_metadata[idx + 1]) for idx in
    #                                                range(2, len(row_metadata), 2)])
    #     line = f"<p>{surah_num}:{verse_num}: {verse}</p>"
    #     # line = f"{ref}: {verse}"
    #     self.textBrowser.append(line)

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
        self.load_more_items(self.items_to_load, prevent_scrolling=True)

    def before_scroll(self):
        scrollbar = self.textBrowser.verticalScrollBar()
        self._prev_scrolling_value = scrollbar.value()

    def after_scroll(self):
        if self._adding_items or ((scrollbar := self.textBrowser.verticalScrollBar()).value() < self._prev_scrolling_value):
            return "break"
        current_val = scrollbar.value()
        # print(f"{scrollbar.value()}/{scrollbar.maximum()}")
        if scrollbar.value() > 0.85 * scrollbar.maximum():  # At the bottom
            self.load_more_items(self.items_to_load)
            scrollbar.setValue(min(scrollbar.maximum(), current_val))

    def resizeEvent(self, event):
        scrollbar = self.textBrowser.verticalScrollBar()
        if scrollbar.value() > 0.85 * scrollbar.maximum():
            self._prev_scrolling_value = scrollbar.value()
            self.load_more_items(self.items_to_load, prevent_scrolling=True)
        super().resizeEvent(event)
