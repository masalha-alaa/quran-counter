from my_utils.utils import translate_text
from my_widgets.lazy_table_widget import MyLazyTableWidget
from my_widgets.lazy_table_widget import CustomTableRow
from tabs_management.table_headers import WordTableHeaders
from my_widgets.lazy_table_widget import TableDataType, CustomTableWidgetItem
from PySide6.QtCore import Qt
from my_delegates.left_to_right_delegate import LeftToRightDelegate


class WordLazyTableWidget(MyLazyTableWidget):
    def __init__(self, parent, default_items_load=30):
        super().__init__(parent, default_items_load)
        headers = [None] * len(WordTableHeaders)
        headers[WordTableHeaders.WORD_TEXT_HEADER.value] = "الكلمة"
        headers[WordTableHeaders.ENGLISH_TRANSLATION.value] = "ترجمة"
        headers[WordTableHeaders.ENGLISH_TRANSLITERATION.value] = "حَورَفَة"
        headers[WordTableHeaders.RESULTS_HEADER.value] = "عدد النتائج"
        tooltips = [None] * len(WordTableHeaders)
        tooltips[WordTableHeaders.ENGLISH_TRANSLATION.value] = "Showing one meaning, there could be more"
        self.set_headers(headers, tooltips)
        # ltrDelegate = LeftToRightDelegate()
        # self.setItemDelegateForColumn(WordTableHeaders.ENGLISH_TRANSLATION.value, ltrDelegate)
        # self.setItemDelegateForColumn(WordTableHeaders.ENGLISH_TRANSLITERATION.value, ltrDelegate)

    def append_row(self, row: CustomTableRow):
        data = row.data
        self.insertRow(self.rowCount())
        for j in range(len(data)):
            if j == WordTableHeaders.RESULTS_HEADER.value:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.INT)
            elif j in [WordTableHeaders.ENGLISH_TRANSLATION.value, WordTableHeaders.ENGLISH_TRANSLITERATION.value]:
                item = CustomTableWidgetItem(self.LRM_CHAR + str(data[j]), TableDataType.STRING)
            else:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.STRING)


            is_metadata_col = j == WordTableHeaders.METADATA_POSITION.value
            if is_metadata_col:
                item.setData(Qt.ItemDataRole.UserRole, row.metadata)

            self.setItem(self.rowCount()-1, j, item)
