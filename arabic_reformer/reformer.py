class Reformer:
    MAX_CONSECUTIVE_DIACRITICS = 4

    class La:
        LAM_CONNECTED_FROM_LEFT = 0  # لـ
        LAM_CONNECTED_FROM_BOTH_SIDES = 1  # ـلـ
        LAM_CONNECTED_FROM_BOTH_RIGHT = 2  # ـل
        ISOLATED_LA = 3  # لا
        LA_CONNECTED_FROM_RIGHT = 4  # ـلا
        ISOLATED_LA_WITH_ALIF_WITH_HAMZA_ABOVE = 5  # لأ
        ISOLATED_LA_WITH_ALIF_WITH_HAMZA_BELOW = 6  # لإ
        LA_WITH_ALIF_WITH_HAMZA_ABOVE_CONNECTED_FROM_LEFT = 7  # ـلأ
        LA_WITH_ALIF_WITH_HAMZA_BELOW_CONNECTED_FROM_LEFT = 8  # ـلإ

    class Alif:
        ALIF = 'ا'
        ALIF_WITH_HAMZA_ABOVE = 'أ'
        ALIF_WITH_HAMZA_BELOW = 'إ'
        ALIF_WITH_MADDA = 'آ'
        ALIF_WITH_HAMZAT_WASL = 'ﭐ'
        ALIF_WITH_HAMZAT_WASL2 = 'ٱ'

    def __init__(self):
        self._diacritics_begin = "\u064B"
        self._diacritics_end = "\u065F"
        self._alamaat_waqf = ["\u06D6", "\u06D8", "\u06D9", "\u06DA", "\u06DB", "\u06D7", "\u06DC"]
        self._long_harakat = ["\u06E6", "\u06E7"]
        self._alif_khunjariyah = "\u0670"  # ـٰ
        self._alif_maksura = "ى"
        self._special_diacritics = ["\uFC60", "\uFC61", "\uFC62", "\u0640", "\u06DF", "\u06EA"] + [self._alif_khunjariyah] + self._alamaat_waqf + self._long_harakat
        self._diacritics = f"[{self._diacritics_begin}-{self._diacritics_end}{''.join(self._special_diacritics)}]"

        # TODO: Adding _alif_khunjariyah to both special diacritics and to _alifs is a bit dangerous
        self._alifs = [Reformer.Alif.ALIF,
                       Reformer.Alif.ALIF_WITH_HAMZA_ABOVE,
                       Reformer.Alif.ALIF_WITH_HAMZA_BELOW,
                       Reformer.Alif.ALIF_WITH_MADDA,
                       Reformer.Alif.ALIF_WITH_HAMZAT_WASL,
                       Reformer.Alif.ALIF_WITH_HAMZAT_WASL2] + [self._alif_khunjariyah]
        self._d = self._build_dict()

    def _connects_from_right(self, ch):
        return ch in self._alifs + ["ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي", "ى", "ئ", "ؤ", "ة"]

    def _connects_from_left(self, ch, support_alif_khunjariyah=False):
        alif_mamduda = support_alif_khunjariyah and ch == self._alif_khunjariyah
        return (ch in ["ب", "ت", "ث", "ج", "ح", "خ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "ي", "ى", "ئ"]) or alif_mamduda

    def _is_alif(self, ch):
        return ch in self._alifs

    def _build_dict(self):
        d = {
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
            "ل": (chr(0xFEDF), chr(0xFEE0), chr(0xFEDE), chr(0xFEFB), chr(0xFEFC), chr(0xFEF7), chr(0xFEF9), chr(0xFEF8), chr(0xFEFA)),

            "م": (chr(0xFEE3), chr(0xFEE4), chr(0xFEE2)),
            "ن": (chr(0xFEE7), chr(0xFEE8), chr(0xFEE6)),
            "ه": (chr(0xFEEB), chr(0xFEEC), chr(0xFEEA)),
            "و": (None, None, chr(0xFEEE)),
            "ؤ": (None, None, chr(0xFE86)),
            "ي": (chr(0xFEF3), chr(0xFEF4), chr(0xFEF2)),
            "ة": (None, None, chr(0xFE94)),
            "ى": ("ىـ", "ـ", chr(0xFEF0)),  # TODO: DEBUG
            "ئ": (chr(0xFE8B), chr(0xFE8C), chr(0xFE8A)),
             }
        return d

    def reformer_char(self, ch):
        return self._d.get(ch, ch)

    def _is_diacritic(self, ch):
        return (self._diacritics_begin <= ch <= self._diacritics_end) or ch in self._diacritics

    def reform_text_old(self, txt):
        # diacritics not supported

        reformed = list(txt)
        for i, ch in enumerate(txt):
            if ch not in self._d:
                continue
            can_connect_from_right = self._connects_from_right(ch)
            can_connect_from_left = self._connects_from_left(ch)
            can_connect_from_both_sides = can_connect_from_right and can_connect_from_left
            prv_can_connect_from_left = i - 1 >= 0 and self._connects_from_left(txt[i - 1])
            nxt_can_connect_from_right = i + 1 < len(txt) and self._connects_from_right(txt[i + 1])
            if can_connect_from_both_sides:
                # potential to connect from both sides
                if prv_can_connect_from_left and nxt_can_connect_from_right:
                    # middle
                    if ch == "ل" and self._is_alif(txt[i + 1]):
                        # ـلا
                        reformed[i] = self._d[ch][4]
                    else:
                        reformed[i] = self._d[ch][1]
                elif not prv_can_connect_from_left and nxt_can_connect_from_right:
                    # beginning
                    if ch == "ل" and self._is_alif(txt[i + 1]):
                        # لا
                        reformed[i] = self._d[ch][3]
                    else:
                        reformed[i] = self._d[ch][0]
                elif prv_can_connect_from_left and not nxt_can_connect_from_right:
                    # end
                    reformed[i] = self._d[ch][2]
            elif can_connect_from_right:
                # potential to connect only from right side
                if prv_can_connect_from_left:
                    # end
                    if self._is_alif(ch) and txt[i - 1] == "ل":
                        reformed[i] = self._d['invisible']
                    else:
                        reformed[i] = self._d[ch][2]
            elif can_connect_from_left:
                # potential to connect only from left side
                if nxt_can_connect_from_right:
                    # beginning
                    reformed[i] = self._d[ch][0]

        return ''.join(reformed)

    def reform_text(self, txt, text_may_contain_diacritics=False):
        # diacritics supported

        def _get_next_char(txt_, current_idx):
            if not text_may_contain_diacritics and current_idx + 1 < len(txt_):
                return txt_[current_idx + 1]

            for j in range(1, Reformer.MAX_CONSECUTIVE_DIACRITICS + 2):
                if current_idx + j < len(txt_) and not self._is_diacritic(txt_[current_idx + j]):
                    return txt_[current_idx + j]
            return None

        def _get_prv_char(txt_, current_idx):
            if not text_may_contain_diacritics and current_idx - 1 >= 0:
                return txt_[current_idx - 1]

            for j in range(1, Reformer.MAX_CONSECUTIVE_DIACRITICS + 2):
                if current_idx - j >= 0 and not self._is_diacritic(txt_[current_idx - j]):
                    return txt_[current_idx - j]
            return None

        reformed = list(txt)
        for i, ch in enumerate(txt):
            if ch not in self._d:
                continue

            prv_char = _get_prv_char(txt, i)
            nxt_char = _get_next_char(txt, i)
            can_connect_from_right = self._connects_from_right(ch)
            can_connect_from_left = self._connects_from_left(ch)
            can_connect_from_both_sides = can_connect_from_right and can_connect_from_left
            prv_can_connect_from_left = self._connects_from_left(prv_char, support_alif_khunjariyah=True)
            nxt_can_connect_from_right = self._connects_from_right(nxt_char)
            if can_connect_from_both_sides:
                # potential to connect from both sides
                if prv_can_connect_from_left and nxt_can_connect_from_right:
                    # middle
                    if ch == "ل" and self._is_alif(nxt_char):
                        match nxt_char:
                            case Reformer.Alif.ALIF:
                                # ـلا
                                reformed[i] = self._d[ch][Reformer.La.LA_CONNECTED_FROM_RIGHT]
                            case Reformer.Alif.ALIF_WITH_HAMZA_ABOVE:
                                # ـلأ
                                reformed[i] = self._d[ch][Reformer.La.LA_WITH_ALIF_WITH_HAMZA_ABOVE_CONNECTED_FROM_LEFT]
                            case Reformer.Alif.ALIF_WITH_HAMZA_BELOW:
                                # ـلإ
                                reformed[i] = self._d[ch][Reformer.La.LA_WITH_ALIF_WITH_HAMZA_BELOW_CONNECTED_FROM_LEFT]
                            case _:
                                # ـلا
                                reformed[i] = self._d[ch][Reformer.La.LA_CONNECTED_FROM_RIGHT]
                    else:
                        reformed[i] = self._d[ch][1]
                elif not prv_can_connect_from_left and nxt_can_connect_from_right:
                    # beginning
                    if ch == "ل" and self._is_alif(nxt_char):
                        match nxt_char:
                            case Reformer.Alif.ALIF:
                                # لا
                                reformed[i] = self._d[ch][Reformer.La.ISOLATED_LA]
                            case Reformer.Alif.ALIF_WITH_HAMZA_ABOVE:
                                # لأ
                                reformed[i] = self._d[ch][Reformer.La.ISOLATED_LA_WITH_ALIF_WITH_HAMZA_ABOVE]
                            case Reformer.Alif.ALIF_WITH_HAMZA_BELOW:
                                # لإ
                                reformed[i] = self._d[ch][Reformer.La.ISOLATED_LA_WITH_ALIF_WITH_HAMZA_BELOW]
                            case _:
                                # لا
                                reformed[i] = self._d[ch][Reformer.La.ISOLATED_LA]
                    else:
                        reformed[i] = self._d[ch][0]
                elif prv_can_connect_from_left and not nxt_can_connect_from_right:
                    # end
                    reformed[i] = self._d[ch][2]
            elif can_connect_from_right:
                # potential to connect only from right side
                if prv_can_connect_from_left:
                    # end
                    if self._is_alif(ch) and prv_char == "ل":
                        reformed[i] = self._d['invisible']
                    else:
                        reformed[i] = self._d[ch][2]
            elif can_connect_from_left:
                # potential to connect only from left side
                if nxt_can_connect_from_right:
                    # beginning
                    reformed[i] = self._d[ch][0]

        return ''.join(reformed)

    def reform_span(self, txt, span):
        beginning_of_span = max(0, span[0] - 1)
        end_of_span = min(len(txt), span[1] + 1)
        return f"{txt[:beginning_of_span]}{self.reform_text(txt[beginning_of_span:end_of_span])}{txt[end_of_span:]}"

    def reform_regex(self, p):
        new_p = ""
        for ch in p:
            if self._is_alif(ch):
                new_p += f"[{''.join(self._alifs)}{self._alif_maksura}]"
            else:
                new_p += ch
            if ch == " ":
                new_p += f"(?:[{''.join(self._alamaat_waqf)}] )?"
            elif not self._is_diacritic(ch):
                # not diacritics
                new_p += f"{self._diacritics}{{,{Reformer.MAX_CONSECUTIVE_DIACRITICS}}}"
        return new_p


if __name__ == '__main__':
    import re
    from emphasizer import emphasize_span, CssColors

    reformer = Reformer()

    print(reformer.reform_regex("الليل"))

    txt2 = "بِسْمِ الله الرحمن الرحيم"
    w = "بس"
    print(txt2)
    spans = [m.span() for m in re.finditer(reformer.reform_regex(w), txt2)]
    print(spans)
    print(emphasize_span(reformer.reform_text(txt2, text_may_contain_diacritics=True), spans, color=CssColors.BLUE, css=True))


