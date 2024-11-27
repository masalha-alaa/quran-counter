from .globals import (diacritics_regex, alif_maksura,
                      alif_khunjariyah, alamaat_waqf_regex, alamaat_waqf,
                      rub_el_hizb_mark, sujood_mark, arabic_alphabit,
                      diacritics_regex_compiled, diacritics_ending_regex_compiled,
                      waw_khunjariyah)
from .reformer import (get_arabic_abc, reform_char,
                       is_diacritic, reform_text,
                       reform_span, reform_regex,
                       remove_diacritics, normalize_letter,
                       strip_last_diacritic, normalize_alif)
from .utils import is_alif
