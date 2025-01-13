from enum import Enum, auto


class AppLang(Enum):
    ARABIC = "ar"
    ENGLISH = "en"
    DEFAULT_LANGUAGE = ARABIC


class ScaleRounding(Enum):
    NONE = auto()
    NORMAL = auto()
    CEIL = auto()
    FLOOR = auto()
