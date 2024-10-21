from re import compile as re_compile
from .alif import Alif

MAX_CONSECUTIVE_DIACRITICS = 4
_diacritics_begin = "\u064B"
_diacritics_end = "\u065F"
_alamaat_waqf = ["\u06D6", "\u06D8", "\u06D9", "\u06DA", "\u06DB", "\u06D7", "\u06DC"]
_long_harakat = ["\u06E5", "\u06E6", "\u06E7"]
alif_khunjariyah = "\u0670"  # ـٰ
_n_to_m_conversion = "\u06E2"
rub_el_hizb_mark = "\u06DE"
alif_maksura = "ى"
_special_diacritics = ["\uFC60", "\uFC61", "\uFC62", "\u0640", "\u06DF", "\u06EA"] + [
    alif_khunjariyah] + _alamaat_waqf + _long_harakat + [_n_to_m_conversion]
diacritics_regex = f"[{_diacritics_begin}-{_diacritics_end}{''.join(_special_diacritics)}]"
diacritics_regex_compiled = re_compile(diacritics_regex)
_prohibited_characters = ["\u0640"]  # TODO?

alamaat_waqf_regex = f"(?:[{''.join(_alamaat_waqf)}] )?"

# TODO: Adding _alif_khunjariyah to both special diacritics and to _alifs is a bit dangerous
_alifs = [Alif.ALIF,
          Alif.ALIF_WITH_HAMZA_ABOVE,
          Alif.ALIF_WITH_HAMZA_BELOW,
          Alif.ALIF_WITH_MADDA,
          Alif.ALIF_WITH_HAMZAT_WASL,
          Alif.ALIF_WITH_HAMZAT_WASL2] + [alif_khunjariyah]
_d = {
    "invisible": chr(0x200B),
    "ا": (None, None, chr(0xFE8E)),
    "أ": (None, None, chr(0xFE84)),
    "إ": (None, None, chr(0xFE88)),
    "آ": (None, None, chr(0xFE82)),
    "ﭐ": (None, None, chr(0xFB51)),
    "ٱ": (None, None, chr(0xFB51)),
    "ب": (chr(0xFE91), chr(0xFE92), chr(0xFE90)),
    "ت": (chr(0xFE97), chr(0xFE98), chr(0xFE96)),
    "ث": (chr(0xFE9B), chr(0xFE9C), chr(0xFE9A)),
    "ج": (chr(0xFE9F), chr(0xFEA0), chr(0xFE9E)),
    "ح": (chr(0xFEA3), chr(0xFEA4), chr(0xFEA2)),
    "خ": (chr(0xFEA7), chr(0xFEA8), chr(0xFEA6)),
    "د": (None, None, chr(0xFEAA)),
    "ذ": (None, None, chr(0xFEAC)),
    "ر": (None, None, chr(0xFEAE)),
    "ز": (None, None, chr(0xFEB0)),
    "س": (chr(0xFEB3), chr(0xFEB4), chr(0xFEB2)),
    "ش": (chr(0xFEB7), chr(0xFEB8), chr(0xFEB6)),
    "ص": (chr(0xFEBB), chr(0xFEBC), chr(0xFEBA)),
    "ض": (chr(0xFEBF), chr(0xFEC0), chr(0xFEBE)),
    "ط": (chr(0xFEC3), chr(0xFEC4), chr(0xFEC2)),
    "ظ": (chr(0xFEC7), chr(0xFEC8), chr(0xFEC6)),
    "ع": (chr(0xFECB), chr(0xFECC), chr(0xFECA)),
    "غ": (chr(0xFECF), chr(0xFED0), chr(0xFECE)),
    "ف": (chr(0xFED3), chr(0xFED4), chr(0xFED2)),
    "ق": (chr(0xFED7), chr(0xFED8), chr(0xFED6)),
    "ك": (chr(0xFEDB), chr(0xFEDC), chr(0xFEDA)),

    # See class La
    "ل": (chr(0xFEDF), chr(0xFEE0), chr(0xFEDE), chr(0xFEFB), chr(0xFEFC), chr(0xFEF7), chr(0xFEF9), chr(0xFEF8),
          chr(0xFEFA)),

    "م": (chr(0xFEE3), chr(0xFEE4), chr(0xFEE2)),
    "ن": (chr(0xFEE7), chr(0xFEE8), chr(0xFEE6)),
    "ه": (chr(0xFEEB), chr(0xFEEC), chr(0xFEEA)),
    "و": (None, None, chr(0xFEEE)),
    "ؤ": (None, None, chr(0xFE86)),
    "ي": (chr(0xFEF3), chr(0xFEF4), chr(0xFEF2)),
    "ة": (None, None, chr(0xFE94)),
    "ى": (chr(0xFBE8), "ـ", chr(0xFEF0)),  # TODO: DEBUG
    "ئ": (chr(0xFE8B), chr(0xFE8C), chr(0xFE8A)),
    "ء": (chr(0x0621), chr(0x0621), chr(0x0621)),
}
