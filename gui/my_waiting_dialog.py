from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QShowEvent
from PySide6.QtCore import Signal
from gui.waiting_dialog import Ui_WaitingDialog
from gui.spinning_loader import SpinningLoader


class MyWaitingDialog(QDialog, Ui_WaitingDialog):
    response_signal = Signal(list)

    def __init__(self):
        super(MyWaitingDialog, self).__init__()
        self.setupUi(self)
        self.spinner = SpinningLoader()
        self.verticalLayout.addWidget(self.spinner)

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.spinner.start()

    def reject(self):
        self.spinner.stop()
        super().reject()
