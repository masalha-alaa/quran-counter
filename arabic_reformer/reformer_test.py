from arabic_reformer import reform_text, reform_regex, normalize_letter

if __name__ == '__main__':
    import re
    from emphasizer import emphasize_span, CssColors

    print(reform_regex("الليل"))

    txt2 = "بِسْمِ الله الرحمن الرحيم"
    w = "بس"
    print(txt2)
    spans = [m.span() for m in re.finditer(reform_regex(w), txt2)]
    print(spans)
    print(emphasize_span(reform_text(txt2, text_may_contain_diacritics=True), spans, color=CssColors.BLUE, css=True))

    word = "ٱلْجَنَّةَ وَكُلَا مِنْهَا"
    for ch in word:
        print(f"{normalize_letter((ch)) = }")

