from PySide6.QtWidgets import QTableWidgetItem
from .table_data_type import TableDataType
from PySide6.QtCore import Qt


class CustomTableWidgetItem(QTableWidgetItem):
    def __init__(self, text: str, type_: int = QTableWidgetItem.ItemType.Type):
        super().__init__(text, type_)

    def __lt__(self, other):
        # UNUSED???
        if self.type() == TableDataType.INT:
            return int(self.text()) < int(other.text())
        if self.type() == TableDataType.FLOAT:
            return float(self.text()) < float(other.text())
        if self.type() == TableDataType.BOOL:
            return bool(self.data(Qt.ItemDataRole.DisplayRole)) < bool(other.data(Qt.ItemDataRole.DisplayRole))
        return self.text() < other.text()

    def __str__(self):
        return str(self.text())

