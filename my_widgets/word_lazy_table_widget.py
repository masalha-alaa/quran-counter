from my_widgets.lazy_table_widget import MyLazyTableWidget
from my_widgets.lazy_table_widget import CustomTableRow
from tabs_management.table_headers import WordTableHeaders
from my_widgets.lazy_table_widget import TableDataType, CustomTableWidgetItem
from PySide6.QtCore import Qt


class WordLazyTableWidget(MyLazyTableWidget):
    def __init__(self, parent, default_items_load=30):
        super().__init__(parent, default_items_load)
        headers = [None] * len(WordTableHeaders)
        headers[WordTableHeaders.WORD_TEXT_HEADER.value] = "الكلمة"
        headers[WordTableHeaders.RESULTS_HEADER.value] = "عدد النتائج"
        self.set_headers(headers)

    def append_row(self, row: CustomTableRow):
        data = row.data
        self.insertRow(self.rowCount())
        for j in range(len(data)):
            if WordTableHeaders(j) == WordTableHeaders.RESULTS_HEADER:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.INT)
            else:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.STRING)

            is_metadata_col = j == WordTableHeaders.METADATA_POSITION.value
            if is_metadata_col:
                item.setData(Qt.ItemDataRole.UserRole, row.metadata)

            self.setItem(self.rowCount()-1, j, item)
