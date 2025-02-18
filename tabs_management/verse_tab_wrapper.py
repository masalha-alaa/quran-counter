import warnings
from chat_gpt.disambiguator import Disambiguator
from gui.disambiguation_dialog.my_disambiguation_dialog import MyDidsambiguationDialog
from gui.openai_key_setup_dialog.my_openai_key_setup_dialog import MyOpenAiKeySetupDialog
from gui.waiting_dialog.my_waiting_dialog import MyWaitingDialog
from chat_gpt.ask_gpt_thread import AskGptThread
from my_widgets.tab_wrapper import TabWrapper
from my_utils.shared_data import SharedData
from my_utils.utils import get_radio_threshold
from PySide6.QtCore import Slot
from my_utils.utils import resource_path, load_translation
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QThread, QObject, SIGNAL


class VerseTabWrapper(TabWrapper):
    def __init__(self, parent, latest_search_word='', latest_radio_button=''):
        super().__init__(parent, latest_search_word, latest_radio_button)
        SharedData.found_verses.set_colorize(SharedData.ui.colorizeCheckbox.isChecked())

        self.activate_gpt_dialog = MyOpenAiKeySetupDialog(SharedData.app_language)
        # self._disambiguator = Disambiguator("open_ai_key.txt")  # TODO: REMOVE
        self._disambiguator = Disambiguator()
        self.disambiguation_dialog = MyDidsambiguationDialog(self._disambiguator, SharedData.app_language)

        self.ask_gpt_thread = AskGptThread(self._disambiguator)
        self.waiting_dialog = MyWaitingDialog(SharedData.app_language)
        self._setup_events()

    def init(self):
        pass

    def clear(self):
        # SharedData.found_verses.clear()  # it's done inside
        SharedData.found_verses.save_values_and_refresh([], [])

    def _setup_events(self):
        self.connect_colorize()
        SharedData.ui.filterButton.clicked.connect(self._filter_button_clicked)
        SharedData.ui.clearFilterButton.clicked.connect(self._clear_filter_button_clicked)

    def populate_results(self, number_of_matches=None):
        current_radio_threshold = get_radio_threshold(SharedData.ui.searchOptionsButtonGroup.checkedButton())
        self.update_config(SharedData.search_word,
                           SharedData.ui.searchOptionsButtonGroup.checkedId(),
                           current_radio_threshold)
        SharedData.found_verses.save_values_and_refresh(SharedData.all_matches, range(len(SharedData.all_matches)))
        SharedData.ui.filterButton.setEnabled((number_of_matches > 0) and len(SharedData.search_word.split()) == 1)

    def _colorize_toggled(self, state):
        SharedData.found_verses.reset_iter_and_refresh(SharedData.all_matches, state)

    def switch_colorize_state_without_firing(self, checked, enabled):
        was_connected = self.disconnect_colorize()
        if checked is not None:
            SharedData.ui.colorizeCheckbox.setChecked(checked)
        if enabled is not None:
            SharedData.ui.colorizeCheckbox.setEnabled(enabled)
        if was_connected:
            self.connect_colorize()

    def connect_colorize(self):
        SharedData.ui.colorizeCheckbox.stateChanged.connect(self._colorize_toggled)

    def disconnect_colorize(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error", RuntimeWarning)
            try:
                SharedData.ui.colorizeCheckbox.stateChanged.disconnect(self._colorize_toggled)
            except SystemError:
                return False
        return True


    @Slot()
    def _clear_filter_button_clicked(self):
        self.filter_text_browser(range(len(SharedData.all_matches)))
        SharedData.ui.clearFilterButton.setEnabled(False)

    @Slot()
    def _filter_button_clicked(self):
        if self._disambiguator.is_activated():
            self.show_disambiguation_dialog()
        else:
            self.show_gpt_activation_dialog()

    def show_disambiguation_dialog(self):
        if load_translation(SharedData.translator, resource_path(f"translations/disambig_dlg_{SharedData.app_language.value}.qm")):
            self.disambiguation_dialog.set_language(SharedData.app_language)

        self.disambiguation_dialog.set_data(SharedData.search_word)
        self.disambiguation_dialog.response_signal.connect(self._handle_disambiguation_dialog_response)
        if self.disambiguation_dialog.exec() == QDialog.DialogCode.Accepted:
            pass
        else:
            pass

    def show_gpt_activation_dialog(self, show_disambiguation_dialog=True):
        if load_translation(SharedData.translator, resource_path(f"translations/openai_key_setup_dialog_{SharedData.app_language.value}.qm")):
            self.activate_gpt_dialog.set_language(SharedData.app_language)
        if self.activate_gpt_dialog.exec() == QDialog.DialogCode.Accepted:
            self._disambiguator.set_activated(True)
            if show_disambiguation_dialog:
                self.show_disambiguation_dialog()

    @Slot(str)
    def _handle_disambiguation_dialog_response(self, selected_meaning):
        # print("_handle_disambiguation_dialog_response")
        self.disambiguation_dialog.response_signal.disconnect(self._handle_disambiguation_dialog_response)
        if selected_meaning.strip():
            if load_translation(SharedData.translator, resource_path(f"translations/waiting_dlg_{SharedData.app_language.value}.qm")):
                self.waiting_dialog.set_language(SharedData.app_language)
            self.waiting_dialog.open()
            self.ask_gpt_for_relevant_verses(SharedData.search_word, SharedData.all_matches, selected_meaning)

    def ask_gpt_for_relevant_verses(self, word, verses, meaning):
        self.ask_gpt_thread.set_command_get_relevant_verses(word,
                                                verses,
                                                meaning)
        self.ask_gpt_thread.relevant_verses_result_ready.connect(self.on_ask_gpt_for_relevant_verses_completed)
        self.ask_gpt_thread.start()

    @Slot(list, QThread)
    def on_ask_gpt_for_relevant_verses_completed(self, results, caller_thread: AskGptThread):
        # print("FINAL RESULTS:")
        # print(results)
        # TODO: One time GPT returned the verse refs as they appear in the Holy Quran (x:y, x:y, ...)
        #       Need to put an eye on this
        caller_thread.relevant_verses_result_ready.disconnect(self.on_ask_gpt_for_relevant_verses_completed)
        self.waiting_dialog.reject()
        self.filter_text_browser(results)
        SharedData.ui.clearFilterButton.setEnabled(True)

    def filter_text_browser(self, indices: list | range):
        matches_num, matched_verses_num, surah_count = SharedData.found_verses.save_values_and_refresh(SharedData.all_matches, indices)
