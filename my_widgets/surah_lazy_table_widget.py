from my_widgets.lazy_table_widget import MyLazyTableWidget
from my_widgets.lazy_table_widget import CustomTableRow
from tabs_management.table_headers import SurahTableHeaders
from my_widgets.lazy_table_widget import TableDataType, CustomTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem


class SurahLazyTableWidget(MyLazyTableWidget):
    def __init__(self, parent, default_items_load=30):
        super().__init__(parent, default_items_load)
        headers = [None] * len(SurahTableHeaders)
        headers[SurahTableHeaders.SURAH_NAME_HEADER.value] = "اسم السورة"
        headers[SurahTableHeaders.SURAH_NUM_HEADER.value] = "رقم السورة"
        headers[SurahTableHeaders.RESULTS_HEADER.value] =  "عدد النتائج"
        self.set_headers(headers)

    def append_row(self, row: CustomTableRow):
        data = row.data
        self.insertRow(self.rowCount())
        for j in range(len(data)):
            if SurahTableHeaders(j) == SurahTableHeaders.SURAH_NUM_HEADER:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.INT)
            elif SurahTableHeaders(j) == SurahTableHeaders.RESULTS_HEADER:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.INT)
            else:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.STRING)

            is_metadata_col = j == SurahTableHeaders.METADATA_POSITION.value
            if is_metadata_col:
                item.setData(Qt.ItemDataRole.UserRole, row.metadata)

            self.setItem(self.rowCount()-1, j, item)
