from PySide6.QtWidgets import QListWidgetItem
from .custom_row import CustomRow


class CustomListWidgetItem(QListWidgetItem):
    def __init__(self, row: CustomRow, idx):
        super().__init__(f"{idx}. {row.label}")
        self.row = row
