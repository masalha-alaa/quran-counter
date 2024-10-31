from PySide6.QtGui import QValidator
from PySide6.QtCore import QRegularExpression


class OpenAiKeyValidator(QValidator):
    def validate(self, input, pos):
        abc = QRegularExpression("[a-zA-Z0-9_/-]+")

        if abc.match(input).hasMatch():
            return QValidator.State.Acceptable, input, pos
        else:
            return QValidator.State.Invalid, input, pos
