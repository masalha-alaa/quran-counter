from enum import Enum, auto


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
                return "(ترتيب ابجدي)"
            case self.BY_RESULT_ASCENDING:
                return "(عدد النتائج صعودًا)"
            case self.BY_RESULT_DESCENDING:
                return "(عدد النتائج نزولًا)"
