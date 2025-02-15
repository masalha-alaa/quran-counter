from PySide6.QtWidgets import QPushButton


class PushButtonWithMetadata(QPushButton):
    def __init__(self, parent=None, metadata=None):
        super(PushButtonWithMetadata, self).__init__(parent)
        self.metadata = metadata
