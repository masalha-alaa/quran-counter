from typing import Callable

from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QListWidget

from .custom_results_sort_enum import CustomResultsSortEnum
from .custom_results_sort import CustomResultsSort
from .custom_list_widget_item import CustomListWidgetItem
from .abstract_subtext_getter import AbstractSubtextGetter


class LazyListWidgetWrapper:
    def __init__(self, parent: QListWidget, subtext_getter: AbstractSubtextGetter, default_items_load=30,
                 row_widget: type[CustomListWidgetItem] = None, supported_methods=None,
                 initial_sorting_method: CustomResultsSortEnum = None):
        self._exhausted = object()
        self.list_widget = parent
        self.list_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.list_widget.verticalScrollBar().valueChanged.connect(self.after_scroll)
        self.list_widget.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self._prev_scrolling_value = 0
        self._default_items_load = default_items_load
        self._rows = None
        self._rows_iter = None
        self._adding_items = False
        self._row_widget = row_widget if row_widget else CustomListWidgetItem
        self._selection_changed_callback = None

        if supported_methods is None:
            supported_methods = list(CustomResultsSortEnum)
        if initial_sorting_method is None:
            initial_sorting_method = supported_methods[0]
        self.supported_methods = supported_methods
        self.sorting_method = CustomResultsSort(initial_sorting_method)
        self.subtext_getter = subtext_getter

    def set_item_selection_changed_signal(self, callback: Callable[[list[CustomListWidgetItem]], None]):
        self._selection_changed_callback = callback
        if self._selection_changed_callback:
            self.list_widget.itemSelectionChanged.connect(self._selection_changed)

    def disconnect_item_selection_changed_signal(self):
        self.list_widget.itemSelectionChanged.disconnect(self._selection_changed)

    def _selection_changed(self):
        if self._selection_changed_callback:
            self._selection_changed_callback(self.list_widget.selectedItems())

    def before_scroll(self):
        scrollbar = self.list_widget.verticalScrollBar()
        self._prev_scrolling_value = scrollbar.value()

    def after_scroll(self):
        if self._adding_items or (
                (scrollbar := self.list_widget.verticalScrollBar()).value() < self._prev_scrolling_value):
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
            self.list_widget.addItem(self._row_widget(row, self.subtext_getter, self.get_current_sorting))
        return _done()

    def clear(self):
        self.list_widget.clear()
        # QTimer.singleShot(0, self.list_widget.clear)
        self.list_widget.verticalScrollBar().setValue(0)

    def sort(self):
        self.list_widget.sortItems()

    def switch_order(self):
        new_order = None
        while new_order not in self.supported_methods:
            new_order = self.sorting_method.switch_order()
        return new_order

    def get_current_sorting(self):
        return self.sorting_method.get_current()
