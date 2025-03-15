class MatchItem:
    def __init__(self, surah_num, verse_num, verse_text=None, spans=None, other=None):
        self.surah_num = surah_num
        self.verse_num = verse_num
        self.verse_text = verse_text
        self.spans = spans
        self.other = other

    def __iter__(self):
        return iter((self.surah_num, self.verse_num, self.verse_text, self.spans, self.other))
