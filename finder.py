import re
from my_data_loader import MyDataLoader
from PySide6.QtCore import Signal, QThread
from arabic_reformer import reform_regex


class Finder(QThread):
    result_ready = Signal(str, int, tuple, QThread)

    def __init__(self):
        super().__init__()
        self.df = MyDataLoader.get_data()
        self._working_col = MyDataLoader.get_working_col()
        self._word = None
        self._words_num = None

    def prep_data(self, word, alif_alif_maksura_variations, ya_variations, ta_variations, full_word, beginning_of_word_flag, end_of_word_flag):
        # ignore diacritics
        # TODO: make checkbox?
        new_text = reform_regex(word,
                                alif_alif_maksura_variations=alif_alif_maksura_variations,
                                ya_variations=ya_variations,
                                ta_variations=ta_variations)

        search_words = len(new_text.split())
        new_text = f"({new_text})"  # capturing group
        beginning_of_word = r"[ ^]"
        end_of_word = r"[ ,$]"
        if full_word:
            new_text = beginning_of_word + rf"{new_text}" + end_of_word
        else:
            if beginning_of_word_flag:
                new_text = beginning_of_word + rf"{new_text}"
            if end_of_word_flag:
                new_text = rf"{new_text}" + end_of_word
        self._word = new_text
        self._words_num = search_words

    def _find_in_surah(self, row, w):
        verses_clean_split = row[self._working_col]
        number_of_matches = 0
        all_matches = []
        for i, verse in enumerate(verses_clean_split):
            # re.sub("\uFEFB", "لا", verse) ?
            matches_in_verse = [m.span(1) for m in re.finditer(w, verse, flags=re.M)]
            if matches_in_verse:
                # [(surah_num, verse_num, verse, [spans]), (...), ...]
                all_matches.append((int(row.name)+1, i + 1, verse, matches_in_verse))
                number_of_matches += len(matches_in_verse)
        return (all_matches if all_matches else None), number_of_matches, len(all_matches) > 0, len(all_matches)

    def _find_word(self, w):
        spans, number_of_matches, found_in_surah, number_of_verses = zip(*self.df.apply(lambda row: self._find_in_surah(row, w), axis=1))  # NOTE: index is not retained
        # spans = chain.from_iterable(tup for lst in spans if lst is not None for tup in lst)
        # spans = (tup for lst in spans if lst is not None for tup in lst)
        spans = [tup for lst in spans if lst is not None for tup in lst]
        return spans, sum(number_of_matches), sum(found_in_surah), sum(number_of_verses)

    def run(self):
        word = self._word
        words_num = self._words_num
        if word:
            result = self._find_word(word)
            self.result_ready.emit(word, words_num, result, self)

    def start_thread(self):
        if self.isRunning():
            self.wait()
        self.start()
