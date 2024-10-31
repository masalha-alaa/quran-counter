from PySide6.QtWidgets import QWidget


class TabWrapper(QWidget):
    def __init__(self, parent, latest_search_word='', latest_radio_button=''):
        super().__init__(parent)
        self.parent = parent
        self.latest_search_word = latest_search_word
        self.latest_radio_button = latest_radio_button

    def update_config(self, word, radio):
        self.latest_search_word = word
        self.latest_radio_button = radio

    def config_changed(self, word, radio) -> bool:
        return self.latest_search_word != word or self.latest_radio_button != radio
