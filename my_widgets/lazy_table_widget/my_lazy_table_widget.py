from abc import abstractmethod
from typing import Callable, Any
from enum import Enum

from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QTableWidget
from PySide6.QtCore import Qt
from PySide6.QtCore import QEvent
from PySide6.QtGui import QColor

from my_utils.utils import translate_text
from .table_data_type import TableDataType
from .custom_table_row import CustomTableRow
from tabs_management.table_headers import TableHeaders
from .custom_table_widget_item import CustomTableWidgetItem


class SortingOrder(Enum):
    ASCENDING = 0
    DESCENDING = 1
    INITIAL = DESCENDING

    def convert_to_qt_sorting_type(self):
        if self == SortingOrder.ASCENDING:
            return Qt.SortOrder.AscendingOrder
        return Qt.SortOrder.DescendingOrder

    def __xor__(self, other):
        return self.value ^ other.value

    def flip(self):
        return SortingOrder(self ^ SortingOrder.DESCENDING)


class MyLazyTableWidget(QTableWidget):
    REMOVE_THREAD_AFTER_MS = 500
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self, parent, default_items_load=30):
        super().__init__(parent)
        self._exhausted = object()
        self._threads = set()
        self._headers = None
        self._last_sorting_direction = None
        self.verticalScrollBar().valueChanged.connect(self.after_scroll)
        self.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self.horizontalHeader().sectionClicked.connect(self.on_header_clicked)
        self.cellEntered.connect(self.set_row_highlight)

        # self._qobject = QObject()
        # self._qobject.eventFilter = self._my_event_filter
        # self.installEventFilter(self._qobject)
        # self.horizontalHeader().installEventFilter(self._qobject)
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## GETTING THIS AFTER CLOSING THE APP:
        ## Process finished with exit code -1073741819 (0xC0000005)

        self._prev_scrolling_value = 0
        self._default_items_load = default_items_load
        self._rows: list | None = None
        self._rows_iter = None
        self._adding_items = False
        self._selection_changed_callback = None
        self._item_double_clicked_callback = None
        self._previous_row = -1

    def set_headers(self, headers):
        """
        MUST BE CALLED AT THE BEGINNING
        """
        self._headers = headers
        self._last_sorting_direction = [SortingOrder.INITIAL for _ in range(len(self._headers))]

    def add_thread(self, thread):
        # LazyTableWidget.RUNNING_THREADS_MUTEX.lock()
        self._threads.add(thread)
        # LazyTableWidget.RUNNING_THREADS_MUTEX.unlock()

    def remove_thread(self, thread):
        # LazyTableWidget.RUNNING_THREADS_MUTEX.lock()
        self._threads.remove(thread)
        # LazyTableWidget.RUNNING_THREADS_MUTEX.unlock()

    def set_row_highlight(self, row, _):
        """
        TODO: Try setting this stylesheet for each cell in the given row
        QTableWidget::item:hover {
	        background-color: rgba(59,59,59,150);
        }
        """
        for column in range(self.columnCount()):
            if self._previous_row > -1:
                color = QColor()
                color.setAlpha(0)
                self.item(self._previous_row, column).setBackground(color)
            if current_row := self.item(row, column):
                color = QColor(0x35434f)
                # color = QColor(0x536778)
                color.setAlpha(150)
                current_row.setBackground(color)
        self._previous_row = row

    # SELECTION CALLBACKS [BEGIN]
    def set_item_selection_changed_callback(self, callback: Callable[[list], None]):
        self._selection_changed_callback = callback
        if self._selection_changed_callback:
            self.itemSelectionChanged.connect(self._selection_changed)

    def disconnect_item_selection_changed_callback(self):
        self.itemSelectionChanged.disconnect(self._selection_changed)

    def _selection_changed(self):
        if self._selection_changed_callback:
            self._selection_changed_callback(self.get_selected_items())

    def get_selected_items(self):
        results = {}
        for item in self.selectedItems():
            row_id = item.row()
            results[row_id] = [self.item(row_id, col) for col in range(self.columnCount())]
        return list(results.values())

    # SELECTION CALLBACKS [END]

    # DOUBLE CLICK CALLBACKS [BEGIN]
    def set_item_double_clicked_callback(self, callback: Callable[[Any], None]):
        self._item_double_clicked_callback = callback
        if self._item_double_clicked_callback:
            self.itemDoubleClicked.connect(self._item_double_clicked)

    def disconnect_item_double_clicked_callback(self):
        self.itemDoubleClicked.disconnect(self._item_double_clicked)

    def _item_double_clicked(self, item: QTableWidgetItem):
        if self._item_double_clicked_callback:
            self._item_double_clicked_callback(item)

    # DOUBLE CLICK CALLBACKS [END]

    def on_header_clicked(self, col_idx:int|TableHeaders):
        self.sort(col_idx)

    def sort(self, col_idx:int|TableHeaders):
        if isinstance(col_idx, TableHeaders):
            col_idx = col_idx.value

        reverse = self._last_sorting_direction[col_idx] == SortingOrder.ASCENDING
        self._rows.sort(key=lambda x:x[col_idx], reverse=reverse)
        self._rows_iter = iter(self._rows)
        # self.horizontalHeader().setSortIndicator(col_idx,
        #                                                       self._last_sorting_direction[col_idx].convert_to_qt_sorting_type())
        self._last_sorting_direction[col_idx] = self._last_sorting_direction[col_idx].flip()
        for idx in range(len(self._last_sorting_direction)):
            if idx != col_idx:
                self._last_sorting_direction[idx] = SortingOrder.DESCENDING
        self.clear()
        self.load_more_items()
        # sort again by qt just to show the arrow symbol
        self.sortByColumn(col_idx, self._last_sorting_direction[col_idx].convert_to_qt_sorting_type())

    def before_scroll(self):
        scrollbar = self.verticalScrollBar()
        self._prev_scrolling_value = scrollbar.value()

    def after_scroll(self):
        if self._adding_items or (
                (scrollbar := self.verticalScrollBar()).value() < self._prev_scrolling_value):
            return "break"
        current_val = scrollbar.value()
        if scrollbar.value() > 0.85 * scrollbar.maximum():  # At the bottom
            self.load_more_items(self._default_items_load)
            scrollbar.setValue(min(scrollbar.maximum(), current_val))

    def save_values(self, rows):
        self._rows = rows
        self._rows_iter = iter(self._rows)
        self.reset_sorting_order()

    def load_more_items(self, how_many: int = None, prevent_scrolling=False):
        def _done():
            if prevent_scrolling:
                scrollbar.setValue(current_scroll_value)
            self.resizeColumnsToContents()
            self.resizeRowsToContents()
            # self.resizeRowToContents(self.rowCount() - 1)
            self._adding_items = False
            return

        self._adding_items = True
        if self.rowCount() == 0:
            self.setColumnCount(len(self._headers))
            self.setHorizontalHeaderLabels(self.get_translated_headers())
        scrollbar = self.verticalScrollBar()
        current_scroll_value = scrollbar.value()

        if how_many is None:
            how_many = self._default_items_load
        for _ in range(how_many):
            if (row := next(self._rows_iter, self._exhausted)) is self._exhausted:
                return _done()
            self.append_row(row)
        return _done()

    @abstractmethod
    def append_row(self, row: CustomTableRow):
        """
        Optionally override this method
        """
        data = row.data
        self.insertRow(self.rowCount())
        for j in range(len(data)):
            item = CustomTableWidgetItem(str(data[j]))
            # set metadata in last col
            is_last_col = j == len(data) - 1
            if is_last_col:
                item.setData(Qt.ItemDataRole.UserRole, row.metadata)

            self.setItem(self.rowCount()-1, j, item)

    def clear(self):
        self._previous_row = -1
        # self.clearContents()
        self.setRowCount(0)
        self.setColumnCount(0)
        # QTimer.singleShot(0, self.clear)
        self.verticalScrollBar().setValue(0)

    def reset_sorting_order(self):
        self._last_sorting_direction = [SortingOrder.INITIAL for _ in range(len(self._headers))]

    def get_translated_headers(self):
        return [translate_text(header) for header in self._headers]

    def retranslate_ui(self):
        self.setHorizontalHeaderLabels(self.get_translated_headers())
        # self.resizeColumnsToContents()
        # self.resizeRowsToContents()
