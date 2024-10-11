from typing import Callable
from PySide6.QtWidgets import QListWidget, QListWidgetItem


class LazyListWidgetWrapper:
    def __init__(self, parent: QListWidget, default_items_load=30, add_item_function: Callable[[str], None] = None):
        self._exhausted = object()
        self.list_widget = parent
        self.list_widget.verticalScrollBar().valueChanged.connect(self.after_scroll)
        self.list_widget.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self._prev_scrolling_value = 0
        self._default_items_load = default_items_load
        self._rows = None
        self._rows_iter = None
        self._adding_items = False
        self._add_item_function = add_item_function

    def before_scroll(self):
        scrollbar = self.list_widget.verticalScrollBar()
        self._prev_scrolling_value = scrollbar.value()

    def after_scroll(self):
        if self._adding_items or ((scrollbar := self.list_widget.verticalScrollBar()).value() < self._prev_scrolling_value):
            return "break"
        current_val = scrollbar.value()
        if scrollbar.value() > 0.85 * scrollbar.maximum():  # At the bottom
            self.load_more_items(self._default_items_load)
            scrollbar.setValue(min(scrollbar.maximum(), current_val))

    def save_values(self, rows):
        self._rows = rows
        self._rows_iter = iter(self._rows)

    def load_more_items(self, how_many: int = None, prevent_scrolling=False):
        def _done():
            if prevent_scrolling:
                scrollbar.setValue(current_scroll_value)
            self._adding_items = False
            return

        self._adding_items = True
        scrollbar = self.list_widget.verticalScrollBar()
        current_scroll_value = scrollbar.value()

        if how_many is None:
            how_many = self._default_items_load
        for _ in range(how_many):
            if (row := next(self._rows_iter, self._exhausted)) is self._exhausted:
                return _done()
            self._add_item(row)
        return _done()

    def _add_item(self, row):
        if self._add_item_function:
            self._add_item_function(row)
        else:
            # default
            self.list_widget.addItem(QListWidgetItem(row))

    def clear(self):
        self.list_widget.clear()
        # QTimer.singleShot(0, self.list_widget.clear)
        self.list_widget.verticalScrollBar().setValue(0)