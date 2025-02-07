import sys
from my_utils.utils import AppLang
from PySide6.QtCore import QTranslator
from gui.main_window.main_screen import Ui_MainWindow
from my_utils.package_details import PackageDetails
from my_utils.utils import resource_path


class SharedDataMeta(type):
    ui:Ui_MainWindow = None

    # search word
    @property
    def search_word(cls):
        return cls.ui.searchWord.text()

    @property
    def found_verses(cls):
        return cls.ui.foundVerses

    # matches number
    @property
    def matches_number(cls):
        if s := cls.ui.matchesNumber.text():
            return int(s)
        return 0

    @matches_number.setter
    def matches_number(cls, match_count):
        cls.ui.matchesNumber.setText(match_count)

    @property
    def matches_number_surahs(cls):
        if s := cls.ui.matchesNumberSurahs.text():
            return int(s)
        return 0

    @matches_number_surahs.setter
    def matches_number_surahs(cls, match_count):
        cls.ui.matchesNumberSurahs.setText(match_count)

    @property
    def matches_number_verses(cls):
        if s := cls.ui.matchesNumberVerses.text():
            return int(s)
        return 0

    @matches_number_verses.setter
    def matches_number_verses(cls, match_count):
        cls.ui.matchesNumberVerses.setText(match_count)

    # full word
    @property
    def full_word_checkbox(cls):
        return cls.ui.fullWordRadioButton.isChecked()

    # start of word
    @property
    def beginning_of_word_checkbox(cls):
        return cls.ui.beginningOfWordRadioButton.isChecked()

    # end of word
    @property
    def ending_of_word_checkbox(cls):
        return cls.ui.endOfWordRadioButton.isChecked()


class SharedData(metaclass=SharedDataMeta):
    # ui = None
    app_language = AppLang.DEFAULT_LANGUAGE
    all_matches = []
    translator = QTranslator()
    ar_to_en_dynamic_translator = QTranslator()
    en_to_ar_dynamic_translator = QTranslator()
    sentence_transformers_pkg_details = PackageDetails("sentence_transformers",
                                                       "sentence-transformers==3.3.0",
                                                       resource_path("") if hasattr(sys, '_MEIPASS') else ".venv",
                                                       None)
    pytorch_gpu_pkg_details = PackageDetails("torch",
                                             "torch==2.5.1+cu121",
                                             resource_path("") if hasattr(sys, '_MEIPASS') else ".venv",
                                             "https://download.pytorch.org/whl/cu121")
    # TODO: Keep for later, might need
    # PYTORCH_CPU = ("torch", "torch==2.5.1")
    # PYTORCH_GPU = ("torch", "--extra-index-url https://download.pytorch.org/whl/cu121\ntorch==2.5.1+cu121")
    # SENTENCE_TRANSFORMERS = ("sentence_transformers", "sentence-transformers==3.3.0")
