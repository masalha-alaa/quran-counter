from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStyledItemDelegate, QStyle
from PySide6.QtGui import QTextOption


class LeftToRightDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        painter.save()

        # Draw default styling for the cell
        # super().paint(painter, option, index)

        # option.displayAlignment = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        text_option = QTextOption()
        text_option.setTextDirection(Qt.LayoutDirection.LeftToRight)

        painter.drawText(option.rect, option.displayAlignment, index.data())
        painter.restore()
