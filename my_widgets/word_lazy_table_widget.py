from typing import Callable, Any
from my_widgets.lazy_table_widget import MyLazyTableWidget
from my_widgets.lazy_table_widget import CustomTableRow
from my_widgets.push_button_with_metadata import PushButtonWithMetadata
from tabs_management.table_headers import WordTableHeaders
from my_widgets.lazy_table_widget import TableDataType, CustomTableWidgetItem
from PySide6.QtCore import Qt
from my_delegates.left_to_right_delegate import LeftToRightDelegate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout
from my_utils.utils import resource_path


class WordLazyTableWidget(MyLazyTableWidget):
    def __init__(self, parent, default_items_load=30):
        super().__init__(parent, default_items_load)
        headers = [None] * len(WordTableHeaders)
        headers[WordTableHeaders.WORD_TEXT_HEADER.value] = "الكلمة"
        headers[WordTableHeaders.ENGLISH_TRANSLATION.value] = "ترجمة"
        headers[WordTableHeaders.ENGLISH_TRANSLITERATION.value] = "حَورَفَة"
        headers[WordTableHeaders.RESULTS_HEADER.value] = "عدد النتائج"
        headers[WordTableHeaders.PATH_HEADER.value] = "مسار الصلة"
        tooltips = [None] * len(WordTableHeaders)
        tooltips[WordTableHeaders.ENGLISH_TRANSLATION.value] = "Showing one meaning, there could be more"
        self.set_headers(headers, tooltips)
        resizability = [True] * len(headers)
        resizability[WordTableHeaders.PATH_HEADER.value] = False
        self.set_resizability(resizability)
        ltr_delegate = LeftToRightDelegate()
        self.setItemDelegateForColumn(WordTableHeaders.ENGLISH_TRANSLATION.value, ltr_delegate)
        self.setItemDelegateForColumn(WordTableHeaders.ENGLISH_TRANSLITERATION.value, ltr_delegate)
        self._button_clicked_lambda = lambda path: self._path_button_clicked(path)
        self._path_button_clicked_callback = None

    def append_row(self, row: CustomTableRow):
        data = row.data
        # TODO: Find the root cause for empty paths and fix it there (don't add words with empty paths (in any tab!))
        # if len(data[WordTableHeaders.PATH_HEADER.value]) == 0:
        #     return

        self.insertRow(self.rowCount())
        for j in range(len(data)):
            if j == WordTableHeaders.RESULTS_HEADER.value:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.INT)
            elif j == WordTableHeaders.PATH_HEADER.value:
                if path_exists := (len(data[j]) > 0):
                    button = self.create_path_button(data[j])
                    self.setCellWidget(self.rowCount()-1, j, button)
                item = CustomTableWidgetItem("")
            else:
                item = CustomTableWidgetItem(str(data[j]), TableDataType.STRING)

            is_metadata_col = j == WordTableHeaders.METADATA_POSITION.value
            if is_metadata_col:
                item.setData(Qt.ItemDataRole.UserRole, row.metadata)

            self.setItem(self.rowCount()-1, j, item)

    def create_path_button(self, path):
        icon = QIcon(resource_path("gui/resources/path-icon.png"))
        button = PushButtonWithMetadata(self, path)
        button.setIcon(icon)
        button.setFixedSize(30, 30)
        button.clicked.connect(lambda: self._button_clicked_lambda(path))  # TODO: This works but idk
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.setAlignment(button, Qt.AlignmentFlag.AlignCenter)
        container.setLayout(layout)
        return container

    def set_path_clicked_callback(self, callback: Callable[[Any], None]):
        self._path_button_clicked_callback = callback

    def _path_button_clicked(self, path):
        if self._path_button_clicked_callback:
            self._path_button_clicked_callback(path)
