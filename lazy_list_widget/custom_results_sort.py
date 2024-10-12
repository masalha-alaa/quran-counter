from .custom_results_sort_enum import CustomResultsSortEnum


class CustomResultsSort:
    def __init__(self, initial_value=CustomResultsSortEnum.BY_NUMBER):
        self._current = initial_value

    def switch_order(self):
        self._current = CustomResultsSortEnum((self._current.value + 1) % len(CustomResultsSortEnum))
        return self._current

    def get_current(self):
        return self._current
