from PySide6.QtWidgets import QTableWidgetItem


class TableDataType:
    STRING = QTableWidgetItem.ItemType.UserType + 0
    INT = QTableWidgetItem.ItemType.UserType + 1
    FLOAT = QTableWidgetItem.ItemType.UserType + 2
