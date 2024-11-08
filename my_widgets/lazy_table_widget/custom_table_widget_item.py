from PySide6.QtWidgets import QTableWidgetItem
from .table_data_type import TableDataType


class CustomTableWidgetItem(QTableWidgetItem):
    def __init__(self, text: str, type_: int = QTableWidgetItem.ItemType.Type):
        super().__init__(text, type_)

    def __lt__(self, other):
        if self.type() == TableDataType.INT:
            return int(self.text()) < int(other.text())
        return self.text() < other.text()

