from PySide6.QtGui import QValidator
from PySide6.QtCore import QRegularExpression


class ArabicOnlyValidator(QValidator):
    def validate(self, input, pos):
        # Define the regular expression for Arabic letters
        arabic_letters = QRegularExpression('^ ?[\u0600-\u06FF]+( [\u0600-\u06FF]+)*$')

        # Check if the input matches the pattern
        if arabic_letters.match(input).hasMatch():
            return QValidator.State.Acceptable, input, pos
        elif input == "" or (input.endswith(" ") and not input.endswith("  ")):
            return QValidator.State.Intermediate, input, pos
        else:
            return QValidator.State.Invalid, input, pos
