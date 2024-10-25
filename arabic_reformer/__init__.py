from .globals import (diacritics_regex, alif_maksura,
                      alif_khunjariyah, alamaat_waqf_regex,
                      rub_el_hizb_mark, arabic_alphabit,
                      diacritics_regex_compiled, diacritics_ending_regex_compiled)
from .reformer import (get_arabic_abc, reform_char,
                       is_diacritic, reform_text,
                       reform_span, reform_regex,
                       remove_diacritics, normalize_letter)
from .utils import is_alif
