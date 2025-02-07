from my_utils.my_data_loader import MyDataLoader
from my_widgets.base_detailed_display_dialog import BaseDetailedDisplayDialog
from my_utils.utils import AppLang


class MyWordDetailedDisplayDialog(BaseDetailedDisplayDialog):
    _exhausted = object()

    def __init__(self, language: None | AppLang, items_to_load=25):
        super(MyWordDetailedDisplayDialog, self).__init__(language, items_to_load)

    def _append(self, row_metadata):
        surah_num, verse_num = row_metadata[0], row_metadata[1]
        verse = MyDataLoader.get_verse(int(surah_num), int(verse_num))
        if self.colorizeCheckbox.isChecked():
            # row_metadata = [2,         80,        10,                  93,         100,      1,                 124,        131,      1,                 167, 174, 1]
            #                [surah_num, verse_num, word_id_first_match, word_start, word_end, len(word.split()), word_start, word_end, len(word.split()), ...        ]
            # range starts from idx 3 (word_start), we collect idx & idx + 1 (word_start, word_end), jump 3 items to get to the next word_start...
            # see word_bounds_populator_thread.py
            verse = self._reform_and_color(verse, [(row_metadata[idx], row_metadata[idx + 1]) for idx in
                                                   range(3, len(row_metadata), 3)])
        line = f"<p>{surah_num}:{verse_num}: {verse}</p>"
        # line = f"{ref}: {verse}"
        self.textBrowser.append(line)
