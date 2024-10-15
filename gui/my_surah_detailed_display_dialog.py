from my_data_loader import MyDataLoader
from gui.base_detailed_display_dialog import BaseDetailedDisplayDialog


class MySurahDetailedDisplayDialog(BaseDetailedDisplayDialog):
    _exhausted = object()

    def __init__(self, items_to_load=25):
        super(MySurahDetailedDisplayDialog, self).__init__(items_to_load)

    def _append(self, row_metadata):
        surah_num, verse_num, verse_nums_and_spans = row_metadata
        verse = MyDataLoader.get_verse(int(surah_num), int(verse_num))
        if self.colorizeCheckbox.isChecked():
            verse = self._reform_and_color(verse, verse_nums_and_spans)
        line = f"<p>{surah_num}:{verse_num}: {verse}</p>"
        # line = f"{ref}: {verse}"
        self.textBrowser.append(line)
