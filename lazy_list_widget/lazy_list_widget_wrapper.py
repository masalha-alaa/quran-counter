from typing import Callable

from PySide6.QtCore import Signal, QThread, QTimer, QMutex
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QListWidget

from .abstract_subtext_getter import AbstractSubtextGetter
from .custom_list_widget_item import CustomListWidgetItem
from .custom_results_sort import CustomResultsSort
from .custom_results_sort_enum import CustomResultsSortEnum
from .custom_row import CustomRow


class SortingThread(QThread):
    result_ready = Signal(list, QThread)

    def __init__(self):
        super().__init__()
        self.data = None
        self.sorting_method: CustomResultsSort | None = None
        self.subtext_getter: AbstractSubtextGetter | None = None

    def run(self):
        match self.sorting_method:
            case CustomResultsSortEnum.BY_NUMBER:
                self.data = sorted(self.data, key=lambda x: int(self.subtext_getter.find_number(x.label) or -1))
            case CustomResultsSortEnum.BY_NAME:
                self.data = sorted(self.data, key=lambda x: (self.subtext_getter.find_name(x.label) or -1,
                                                             int(self.subtext_getter.number or -1)))
            case CustomResultsSortEnum.BY_RESULT_ASCENDING:
                self.data = sorted(self.data, key=lambda x: (int(self.subtext_getter.find_result(x.label) or -1),
                                                             self.subtext_getter.name or -1,
                                                             int(self.subtext_getter.number or -1)))
            case CustomResultsSortEnum.BY_RESULT_DESCENDING:
                self.data = sorted(self.data, key=lambda x: (int(self.subtext_getter.find_result(x.label) or -1),
                                                             self.subtext_getter.name or -1,
                                                             int(self.subtext_getter.number or -1)),
                                   reverse=True)
            case _:
                self.data = sorted(self.data, key=lambda x: x.label)
        self.result_ready.emit(self.data, self)


class LazyListWidgetWrapper:
    REMOVE_THREAD_AFTER_MS = 1000
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self, parent: QListWidget, subtext_getter: AbstractSubtextGetter, default_items_load=30,
                 row_widget: type[CustomListWidgetItem] = None, supported_methods=None,
                 initial_sorting_method: CustomResultsSortEnum = None):
        self._exhausted = object()
        self._threads = set()
        self.list_widget = parent
        self.list_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.list_widget.verticalScrollBar().valueChanged.connect(self.after_scroll)
        self.list_widget.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self._prev_scrolling_value = 0
        self._default_items_load = default_items_load
        self._rows: list | None = None
        self._rows_iter = None
        self._adding_items = False
        self._row_widget = row_widget if row_widget else CustomListWidgetItem
        self._selection_changed_callback = None
        self._item_double_clicked_callback = None

        if supported_methods is None:
            supported_methods = list(CustomResultsSortEnum)
        if initial_sorting_method is None:
            initial_sorting_method = supported_methods[0]
        self.supported_methods = supported_methods
        self.sorting_method = CustomResultsSort(initial_sorting_method)
        self.subtext_getter = subtext_getter
        self._sorting_done_callback = None

    def add_thread(self, thread):
        # LazyListWidgetWrapper.RUNNING_THREADS_MUTEX.lock()
        self._threads.add(thread)
        # LazyListWidgetWrapper.RUNNING_THREADS_MUTEX.unlock()

    def remove_thread(self, thread):
        # LazyListWidgetWrapper.RUNNING_THREADS_MUTEX.lock()
        self._threads.remove(thread)
        # LazyListWidgetWrapper.RUNNING_THREADS_MUTEX.unlock()

    def set_sorting_done_callback(self, callback):
        self._sorting_done_callback = callback

    # SELECTION CALLBACKS [BEGIN]
    def set_item_selection_changed_callback(self, callback: Callable[[list[CustomListWidgetItem]], None]):
        self._selection_changed_callback = callback
        if self._selection_changed_callback:
            self.list_widget.itemSelectionChanged.connect(self._selection_changed)

    def disconnect_item_selection_changed_callback(self):
        self.list_widget.itemSelectionChanged.disconnect(self._selection_changed)

    def _selection_changed(self):
        if self._selection_changed_callback:
            self._selection_changed_callback(self.list_widget.selectedItems())

    # SELECTION CALLBACKS [END]

    # DOUBLE CLICK CALLBACKS [BEGIN]
    def set_item_double_clicked_callback(self, callback: Callable[[CustomRow], None]):
        self._item_double_clicked_callback = callback
        if self._item_double_clicked_callback:
            self.list_widget.itemDoubleClicked.connect(self._item_double_clicked)

    def disconnect_item_double_clicked_callback(self):
        self.list_widget.itemDoubleClicked.disconnect(self._item_double_clicked)

    def _item_double_clicked(self, item: CustomListWidgetItem):
        if self._item_double_clicked_callback:
            self._item_double_clicked_callback(item.row)

    # DOUBLE CLICK CALLBACKS [END]

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
        for i in range(how_many):
            if (row := next(self._rows_iter, self._exhausted)) is self._exhausted:
                return _done()
            # self.list_widget.addItem(self._row_widget(row, self.subtext_getter, self.get_current_sorting))
            self.list_widget.addItem(self._row_widget(row, i+1))
            # self.list_widget.addItem(row.label)
        return _done()

    def clear(self):
        self.list_widget.clear()
        # QTimer.singleShot(0, self.list_widget.clear)
        self.list_widget.verticalScrollBar().setValue(0)

    def sort(self):
        # self.list_widget.sortItems()
        sorting_thread = SortingThread()
        sorting_thread.data = self._rows
        sorting_thread.sorting_method = self.get_current_sorting()
        sorting_thread.subtext_getter = self.subtext_getter
        sorting_thread.result_ready.connect(self._sorting_done)
        self.add_thread(sorting_thread)
        sorting_thread.start()

    def _sorting_done(self, sorted_data: list, caller_thread: SortingThread):
        caller_thread.result_ready.disconnect(self._sorting_done)
        QTimer.singleShot(LazyListWidgetWrapper.REMOVE_THREAD_AFTER_MS, lambda: self.remove_thread(caller_thread))
        self._rows = sorted_data
        self._rows_iter = iter(self._rows)
        self.clear()
        self.load_more_items()
        if self._sorting_done_callback:
            self._sorting_done_callback()

    def switch_order(self):
        new_order = None
        while new_order not in self.supported_methods:
            new_order = self.sorting_method.switch_order()
        return new_order

    def get_current_sorting(self):
        return self.sorting_method.get_current()
