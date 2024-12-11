from PySide6.QtWidgets import QDialog, QLabel
from PySide6.QtGui import QShowEvent, QPixmap
from PySide6.QtCore import Signal, Slot, QTimer
from gui.openai_key_setup_dialog.openai_key_setup_dialog import Ui_OpenAiKeySetupDialog
from my_widgets.spinning_loader import SpinningLoader
from my_utils.utils import AppLang, resource_path
from text_validators.openai_key_validator import OpenAiKeyValidator
from chat_gpt.activate_gpt_thread import ActivateGptThread


class MyOpenAiKeySetupDialog(QDialog, Ui_OpenAiKeySetupDialog):
    response_signal = Signal(str)

    def __init__(self, language: None | AppLang):
        super(MyOpenAiKeySetupDialog, self).__init__()
        self.setupUi(self)
        self.enterKeyLineEdit.setValidator(OpenAiKeyValidator())
        self._current_lang = None
        self._apply_language(language)
        self.activate_gpt_thread = ActivateGptThread()

        self.spinner = SpinningLoader(10)
        self.spinner.hide()
        self.failure_icon = QLabel()
        self.failure_icon.setPixmap(QPixmap(resource_path("gui/resources/failure-x-icon.png")).scaled(15, 16))
        self.failure_icon.hide()
        self.success_icon = QLabel()
        self.success_icon.setPixmap(QPixmap(resource_path("gui/resources/success-v-icon.png")).scaled(15, 16))
        self.success_icon.hide()
        self.statusParentLayout.addWidget(self.success_icon)
        self.statusParentLayout.addWidget(self.failure_icon)
        self.statusParentLayout.addWidget(self.spinner)

        self._setup_events()
        self.okButton.setEnabled(True)
        self.cancelButton.setEnabled(True)

    def set_language(self, lang):
        self._apply_language(lang)

    def _apply_language(self, lang):
        if lang != self._current_lang:
            self.retranslateUi(self)
            # self.set_font_for_language(lang)
            self._current_lang = lang

    def _setup_events(self):
        self.cancelButton.clicked.connect(self.on_rejected)
        self.okButton.clicked.connect(self.on_accepted)

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.enterKeyLineEdit.setText("")
        self.spinner.hide()
        self.success_icon.hide()
        self.failure_icon.hide()

    @Slot()
    def on_rejected(self):
        self.spinner.stop()
        self.reject()

    @Slot()
    def on_accepted(self):
        self.okButton.setEnabled(False)
        self.cancelButton.setEnabled(False)
        self.spinner.setText("")
        self.spinner.start()

        if key := self.enterKeyLineEdit.text():
            self.activate_gpt_thread.set_key(key)
            self.activate_gpt_thread.activation_result.connect(self.gpt_activation_signal)
            self.activate_gpt_thread.start()
        else:
            self._activation_failure()

    def gpt_activation_signal(self, activated):
        self.spinner.stop()
        self.success_icon.hide()
        self.failure_icon.hide()
        if activated:
            self._activation_success()
        else:
            self._activation_failure()

    def _activation_success(self):
        self.success_icon.show()
        QTimer.singleShot(700, lambda: self.accept())

    def _activation_failure(self):
        self.failure_icon.show()
        self.okButton.setEnabled(True)
        self.cancelButton.setEnabled(True)
