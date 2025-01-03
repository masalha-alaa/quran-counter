import os
import sys
from math import ceil
from enum import Enum, auto
from arabic_reformer import strip_last_diacritic
from paths import ROOT_DIR
try:
    from PySide6.QtCore import QCoreApplication
except ImportError:
    print("Warning: PySide6 not installed")

class AppLang(Enum):
    ARABIC = "ar"
    ENGLISH = "en"
    DEFAULT_LANGUAGE = ARABIC


class ScaleRounding(Enum):
    NONE = auto()
    NORMAL = auto()
    CEIL = auto()
    FLOOR = auto()


def resource_path(relative_path):
    """Get the absolute path to the resource (works for both PyInstaller bundle and during development)."""
    if hasattr(sys, '_MEIPASS'):
        # When bundled by PyInstaller, files are unpacked into a temporary directory
        return os.path.join(sys._MEIPASS, relative_path)
    elif 'COLAB_JUPYTER_IP' in os.environ:
        return f"{ROOT_DIR}/{relative_path}"
    else:
        # When running in development mode (not bundled), just use the relative path
        return relative_path


def translate_text(text):
    return QCoreApplication.translate("Dynamic", text)


def load_translation(translator, path):
    return translator.load(resource_path(path))


def equal_words(w1, w2):
    return strip_last_diacritic(w1) == strip_last_diacritic(w2)


def scale(x, old_min, old_max, new_min, new_max, rounding:ScaleRounding=ScaleRounding.NONE):
    new_x = new_min + ((x - old_min) * (new_max - new_min)) / (old_max - old_min)
    match rounding:
        case ScaleRounding.NORMAL:
            new_x = round(new_x)
        case ScaleRounding.CEIL:
            new_x = ceil(new_x)
        case ScaleRounding.FLOOR:
            new_x = int(new_x)
        case _:
            pass
    return new_x
