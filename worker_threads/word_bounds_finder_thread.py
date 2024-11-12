import re
from functools import lru_cache
from PySide6.QtCore import Signal, QThread
from collections import defaultdict
from arabic_reformer import diacritics_regex, alamaat_waqf, rub_el_hizb_mark
from my_utils.my_data_loader import MyDataLoader
from tabs_management.table_headers import WordTableHeaders
from my_widgets.lazy_table_widget import CustomTableRow


class WordBoundsFinderThread(QThread):
    result_ready = Signal(list, float, QThread)
    _diacritics_regex = re.compile(diacritics_regex)
    # _word_separator_regex = re.compile(rf"[{''.join(alamaat_waqf)}{rub_el_hizb_mark} ]+")
    _word_separator_regex = re.compile(r" (?:. )?")

    def __init__(self, diacritics_sensitive=True, thread_id=None):
        super().__init__()
        self._thread_id = thread_id
        self._matches = []
        self._diacritics_sensitive = diacritics_sensitive

    def set_data(self, matches, diacritics_sensitive):
        self._matches = matches
        self._diacritics_sensitive = diacritics_sensitive

    @lru_cache(maxsize=1000)
    def remove_diacritics(self, word):
        return WordBoundsFinderThread._diacritics_regex.sub("", word)

    def run(self):
        # print(f"word bounds start {id(self)}")
        counts = defaultdict(list)
        for surah_num, verse_num, verse, spans in self._matches:
            for span in spans:
                # spaces = list(re.finditer(" ", verse[:span[0]]))
                # word_id_first_match = len(spaces)
                # word_start = spaces[-1].span()[1] if spaces else 0

                # Strip rub el hizb mark at the beginning (lstrip and not rstrip although Arabic is RTL,
                # because 'l' means "leading".
                # 'r' means trailing btw.
                word_id_first_match = len(re.findall(WordBoundsFinderThread._word_separator_regex, verse[:span[0]].lstrip(f"{rub_el_hizb_mark} ")))
                word_start = verse.rfind(" ", 0, span[0]) + 1
                word_end = verse.find(" ", span[1])
                if word_end == -1:
                    word_end = len(verse)
                word = verse[word_start:word_end]
                # if int(surah_num) == 6 and int(verse_num) == 29:
                #     print(verse)
                #     print(span)
                #     print(word_id_first_match)
                #     print(word_start)
                #     print(word_end)
                #     print(word)
                if not self._diacritics_sensitive:
                    word = self.remove_diacritics(word)
                if word in counts and surah_num == counts[word][-1][0] and verse_num == counts[word][-1][1]:
                    counts[word][-1].extend((word_start, word_end))
                else:
                    counts[word].append([surah_num, verse_num, word_id_first_match, word_start, word_end])

        rows = []
        for w, data in counts.items():
            row_results = [None] * len(WordTableHeaders)
            row_results[WordTableHeaders.WORD_TEXT_HEADER.value] = w
            # TODO: This is only translation of first match...
            eng_translit, eng_transl = MyDataLoader.get_word_eng_transliteration(data[0][0], data[0][1], data[0][2])
            row_results[WordTableHeaders.ENGLISH_TRANSLATION.value] = eng_transl
            row_results[WordTableHeaders.ENGLISH_TRANSLITERATION.value] = eng_translit
            row_results[WordTableHeaders.RESULTS_HEADER.value] = sum(((len(lst) - 2) // 2) for lst in data)
            rows.append(CustomTableRow(row_results, data))

        self._matches = []
        self.result_ready.emit(rows, self._thread_id, self)
        # print(f"word bounds end {id(self)}")
