from datetime import datetime
from my_widgets.tab_wrapper import TabWrapper
from my_utils.utils import  resource_path, load_translation
from my_utils.shared_data import SharedData
from gui.detailed_display_dialog.my_word_detailed_display_dialog import MyWordDetailedDisplayDialog
from my_widgets.lazy_list_widget import CustomRow
from tabs_management.table_headers import WordTableHeaders
from worker_threads.word_bounds_finder_thread import WordBoundsFinderThread
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem


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

    def _setup_events(self):
        SharedData.ui.diacriticsCheckbox.stateChanged.connect(self._toggle_diacritics)

    def clear(self):
        self.lazy_word_results_table.clear()
        self.lazy_word_results_table.save_values([])

    def retranslate_ui(self):
        self.lazy_word_results_table.retranslate_ui()

    def _toggle_diacritics(self, state):
        self.populate_results(SharedData.search_word)

    def populate_results(self, initial_word=''):
        if len(initial_word.strip()) < 2:
            self.lazy_word_results_table.clear()
            self.lazy_word_results_table.save_values([])
            SharedData.ui.minimum_letters_restriction_lbl.setStyleSheet(f"{self.minimum_letters_restriction_lbl_stylesheet} color: red;")
            return
        SharedData.ui.minimum_letters_restriction_lbl.setStyleSheet(self.minimum_letters_restriction_lbl_stylesheet)

        self.update_config(SharedData.search_word, SharedData.ui.searchOptionsButtonGroup.checkedId())
        thread_id = datetime.now().timestamp()
        word_bounds_finder_thread = WordBoundsFinderThread(SharedData.ui.diacriticsCheckbox.isChecked(), thread_id)
        word_bounds_finder_thread.set_data(SharedData.all_matches, SharedData.ui.diacriticsCheckbox.isChecked())
        word_bounds_finder_thread.result_ready.connect(self.on_find_word_bounds_completed)
        self._add_thread(word_bounds_finder_thread)
        word_bounds_finder_thread.start()

    def on_find_word_bounds_completed(self, counts, thread_id, caller_thread: WordBoundsFinderThread):
        caller_thread.result_ready.disconnect(self.on_find_word_bounds_completed)
        self._remove_thread(caller_thread)
        # reject older threads?
        if thread_id < self._last_thread_id:
            return

        self._last_thread_id = thread_id
        self.lazy_word_results_table.clear()
        self.lazy_word_results_table.save_values(counts)
        self.lazy_word_results_table.sort(WordTableHeaders.WORD_TEXT_HEADER)

    def word_bounds_results_selection_changed(self, selected_items: list[list]):
        total = sum(int(row[WordTableHeaders.RESULTS_HEADER.value].text()) for row in selected_items)
        SharedData.ui.wordSum.setText(str(total))

    def word_bounds_results_item_double_clicked(self, item: QTableWidgetItem):
        metadata = SharedData.ui.wordResultsTableWidget.item(item.row(), WordTableHeaders.METADATA_POSITION.value).data(Qt.ItemDataRole.UserRole)
        if load_translation(SharedData.translator, resource_path(f"translations/word_detailed_display_{SharedData.app_language.value}.qm")):
            self.detailed_word_display_dialog.set_language(SharedData.app_language)
        self.detailed_word_display_dialog.set_data(metadata)
        # self.detailed_word_display_dialog.open()
        self.detailed_word_display_dialog.exec()
