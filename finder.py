import re
from my_data_loader import MyDataLoader


class Finder:
    def __init__(self):
        self.df = MyDataLoader.get_data()
        self._working_col = MyDataLoader.get_working_col()

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

    def find_word(self, w):
        spans, number_of_matches, found_in_surah, number_of_verses = zip(*self.df.apply(lambda row: self._find_in_surah(row, w), axis=1))  # NOTE: index is not retained
        # spans = chain.from_iterable(tup for lst in spans if lst is not None for tup in lst)
        # spans = (tup for lst in spans if lst is not None for tup in lst)
        spans = [tup for lst in spans if lst is not None for tup in lst]
        return spans, sum(number_of_matches), sum(found_in_surah), sum(number_of_verses)
