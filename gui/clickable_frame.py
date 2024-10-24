from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class ClickableFrame(QFrame):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShadow(QFrame.Shadow.Raised)

    def mousePressEvent(self, event):
        self.setFrameShadow(QFrame.Shadow.Sunken)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.clicked.emit()
        super().mouseReleaseEvent(event)
