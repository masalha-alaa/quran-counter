from enum import Enum
from tabs.verse_tab_wrapper import VerseTabWrapper
from tabs.surah_tab_wrapper import SurahTabWrapper
from my_utils.shared_data import SharedData
from PySide6.QtCore import QTranslator

from tabs.word_tab_wrapper import WordTabWrapper


class TabIndex(Enum):
    VERSES = 0
    SURAHS = 1
    WORDS = 2


class TabsManager:
    def __init__(self):
        self._translator = QTranslator()

        self.verse_tab_wrapper = VerseTabWrapper(SharedData.ui.ayatTab, latest_radio_button=SharedData.ui.searchOptionsButtonGroup.checkedId())
        self.surah_tab_wrapper = SurahTabWrapper(SharedData.ui.surahTab, latest_radio_button=SharedData.ui.searchOptionsButtonGroup.checkedId())
        self.word_tab_wrapper = WordTabWrapper(SharedData.ui.wordsTab, latest_radio_button=SharedData.ui.searchOptionsButtonGroup.checkedId())

        self.verse_tab_wrapper.init()
        self.surah_tab_wrapper.init()
        self.word_tab_wrapper.init()
        SharedData.ui.tabWidget.setCurrentIndex(0)

        self._setup_events()

    def _setup_events(self):
        SharedData.ui.tabWidget.currentChanged.connect(self._tab_changed)

    def refresh_tabs_config(self):
        self.verse_tab_wrapper.update_config(SharedData.search_word, SharedData.ui.searchOptionsButtonGroup.checkedId())
        self.surah_tab_wrapper.update_config(SharedData.search_word, SharedData.ui.searchOptionsButtonGroup.checkedId())
        self.word_tab_wrapper.update_config(SharedData.search_word, SharedData.ui.searchOptionsButtonGroup.checkedId())

    def clear_tabs_results(self):
        self.verse_tab_wrapper.clear()
        self.surah_tab_wrapper.clear()
        self.word_tab_wrapper.clear()

    def on_txt_found_complete(self, initial_word, number_of_matches):
        match SharedData.ui.tabWidget.currentIndex():
            case TabIndex.VERSES.value:
                self.verse_tab_wrapper.populate_results(number_of_matches)
            case TabIndex.SURAHS.value:
                self.surah_tab_wrapper.populate_results()
            case TabIndex.WORDS.value:
                self.word_tab_wrapper.populate_results(initial_word)

    def _tab_changed(self, tab_index):
        current_word, current_radio = SharedData.search_word, SharedData.ui.searchOptionsButtonGroup.checkedId()
        match tab_index:
            case TabIndex.VERSES.value:
                if self.verse_tab_wrapper.config_changed(current_word, current_radio):
                    self.verse_tab_wrapper.populate_results(SharedData.matches_number)
            case TabIndex.SURAHS.value:
                if self.surah_tab_wrapper.config_changed(current_word, current_radio):
                    self.surah_tab_wrapper.populate_results()
            case TabIndex.WORDS.value:
                if self.word_tab_wrapper.config_changed(current_word, current_radio):
                    self.word_tab_wrapper.populate_results(SharedData.search_word)

    # def filter_text_browser(self, indices: list | range):
    #     # self.clear_results()
    #     matches_num, matched_verses_num, surah_count = SharedData.found_verses.save_values_and_refresh(SharedData.all_matches, indices)
    #     # self.matches_number = str(matches_num)
    #     # self.matches_number_surahs = str(surah_count)
    #     # self.matches_number_verses = str(matched_verses_num)
