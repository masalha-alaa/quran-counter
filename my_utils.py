import os
import sys
from enum import Enum
from PySide6.QtCore import QCoreApplication

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
        return os.path.join(os.path.abspath("."), relative_path)


def translate_text(text):
    return QCoreApplication.translate("Dynamic", text)

