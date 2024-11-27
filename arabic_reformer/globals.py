import re
from re import compile as re_compile
from .alif import Alif

MAX_CONSECUTIVE_DIACRITICS = 5  # 5 because ـ (e.g. in "وَلِـِّۧىَ")
_diacritics_begin = "\u064B"
_diacritics_end = "\u065F"
alamaat_waqf = ["\u06D6", "\u06D8", "\u06D9", "\u06DA", "\u06DB", "\u06D7", "\u06DC"]
_long_harakat = ["\u06E5", "\u06E6", "\u06E7"]
alif_khunjariyah = "\u0670"  # ـٰ
waw_khunjariyah = "وٰ"  # 2 characters
_n_to_m_conversion = "\u06E2"
rub_el_hizb_mark = "\u06DE"
sujood_mark = "\u06E9"
alif_maksura = "\u0649"  # "ى"
_ya_variations = ['\u064a', '\u0649']  # ["ي", "ى"]
_final_ta_variations = ['\u062a', '\u0629']  # ["ت", "ة"]
_hamza_above = "\u0654"
_hamza = "\u0621"  # "ء"
_hamzas = [_hamza, _hamza_above]
_tatweel_character = "\u0640"
_special_diacritics = ["\uFC60", "\uFC61", "\uFC62", _tatweel_character, "\u06DF", "\u06EA"] + [
    alif_khunjariyah] + alamaat_waqf + _long_harakat + [_n_to_m_conversion]
diacritics_regex = f"[{_diacritics_begin}-{_diacritics_end}{''.join(_special_diacritics)}]"
diacritics_regex_compiled = re_compile(diacritics_regex)
diacritics_ending_regex_compiled = re_compile(f"{diacritics_regex}+$")
# _prohibited_characters = ["\u0640"]  # TODO?
_prohibited_characters = []  # TODO?

alamaat_waqf_regex = f"(?:[{''.join(alamaat_waqf)}] )?"

# TODO: Adding _alif_khunjariyah to both special diacritics and to _alifs is a bit dangerous
_alifs = [Alif.ALIF,
          Alif.ALIF_WITH_HAMZA_ABOVE,
          Alif.ALIF_WITH_HAMZA_BELOW,
          Alif.ALIF_WITH_MADDA,
          Alif.ALIF_WITH_HAMZAT_WASL,
          Alif.ALIF_WITH_HAMZAT_WASL2] + [alif_khunjariyah]

_alifs_without_khunjariya = [Alif.ALIF,
                             Alif.ALIF_WITH_HAMZA_ABOVE,
                             Alif.ALIF_WITH_HAMZA_BELOW,
                             Alif.ALIF_WITH_MADDA,
                             Alif.ALIF_WITH_HAMZAT_WASL,
                             Alif.ALIF_WITH_HAMZAT_WASL2]

waw_alif_khunjariyah_regex = re.compile("وٰ")
alifs_regex_with_khunjariyah = re.compile(rf"[{''.join(_alifs)}]")
alifs_regex_without_khunjariyah = re.compile(rf"[{''.join(_alifs_without_khunjariya)}]")

_d = {
    "invisible": chr(0x200B),
    "\u0627": (None, None, chr(0xFE8E)),  # ا
    "\u0623": (None, None, chr(0xFE84)),  # أ
    "\u0625": (None, None, chr(0xFE88)),  # إ
    "\u0622": (None, None, chr(0xFE82)),  # آ
    "\ufb50": (None, None, chr(0xFB51)),  # ﭐ
    "\u0671": (None, None, chr(0xFB51)),  # ٱ
    "\u0628": (chr(0xFE91), chr(0xFE92), chr(0xFE90)),  # ب
    "\u062a": (chr(0xFE97), chr(0xFE98), chr(0xFE96)),  # ت
    "\u062b": (chr(0xFE9B), chr(0xFE9C), chr(0xFE9A)),  # ث
    "\u062c": (chr(0xFE9F), chr(0xFEA0), chr(0xFE9E)),  # ج
    "\u062d": (chr(0xFEA3), chr(0xFEA4), chr(0xFEA2)),  # ح
    "\u062e": (chr(0xFEA7), chr(0xFEA8), chr(0xFEA6)),  # خ
    "\u062f": (None, None, chr(0xFEAA)),  # د
    "\u0630": (None, None, chr(0xFEAC)),  # ذ
    "\u0631": (None, None, chr(0xFEAE)),  # ر
    "\u0632": (None, None, chr(0xFEB0)),  # ز
    "\u0633": (chr(0xFEB3), chr(0xFEB4), chr(0xFEB2)),  # س
    "\u0634": (chr(0xFEB7), chr(0xFEB8), chr(0xFEB6)),  # ش
    "\u0635": (chr(0xFEBB), chr(0xFEBC), chr(0xFEBA)),  # ص
    "\u0636": (chr(0xFEBF), chr(0xFEC0), chr(0xFEBE)),  # ض
    "\u0637": (chr(0xFEC3), chr(0xFEC4), chr(0xFEC2)),  # ط
    "\u0638": (chr(0xFEC7), chr(0xFEC8), chr(0xFEC6)),  # ظ
    "\u0639": (chr(0xFECB), chr(0xFECC), chr(0xFECA)),  # ع
    "\u063a": (chr(0xFECF), chr(0xFED0), chr(0xFECE)),  # غ
    "\u0641": (chr(0xFED3), chr(0xFED4), chr(0xFED2)),  # ف
    "\u0642": (chr(0xFED7), chr(0xFED8), chr(0xFED6)),  # ق
    "\u0643": (chr(0xFEDB), chr(0xFEDC), chr(0xFEDA)),  # ك

    # See class La
    "\u0644": (chr(0xFEDF), chr(0xFEE0), chr(0xFEDE), chr(0xFEFB), chr(0xFEFC), chr(0xFEF7), chr(0xFEF9), chr(0xFEF8),
          chr(0xFEFA)),  # ل

    "\u0645": (chr(0xFEE3), chr(0xFEE4), chr(0xFEE2)),  # م
    "\u0646": (chr(0xFEE7), chr(0xFEE8), chr(0xFEE6)),  # ن
    "\u0647": (chr(0xFEEB), chr(0xFEEC), chr(0xFEEA)),  # ه
    "\u0648": (None, None, chr(0xFEEE)),  # و
    "\u0624": (None, None, chr(0xFE86)),  # ؤ
    "\u064a": (chr(0xFEF3), chr(0xFEF4), chr(0xFEF2)),  # ي
    "\u0629": (None, None, chr(0xFE94)),  # ة
    "\u0649": (chr(0xFBE8), "ـ", chr(0xFEF0)),  # TODO: DEBUG  # ى
    "\u0640": (chr(0xFBE8), "ـ", chr(0xFEF0)),  # TODO: DEBUG  # ـ
    "\u0626": (chr(0xFE8B), chr(0xFE8C), chr(0xFE8A)),  # ئ
    "\u0621": (chr(0x0621), chr(0x0621), chr(0x0621)),  # ء
}

arabic_alphabit = [x for x in sum([[k] + [v_i for v_i in v] for k, v in _d.items() if k != 'invisible'] +
                                  [_alifs] +
                                  [_hamzas] +
                                  [_ya_variations] +
                                  [_final_ta_variations], [])
                   if x is not None]
