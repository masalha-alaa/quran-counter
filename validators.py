from PySide6.QtGui import QValidator
from PySide6.QtCore import QRegularExpression
from arabic_reformer import get_arabic_abc


class ArabicOnlyValidator(QValidator):
    arabic_abc = ''.join(get_arabic_abc())

    def validate(self, input, pos):
        # Define the regular expression for Arabic letters
        # arabic_letters = QRegularExpression('^ ?[\u0600-\u06FF]+( [\u0600-\u06FF]+)*$')
        arabic_letters = QRegularExpression(f'^ ?[{self.arabic_abc}]+( [{self.arabic_abc}]+)*$')

        # Check if the input matches the pattern
        if arabic_letters.match(input).hasMatch():
            return QValidator.State.Acceptable, input, pos
        elif input == "" or (input.endswith(" ") and not input.endswith("  ")):
            return QValidator.State.Intermediate, input, pos
        else:
            return QValidator.State.Invalid, input, pos
