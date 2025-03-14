from my_utils.my_data_loader import MyDataLoader
from my_widgets.base_detailed_display_dialog import BaseDetailedDisplayDialog
from my_utils.utils import AppLang


class MySurahDetailedDisplayDialog(BaseDetailedDisplayDialog):
    _exhausted = object()

    def __init__(self, language: None | AppLang, items_to_load=25):
        super(MySurahDetailedDisplayDialog, self).__init__(language, items_to_load)

    def _append(self, row_metadata):
        surah_num, verse_num, verse_nums_and_spans = row_metadata
        verse = MyDataLoader.get_verse(int(surah_num), int(verse_num))
        if self.colorizeCheckbox.isChecked():
            verse = self._reform_and_color(verse, verse_nums_and_spans)
        surah_name = MyDataLoader.get_surah_name(surah_num)
        line = f"<p><b>{surah_name} {surah_num}:{verse_num}</b>: {verse}</p>"
        # line = f"{ref}: {verse}"
        self.textBrowser.append(line)
