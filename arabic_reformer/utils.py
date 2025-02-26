from .globals import (alif_khunjariyah, _alifs)


def _connects_from_right(ch):
    return ch in _alifs + ["ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع",
                           "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي", "ى", "ئ", "ؤ", "ة", "ـ"]


def _connects_from_left(ch, support_alif_khunjariyah=False):
    alif_mamduda = support_alif_khunjariyah and ch == alif_khunjariyah
    return (ch in ["ب", "ت", "ث", "ج", "ح", "خ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن",
                   "ه", "ي", "ى", "ئ", "ـ"]) or alif_mamduda


def is_alif(ch):
    return ch in _alifs
