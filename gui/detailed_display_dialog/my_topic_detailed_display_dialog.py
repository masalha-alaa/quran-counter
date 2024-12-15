from my_utils.my_data_loader import MyDataLoader
from my_widgets.base_detailed_display_dialog import BaseDetailedDisplayDialog
from my_utils.utils import AppLang


class MyTopicDetailedDisplayDialog(BaseDetailedDisplayDialog):
    _exhausted = object()

    def __init__(self, language: None | AppLang, items_to_load=25):
        super(MyTopicDetailedDisplayDialog, self).__init__(language, items_to_load)
        self.colorizeCheckbox.setVisible(False)

    def _append(self, row_metadata):
        surah_num, verse_num = row_metadata
        verse = MyDataLoader.get_verse(int(surah_num), int(verse_num))
        line = f"<p>{surah_num}:{verse_num}: {verse}</p>"
        # line = f"{ref}: {verse}"
        self.textBrowser.append(line)
