from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QShowEvent
from PySide6.QtCore import Signal
from gui.waiting_dialog.waiting_dialog import Ui_WaitingDialog
from my_widgets.spinning_loader import SpinningLoader
from my_utils.utils import AppLang


class MyWaitingDialog(QDialog, Ui_WaitingDialog):
    response_signal = Signal(list)

    def __init__(self, language: None | AppLang):
        super(MyWaitingDialog, self).__init__()
        self.setupUi(self)
        self._current_lang = None
        self._apply_language(language)
        self.spinner = SpinningLoader()
        self.verticalLayout.addWidget(self.spinner)

    def set_language(self, lang):
        self._apply_language(lang)

    def _apply_language(self, lang):
        if lang != self._current_lang:
            self.retranslateUi(self)
            # self.set_font_for_language(lang)
            self._current_lang = lang

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.spinner.start()

    def reject(self):
        self.spinner.stop()
        super().reject()
