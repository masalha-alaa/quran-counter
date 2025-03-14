import webbrowser
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QShowEvent, QCloseEvent
from gui.version_update_dialog.version_update_dialog import Ui_VersionUpdateDialog
from my_utils.utils import AppLang, translate_text, DynamicTranslationSrcLang
from worker_threads.version_update_thread import VersionUpdateThread

class MyVersionUpdateDialog(QDialog, Ui_VersionUpdateDialog):

    def __init__(self, language: None | AppLang):
        super(MyVersionUpdateDialog, self).__init__()
        self.setFixedSize(450, 150)
        self.setupUi(self)
        self.downloadButton.setVisible(False)
        self.version_update_thread = None
        self._current_lang = None
        self._apply_language(language)
        self._update_url = ''
        self._setup_events()

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.statusLabel.setText(self.translate("Checking for updates..."))
        self.version_update_thread = VersionUpdateThread()
        self.version_update_thread.check_finished.connect(self.check_done_callback)
        self.version_update_thread.start()

    def closeEvent(self, event):
        self.version_update_thread.terminate()
        event.accept()

    def check_done_callback(self, update_url: str, caller_thread: VersionUpdateThread):
        caller_thread.check_finished.disconnect(self.check_done_callback)
        self._update_url = update_url
        if self._update_url:
            self.statusLabel.setText(self.translate("Update available!"))
            self.downloadButton.setVisible(True)
        else:
            self.statusLabel.setText(self.translate("You already have the latest version!"))

    def set_language(self, lang):
        self._apply_language(lang)

    def _apply_language(self, lang):
        if lang != self._current_lang:
            self.retranslateUi(self)
            # self.set_font_for_language(lang)
            self._current_lang = lang

    def translate(self, text):
        return translate_text(text, DynamicTranslationSrcLang.ENGLISH)

    def _setup_events(self):
        self.downloadButton.clicked.connect(self.download_button_clicked)

    def download_button_clicked(self):
        webbrowser.open(self._update_url)  # Open download link in browser

