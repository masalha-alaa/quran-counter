import re
from enum import Enum, auto
from PySide6.QtWidgets import QListWidgetItem


class SurahResultsSortEnum(Enum):
    BY_NUMBER = 0
    BY_NAME = auto()
    BY_RESULT_ASCENDING = auto()
    BY_RESULT_DESCENDING = auto()

    def to_string(self):
        match self:
            case self.BY_NUMBER:
                return "(رقم السورة)"
            case self.BY_NAME:
                return "(اسم السورة)"
            case self.BY_RESULT_ASCENDING:
                return "(عدد النتائج صعودًا)"
            case self.BY_RESULT_DESCENDING:
                return "(عدد النتائج نزولًا)"


class SurahResultsSort:
    def __init__(self, initial_value=SurahResultsSortEnum.BY_NUMBER):
        self._current = initial_value

    def switch_order(self):
        self._current = SurahResultsSortEnum((self._current.value + 1) % len(SurahResultsSortEnum))
        return self._current

    def get_current(self):
        return self._current


class CustomSurahSortWidget(QListWidgetItem):
    _ptrn = re.compile(r"(.*)\s+\(#(\d{,3})\):\s+(\d+)")
    _list_ids = {}

    def __init__(self, label, list_id):
        super().__init__(label)
        self._my_list_id = list_id

    @staticmethod
    def add_list_id(list_id, initial_sorting: SurahResultsSortEnum = None):
        if list_id not in CustomSurahSortWidget._list_ids:
            CustomSurahSortWidget._list_ids[list_id] = SurahResultsSort(initial_sorting)

    @staticmethod
    def set_sorting(list_id, sorting_method: SurahResultsSortEnum):
        if list_id in CustomSurahSortWidget._list_ids:
            CustomSurahSortWidget._list_ids[list_id] = SurahResultsSort(sorting_method)
        else:
            raise KeyError(f"{list_id} does not exist. Please call add_list_id() first.")

    @staticmethod
    def switch_order(list_id):
        return CustomSurahSortWidget._list_ids[list_id].switch_order()

    @staticmethod
    def pop_list_id(list_id):
        CustomSurahSortWidget._list_ids.pop(list_id)

    @staticmethod
    def get_current_sorting(list_id):
        if list_id in CustomSurahSortWidget._list_ids:
            return CustomSurahSortWidget._list_ids[list_id].get_current()
        return None

    def __lt__(self, other):
        self_details = self._ptrn.match(self.text())
        other_details = self._ptrn.match(other.text())
        surah_name_1, surah_num_1, surah_count_1 = self_details.group(1), self_details.group(2), self_details.group(3)
        surah_name_2, surah_num_2, surah_count_2 = other_details.group(1), other_details.group(2), other_details.group(3)

        new_sort_method = CustomSurahSortWidget._list_ids[self._my_list_id].get_current()
        match new_sort_method:
            case SurahResultsSortEnum.BY_NUMBER:
                return int(surah_num_1) < int(surah_num_2)
            case SurahResultsSortEnum.BY_NAME:
                return surah_name_1 < surah_name_2
            case SurahResultsSortEnum.BY_RESULT_ASCENDING:
                if int(surah_count_1) != int(surah_count_2):
                    return int(surah_count_1) < int(surah_count_2)
                else:
                    return surah_name_1 < surah_name_2
            case SurahResultsSortEnum.BY_RESULT_DESCENDING:
                if int(surah_count_1) != int(surah_count_2):
                    return int(surah_count_1) > int(surah_count_2)
                else:
                    return surah_name_1 < surah_name_2
