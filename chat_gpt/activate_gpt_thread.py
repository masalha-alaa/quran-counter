import os
from PySide6.QtCore import Signal, QThread
import openai


class ActivateGptThread(QThread):
    activation_result = Signal(str, bool, QThread)

    def __init__(self):
        super().__init__()

    def set_key(self, openai_key):
        if os.path.exists(openai_key):
            key = open(openai_key, mode='r').read()
        else:
            key = openai_key
        openai.api_key = key

    def run(self):
        print("Activating gpt...")
        if openai.api_key:
            try:
                openai.models.list()
                self.activation_result.emit(openai.api_key, True, self)
                print("Activation completed successfully")

            except (openai.AuthenticationError, openai.APIConnectionError):
                self.activation_result.emit(openai.api_key, False, self)
                openai.api_key = None
                print("Activation error")
        else:
            self.activation_result.emit('', False, self)
            print("Activation error")
