import os
import sys
from enum import Enum
from PySide6.QtCore import QCoreApplication
from arabic_reformer import is_diacritic

class AppLang(Enum):
    ARABIC = "ar"
    ENGLISH = "en"


def resource_path(relative_path):
    """Get the absolute path to the resource (works for both PyInstaller bundle and during development)."""
    if hasattr(sys, '_MEIPASS'):
        # When bundled by PyInstaller, files are unpacked into a temporary directory
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # When running in development mode (not bundled), just use the relative path
        return relative_path


def translate_text(text):
    return QCoreApplication.translate("Dynamic", text)


def load_translation(translator, path):
    return translator.load(resource_path(path))


def equal_words(w1, w2):
    if w1[:-1] == w2[:-1] and (w1[-1] == w2[-1] or (is_diacritic(w1[-1]) and is_diacritic(w2[-1]))):
        return True
    return False
