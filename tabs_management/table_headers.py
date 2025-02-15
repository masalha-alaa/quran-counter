from abc import abstractmethod
from enum import Enum, auto


class TableHeaders(Enum):
    @property
    @abstractmethod
    def METADATA_POSITION(self):
        """Abstract property that must be defined in subclasses."""
        pass


class SurahTableHeaders(TableHeaders):
    SURAH_NAME_HEADER = 0
    SURAH_NUM_HEADER = auto()
    RESULTS_HEADER = auto()
    METADATA_POSITION = RESULTS_HEADER


class WordTableHeaders(TableHeaders):
    WORD_TEXT_HEADER = 0
    ENGLISH_TRANSLITERATION = auto()
    ENGLISH_TRANSLATION = auto()
    RESULTS_HEADER = auto()
    PATH_HEADER = auto()
    METADATA_POSITION = RESULTS_HEADER

class TopicTableHeaders(TableHeaders):
    TOPIC_NAME_HEADER = 0
    SCORE_HEADER = auto()
    RESULTS_HEADER = auto()
    METADATA_POSITION = RESULTS_HEADER


if __name__ == '__main__':
    print(f"{len(SurahTableHeaders) = }")  # doesn't include same value enums
    print(f"{len(WordTableHeaders) = }")  # doesn't include same value enums
    print(f"{SurahTableHeaders.METADATA_POSITION = }")
    print(f"{WordTableHeaders.METADATA_POSITION = }")
