from PySide6.QtWidgets import QRadioButton


class RadioButtonWithThreshold(QRadioButton):
    def __init__(self, parent=None, threshold=None):
        super(RadioButtonWithThreshold, self).__init__(parent)
        self.threshold = threshold
