from .alif import Alif
from .globals import (MAX_CONSECUTIVE_DIACRITICS, _diacritics_begin, _diacritics_end, alif_maksura,
                      _special_diacritics, diacritics_regex,
                      _prohibited_characters, _alifs, _d, diacritics_regex_compiled, alif_khunjariyah,
                      alamaat_waqf_regex)
from .la import La
from .utils import _connects_from_left, _connects_from_right, is_alif


def get_arabic_abc():
    return [k for k in _d.keys() if k != "invisible"]


def reform_char(ch):
    return _d.get(ch, ch)


def is_diacritic(ch):
    return (_diacritics_begin <= ch <= _diacritics_end) or ch in _special_diacritics


def remove_diacritics(txt):
    return diacritics_regex_compiled.sub("", txt)


def reform_text(txt, text_may_contain_diacritics=False):
    # diacritics supported

    def _get_next_char(txt_, current_idx):
        if not text_may_contain_diacritics and current_idx + 1 < len(txt_):
            return txt_[current_idx + 1]

        for j in range(1, MAX_CONSECUTIVE_DIACRITICS + 2):
            if current_idx + j < len(txt_) and not is_diacritic(txt_[current_idx + j]):
                return txt_[current_idx + j]
        return None

    def _get_prv_char(txt_, current_idx):
        if not text_may_contain_diacritics and current_idx - 1 >= 0:
            return txt_[current_idx - 1]

        for j in range(1, MAX_CONSECUTIVE_DIACRITICS + 2):
            if current_idx - j >= 0 and not is_diacritic(txt_[current_idx - j]):
                return txt_[current_idx - j]
        return None

    reformed = list(txt)
    for i, ch in enumerate(txt):
        if ch in _prohibited_characters:  # TODO: DEBUG
            reformed[i] = _d['invisible']
        elif ch not in _d:
            continue

        prv_char = _get_prv_char(txt, i)
        nxt_char = _get_next_char(txt, i)
        can_connect_from_right = _connects_from_right(ch)
        can_connect_from_left = _connects_from_left(ch)
        can_connect_from_both_sides = can_connect_from_right and can_connect_from_left
        prv_can_connect_from_left = _connects_from_left(prv_char, support_alif_khunjariyah=True)
        nxt_can_connect_from_right = _connects_from_right(nxt_char)
        if can_connect_from_both_sides:
            # potential to connect from both sides
            if prv_can_connect_from_left and nxt_can_connect_from_right:
                # middle
                if ch == "ل" and is_alif(nxt_char):
                    match nxt_char:
                        case Alif.ALIF:
                            # ـلا
                            reformed[i] = _d[ch][La.LA_CONNECTED_FROM_RIGHT]
                        case Alif.ALIF_WITH_HAMZA_ABOVE:
                            # ـلأ
                            reformed[i] = _d[ch][La.LA_WITH_ALIF_WITH_HAMZA_ABOVE_CONNECTED_FROM_LEFT]
                        case Alif.ALIF_WITH_HAMZA_BELOW:
                            # ـلإ
                            reformed[i] = _d[ch][La.LA_WITH_ALIF_WITH_HAMZA_BELOW_CONNECTED_FROM_LEFT]
                        case _:
                            # ـلا
                            reformed[i] = _d[ch][La.LA_CONNECTED_FROM_RIGHT]
                else:
                    reformed[i] = _d[ch][1]
            elif not prv_can_connect_from_left and nxt_can_connect_from_right:
                # beginning
                if ch == "ل" and is_alif(nxt_char):
                    match nxt_char:
                        case Alif.ALIF:
                            # لا
                            reformed[i] = _d[ch][La.ISOLATED_LA]
                        case Alif.ALIF_WITH_HAMZA_ABOVE:
                            # لأ
                            reformed[i] = _d[ch][La.ISOLATED_LA_WITH_ALIF_WITH_HAMZA_ABOVE]
                        case Alif.ALIF_WITH_HAMZA_BELOW:
                            # لإ
                            reformed[i] = _d[ch][La.ISOLATED_LA_WITH_ALIF_WITH_HAMZA_BELOW]
                        case _:
                            # لا
                            reformed[i] = _d[ch][La.ISOLATED_LA]
                else:
                    reformed[i] = _d[ch][0]
            elif not prv_can_connect_from_left and not nxt_can_connect_from_right and ord(ch) == 0x647:
                reformed[i] = chr(0xFEE9)
            elif prv_can_connect_from_left and not nxt_can_connect_from_right:
                # end
                reformed[i] = _d[ch][2]
        elif can_connect_from_right:
            # potential to connect only from right side
            if prv_can_connect_from_left:
                # end
                if is_alif(ch) and prv_char == "ل":
                    reformed[i] = _d['invisible']
                else:
                    reformed[i] = _d[ch][2]
        elif can_connect_from_left:
            # potential to connect only from left side
            if nxt_can_connect_from_right:
                # beginning
                reformed[i] = _d[ch][0]

    return ''.join(reformed)


def reform_span(txt, spans, text_may_contain_diacritics=False):
    res = txt
    for span in spans[::-1]:
        beginning_of_span = max(0, span[0] - 1)
        end_of_span = min(len(res), span[1] + 1)
        res = f"{res[:beginning_of_span]}{reform_text(res[beginning_of_span:end_of_span], text_may_contain_diacritics=text_may_contain_diacritics)}{txt[end_of_span:]}"
    return res


def reform_regex(p, alif_variations=True,
                 alif_alif_maksura_variations=False,
                 ya_variations=False,
                 ta_variations=False):
    new_p = ""
    for ch in p:
        if is_alif(ch) and (alif_variations or alif_alif_maksura_variations):
            variations = []
            if alif_variations:
                variations.extend(_alifs)
            if alif_alif_maksura_variations:
                variations.append(alif_maksura)
            new_p += f"[{''.join(variations)}]"
        elif ch == alif_maksura and (ya_variations or alif_alif_maksura_variations):
            variations = []
            if ya_variations:
                variations.extend(["ي", "ى"])
            if alif_alif_maksura_variations:
                variations.append(alif_maksura)
                if alif_variations:
                    variations.extend(_alifs)
                else:
                    variations.append("ا")
            new_p += f"[{''.join(variations)}]"
        elif ya_variations and ch in ["ي", "ى"]:
            new_p += "[يى]"
        elif ta_variations and ch in ["ت", "ة"]:
            new_p += "[تة]"
        else:
            new_p += ch
        if ch == " ":
            new_p += alamaat_waqf_regex
        elif not is_diacritic(ch):
            # not diacritics
            new_p += f"{diacritics_regex}{{,{MAX_CONSECUTIVE_DIACRITICS}}}"
    return new_p


def normalize_letter(ch):
    if is_alif(ch) or ch == alif_khunjariyah:
        return "ا"
    if ch in ["ي", "ى"]:
        return "ي"
    if ch in ["ت", "ة"]:
        return "ت"
    return ch
