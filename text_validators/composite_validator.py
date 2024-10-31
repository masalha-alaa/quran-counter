from PySide6.QtGui import QValidator
from text_validators.arabic_only_validator import ArabicOnlyValidator
from text_validators.max_words_validator import MaxWordsValidator


class CompositeValidator(QValidator):
    def __init__(self, max_words=None):
        super().__init__()
        self._arabic_validator = ArabicOnlyValidator()
        self._max_words_validator = MaxWordsValidator(max_words=max_words)

    def set_max_words(self, value):
        self._max_words_validator.max_words = value

    def validate(self, input, pos):
        arabic_validator_result, _, _ = self._arabic_validator.validate(input, pos)
        max_words_validator_result, _, _ = self._max_words_validator.validate(input, pos)
        if arabic_validator_result == QValidator.State.Acceptable and max_words_validator_result == QValidator.State.Invalid:
            combined_result = QValidator.State.Invalid
        else:
            combined_result = arabic_validator_result
        return combined_result, input, pos
