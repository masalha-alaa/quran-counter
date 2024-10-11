from .surah_results_sort_enum import SurahResultsSortEnum


class SurahResultsSort:
    def __init__(self, initial_value=SurahResultsSortEnum.BY_NUMBER):
        self._current = initial_value

    def switch_order(self):
        self._current = SurahResultsSortEnum((self._current.value + 1) % len(SurahResultsSortEnum))
        return self._current

    def get_current(self):
        return self._current
