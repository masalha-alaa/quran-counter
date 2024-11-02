from my_utils.utils import AppLang
from PySide6.QtCore import QTranslator


class SharedDataMeta(type):
    ui = None

    # search word
    @property
    def search_word(cls):
        return SharedData.ui.searchWord.text()

    @property
    def found_verses(self):
        return self.ui.foundVerses

    # matches number
    @property
    def matches_number(cls):
        if s := SharedData.ui.matchesNumber.text():
            return int(s)
        return 0

    @matches_number.setter
    def matches_number(cls, match_count):
        SharedData.ui.matchesNumber.setText(match_count)

    @property
    def matches_number_surahs(cls):
        if s := SharedData.ui.matchesNumberSurahs.text():
            return int(s)
        return 0

    @matches_number_surahs.setter
    def matches_number_surahs(cls, match_count):
        SharedData.ui.matchesNumberSurahs.setText(match_count)

    @property
    def matches_number_verses(cls):
        if s := SharedData.ui.matchesNumberVerses.text():
            return int(s)
        return 0

    @matches_number_verses.setter
    def matches_number_verses(cls, match_count):
        SharedData.ui.matchesNumberVerses.setText(match_count)

    # full word
    @property
    def full_word_checkbox(self):
        return self.ui.fullWordRadioButton.isChecked()

    # start of word
    @property
    def beginning_of_word_checkbox(self):
        return self.ui.beginningOfWordRadioButton.isChecked()

    # end of word
    @property
    def ending_of_word_checkbox(self):
        return self.ui.endOfWordRadioButton.isChecked()


class SharedData(metaclass=SharedDataMeta):
    app_language = AppLang.DEFAULT_LANGUAGE
    all_matches = []
    translator = QTranslator()
    dynamic_translator = QTranslator()
