from PySide6.QtGui import QValidator
from PySide6.QtCore import QRegularExpression
from arabic_reformer import get_arabic_abc


class MaxWordsValidator(QValidator):
    def __init__(self, max_words=None):
        super().__init__()
        self._max_words = max_words

    @property
    def max_words(self):
        return self._max_words

    @max_words.setter
    def max_words(self, value):
        self._max_words = value

    def validate(self, input, pos):
        if self._max_words is None or len(input.split()) <= self._max_words:
            return QValidator.State.Acceptable, input, pos
        else:
            return QValidator.State.Invalid, input, pos
