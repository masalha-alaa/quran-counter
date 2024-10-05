from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QShowEvent
from PySide6.QtCore import Signal, Slot, QThread
from gui.disambiguation_dialog import Ui_DidsambiguationDialog
from gui.spinning_loader import SpinningLoader
from ask_gpt_thread import AskGptThread


class MyDidsambiguationDialog(QDialog, Ui_DidsambiguationDialog):
    response_signal = Signal(str)

    def __init__(self, disambiguator):
        super(MyDidsambiguationDialog, self).__init__()
        self.setupUi(self)
        self.spinner = SpinningLoader()
        self.spinnerParentLayout.addWidget(self.spinner)
        self._setup_events()
        self.disambiguator = disambiguator
        self.worker = AskGptThread(disambiguator)  # GPT claims i can't reuse a thread, but it's working...
        self._word = None
        self._verses = None

    def set_data(self, word, verses):
        self._word = word
        self._verses = verses
        self.instructionsWordLabel.setText(f"'{self._word}'")

    def _setup_events(self):
        self.cancelButton.clicked.connect(self.on_rejected)
        self.okButton.clicked.connect(self.on_accepted)

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        if self._word.strip():
            self.ask_gpt_for_meanings(self._word)

    @Slot()
    def on_rejected(self):
        self.spinner.stop()
        self.reject()  # Close the dialog and return # QDialog.DialogCode.Rejected

    @Slot()
    def on_accepted(self):
        if self._word.strip() and self._verses.strip() and (selected := self.resultsListWidget.currentItem()):
            # self.ask_gpt_for_relevant_verses(self._word, self._verses, selected.text())
            self.response_signal.emit(selected.text())
        self.accept()  # Close the dialog and return # QDialog.DialogCode.Accepted

    # [COMMANDS BEGIN]
    def ask_gpt_for_meanings(self, word):
        self.resultsListWidget.clear()
        self.spinner.start()
        self.worker.set_command_get_meanings(word)
        self.worker.meanings_result_ready.connect(self.on_ask_gpt_for_meanings_completed)  # Connect signal to slot
        self.worker.start()

    # def ask_gpt_for_relevant_verses(self, word, verses, meaning):
    #     @lru_cache(maxsize=128)
    #     def _ask_gpt_for_relevant_verses(word, verses_ref, meaning):
    #         """
    #         :param verses_ref: for caching purposes
    #         """
    #         self.worker.set_command_get_relevant_verses(word,
    #                                                     verses,
    #                                                     meaning)
    #         self.worker.relevant_verses_result_ready.connect(self.on_ask_gpt_for_relevant_verses_completed)
    #         self.worker.start()
    #     return _ask_gpt_for_relevant_verses(word, re.findall(r"^\d{,2}:\d{,3}", verses, flags=re.M), meaning)
    # [COMMANDS END]

    # [CALLBACKS BEGIN]
    @Slot(dict, QThread)
    def on_ask_gpt_for_meanings_completed(self, results, caller_thread: AskGptThread):
        # print("on_ask_gpt_for_meanings_completed")
        caller_thread.meanings_result_ready.disconnect(self.on_ask_gpt_for_meanings_completed)
        self.spinner.stop()
        self.okButton.setEnabled(True)
        # TODO: Idk how but need to destroy movie according to this:
        #       https://stackoverflow.com/questions/26958644/qt-loading-indicator-widget#comment78882452_26958738
        self.resultsListWidget.addItems(results.values())

    # @Slot(list)
    # def on_ask_gpt_for_relevant_verses_completed(self, results):
    #     self.response_signal.emit(results)
    #     self.accept()  # Close the dialog and return # QDialog.DialogCode.Accepted
    # [CALLBACKS END]
