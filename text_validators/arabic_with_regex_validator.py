from PySide6.QtGui import QValidator
from PySide6.QtCore import QRegularExpression
from arabic_reformer import get_arabic_abc


class ArabicWithRegexValidator(QValidator):
    SUPPORTED_REGEX_CHARS = r"()?|^$"
    arabic_abc = ''.join(get_arabic_abc())

    def validate(self, input, pos):
        input = input.replace("؟", "?")
        # Define the regular expression for regex
        supported_regex_chars = ArabicWithRegexValidator.SUPPORTED_REGEX_CHARS
        arabic_letters_with_regex = QRegularExpression(f'^ ?[{self.arabic_abc}{supported_regex_chars}]+( [{self.arabic_abc}{supported_regex_chars}]+)*$')

        # Check if the input matches the pattern
        if arabic_letters_with_regex.match(input).hasMatch():
            return QValidator.State.Acceptable, input, pos
        elif input == "" or (input.endswith(" ") and not input.endswith("  ")):
            return QValidator.State.Intermediate, input, pos
        else:
            return QValidator.State.Invalid, input, pos
