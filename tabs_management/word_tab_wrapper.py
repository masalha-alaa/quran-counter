from datetime import datetime
from algos.related_words import RelatedWords
from my_widgets.tab_wrapper import TabWrapper
from my_utils.utils import resource_path, load_translation, get_radio_threshold
from my_utils.shared_data import SharedData
from gui.detailed_display_dialog.my_word_detailed_display_dialog import MyWordDetailedDisplayDialog
from tabs_management.table_headers import WordTableHeaders
from worker_threads.word_bounds_populator_thread import WordBoundsPopulatorThread
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem
from my_widgets.graph_dialog import GraphDialog
import networkx as nx


class WordTabWrapper(TabWrapper):
    def __init__(self, parent, latest_search_word='', latest_radio_button=''):
        super().__init__(parent, latest_search_word, latest_radio_button)
        self._last_thread_id = -1
        self.detailed_word_display_dialog = MyWordDetailedDisplayDialog(SharedData.app_language)
        self.lazy_word_results_table = SharedData.ui.wordResultsTableWidget
        self.minimum_letters_restriction_lbl_stylesheet = SharedData.ui.minimum_letters_restriction_lbl.styleSheet()
        self._setup_events()

    def init(self):
        self.lazy_word_results_table.set_item_selection_changed_callback(self.word_bounds_results_selection_changed)
        self.lazy_word_results_table.set_item_double_clicked_callback(self.word_bounds_results_item_double_clicked)
        self.lazy_word_results_table.set_path_clicked_callback(self.word_bounds_results_path_clicked)
        self.refreshColumnsVisibility()

    def refreshColumnsVisibility(self):
        self.lazy_word_results_table.set_column_visibility(WordTableHeaders.ENGLISH_TRANSLATION,
                                                           SharedData.ui.wordMeaningCheckbox.isChecked())
        self.lazy_word_results_table.set_column_visibility(WordTableHeaders.ENGLISH_TRANSLITERATION,
                                                           SharedData.ui.wordTransliterationCheckbox.isChecked())
        self.lazy_word_results_table.set_column_visibility(WordTableHeaders.PATH_HEADER,
                                                           SharedData.ui.relatedWordsRadioButton.isChecked())

    def _setup_events(self):
        SharedData.ui.diacriticsCheckbox.stateChanged.connect(self._toggle_diacritics)
        SharedData.ui.wordMeaningCheckbox.stateChanged.connect(self._toggle_meaning_checkbox)
        SharedData.ui.wordTransliterationCheckbox.stateChanged.connect(self._toggle_transliteration_checkbox)

    def clear(self):
        self.lazy_word_results_table.clear()
        self.lazy_word_results_table.save_values([])

    def retranslate_ui(self):
        self.lazy_word_results_table.retranslate_ui()

    def _toggle_diacritics(self, state):
        self.populate_results(SharedData.search_word)

    def _toggle_meaning_checkbox(self, state):
        self.lazy_word_results_table.toggle_column(WordTableHeaders.ENGLISH_TRANSLATION)

    def _toggle_transliteration_checkbox(self, state):
        self.lazy_word_results_table.toggle_column(WordTableHeaders.ENGLISH_TRANSLITERATION)

    def populate_results(self, initial_word=''):
        if len(initial_word.strip()) < 2:
            self.lazy_word_results_table.clear()
            self.lazy_word_results_table.save_values([])
            SharedData.ui.minimum_letters_restriction_lbl.setStyleSheet(f"{self.minimum_letters_restriction_lbl_stylesheet} color: red;")
            return
        SharedData.ui.minimum_letters_restriction_lbl.setStyleSheet(self.minimum_letters_restriction_lbl_stylesheet)

        current_radio_threshold = get_radio_threshold(SharedData.ui.searchOptionsButtonGroup.checkedButton())
        self.update_config(SharedData.search_word,
                           SharedData.ui.searchOptionsButtonGroup.checkedId(),
                           current_radio_threshold)
        thread_id = datetime.now().timestamp()
        word_bounds_populator_thread = WordBoundsPopulatorThread(SharedData.ui.diacriticsCheckbox.isChecked(), thread_id)
        word_bounds_populator_thread.set_data(SharedData.all_matches, SharedData.ui.diacriticsCheckbox.isChecked())
        word_bounds_populator_thread.result_ready.connect(self.on_find_word_bounds_completed)
        self._add_thread(word_bounds_populator_thread)
        word_bounds_populator_thread.start()

    def on_find_word_bounds_completed(self, counts, thread_id, caller_thread: WordBoundsPopulatorThread):
        caller_thread.result_ready.disconnect(self.on_find_word_bounds_completed)
        self._remove_thread(caller_thread)
        # reject older threads?
        if thread_id < self._last_thread_id:
            return

        self._last_thread_id = thread_id
        self.lazy_word_results_table.clear()
        self.lazy_word_results_table.save_values(counts)
        self.lazy_word_results_table.sort(WordTableHeaders.WORD_TEXT_HEADER)
        self.refreshColumnsVisibility()

    def word_bounds_results_selection_changed(self, selected_items: list[list]):
        total = sum(int(row[WordTableHeaders.RESULTS_HEADER.value].text()) for row in selected_items)
        SharedData.ui.wordSum.setText(str(total))

    def word_bounds_results_item_double_clicked(self, item: QTableWidgetItem):
        metadata = SharedData.ui.wordResultsTableWidget.item(item.row(), WordTableHeaders.METADATA_POSITION.value).data(Qt.ItemDataRole.UserRole)
        if load_translation(SharedData.translator, resource_path(f"translations/word_detailed_display_dialog_{SharedData.app_language.value}.qm")):
            self.detailed_word_display_dialog.set_language(SharedData.app_language)
        self.detailed_word_display_dialog.set_data(metadata)
        # self.detailed_word_display_dialog.open()
        self.detailed_word_display_dialog.exec()

    def word_bounds_results_path_clicked(self, path: list):
        g = nx.Graph()
        if len(path) > 1:
            for u,v in zip(path, path[1:]):
                # TODO: according to current language
                """
                from arabic_reshaper import reshape
                from bidi.algorithm import get_display
                
                def fix_arabic(w):
                    return  get_display(reshape(w))
                g.add_edge(RelatedWords.eng_to_arb[u], RelatedWords.eng_to_arb[v])
                """
                g.add_edge(u,v)
        else:
            g.add_node(path[0])
        dialog = GraphDialog(g, self)
        dialog.exec()
