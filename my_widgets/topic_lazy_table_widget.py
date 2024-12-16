from my_utils.utils import translate_text
from my_widgets.lazy_table_widget import MyLazyTableWidget
from my_widgets.lazy_table_widget import CustomTableRow
from tabs_management.table_headers import TopicTableHeaders
from my_widgets.lazy_table_widget import TableDataType, CustomTableWidgetItem
from PySide6.QtCore import Qt


class TopicLazyTableWidget(MyLazyTableWidget):
    def __init__(self, parent, default_items_load=30):
        super().__init__(parent, default_items_load)
        headers = [None] * len(TopicTableHeaders)
        headers[TopicTableHeaders.TOPIC_NAME_HEADER.value] = "الموضوع"
        headers[TopicTableHeaders.SCORE_HEADER.value] = "(%) درجة الصلة"
        headers[TopicTableHeaders.RESULTS_HEADER.value] =  "عدد النتائج"
        self.set_headers(headers)

    def append_row(self, row: CustomTableRow):
        data = row.data
        self.insertRow(self.rowCount())
        for j in range(len(data)):
            if TopicTableHeaders(j) == TopicTableHeaders.SCORE_HEADER:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.FLOAT)
            elif TopicTableHeaders(j) == TopicTableHeaders.RESULTS_HEADER:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.INT)
            elif j == TopicTableHeaders.TOPIC_NAME_HEADER.value:
                item = CustomTableWidgetItem(translate_text(str(data[j])), TableDataType.STRING)
            else:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.STRING)

            is_metadata_col = j == TopicTableHeaders.METADATA_POSITION.value
            if is_metadata_col:
                item.setData(Qt.ItemDataRole.UserRole, row.metadata)

            self.setItem(self.rowCount()-1, j, item)

    def retranslate_ui(self):
        for row in range(self.rowCount()):
            current_item = self.item(row, TopicTableHeaders.TOPIC_NAME_HEADER.value)
            current_item.setText(translate_text(current_item.text()))
        super().retranslate_ui()


