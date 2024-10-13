from PySide6.QtWidgets import QListWidgetItem

from arabic_reformer import remove_diacritics
from .abstract_subtext_getter import AbstractSubtextGetter
from .custom_results_sort_enum import CustomResultsSortEnum
from .custom_row import CustomRow


class CustomListWidgetItem(QListWidgetItem):
    def __init__(self, row: CustomRow, subtext_getter: AbstractSubtextGetter, get_sorting_method_handle):
        super().__init__(row.label)
        # self.metadata = row.metadata
        self.row = row
        self.get_sorting_method = get_sorting_method_handle
        self.subtext_getter = subtext_getter

    def __lt__(self, other):
        if self.subtext_getter is None:
            return super().__lt__(other)
        self.subtext_getter.find(self.text())
        surah_name_1, surah_num_1, surah_count_1 = self.subtext_getter.name, self.subtext_getter.number, self.subtext_getter.result
        self.subtext_getter.find(other.text())
        surah_name_2, surah_num_2, surah_count_2 = self.subtext_getter.name, self.subtext_getter.number, self.subtext_getter.result

        surah_name_1, surah_name_2 = remove_diacritics(surah_name_1), remove_diacritics(surah_name_2)

        sorting_method = self.get_sorting_method()
        match sorting_method:
            case CustomResultsSortEnum.BY_NUMBER:
                return int(surah_num_1) < int(surah_num_2)
            case CustomResultsSortEnum.BY_NAME:
                if surah_name_1 != surah_name_2:
                    return surah_name_1 < surah_name_2
                else:
                    return int(surah_count_1) < int(surah_count_2)
            case CustomResultsSortEnum.BY_RESULT_ASCENDING:
                if int(surah_count_1) != int(surah_count_2):
                    return int(surah_count_1) < int(surah_count_2)
                else:
                    return surah_name_1 < surah_name_2
            case CustomResultsSortEnum.BY_RESULT_DESCENDING:
                if int(surah_count_1) != int(surah_count_2):
                    return int(surah_count_1) > int(surah_count_2)
                else:
                    return surah_name_1 < surah_name_2
            case _:
                return surah_name_1 < surah_name_2
