class CursorPositionInfo:
    def __init__(self,
                 surah_name=None,
                 surah_num=None,
                 verse_num=None,
                 page_num=None,
                 words_num_in_verse=None,
                 word=None):
        self.surah_name = surah_name
        self.surah_num = surah_num
        self.verse_num = verse_num
        self.page_num = page_num
        self.word_num_in_verse = words_num_in_verse
        self.word = word

    def is_valid(self):
        return (self.surah_name is not None or
                self.surah_num is not None or
                self.verse_num is not None or
                self.page_num is not None or
                self.word_num_in_verse is not None or
                self.word is not None)

    def clear(self):
        self.surah_name = None
        self.surah_num = None
        self.verse_num = None
        self.page_num = None
        self.word_num_in_verse = None
        self.word = None

    def __gt__(self, other):
        # greater than
        if int(self.page_num) > int(other.page_num):
            return True
        if int(self.page_num) == int(other.page_num):
            if int(self.surah_num) > int(other.surah_num):
                return True
            if int(self.surah_num) == int(other.surah_num):
                if int(self.verse_num) > int(other.verse_num):
                    return True
                if int(self.verse_num) == int(other.verse_num):
                    return self.word_num_in_verse > other.word_num_in_verse
        return False

    def __lt__(self, other):
        # less than
        if int(self.page_num) < int(other.page_num):
            return True
        if int(self.page_num) == int(other.page_num):
            if int(self.surah_num) < int(other.surah_num):
                return True
            if int(self.surah_num) == int(other.surah_num):
                if int(self.verse_num) < int(other.verse_num):
                    return True
                if int(self.verse_num) == int(other.verse_num):
                    return self.word_num_in_verse < other.word_num_in_verse
        return False

    def __eq__(self, other):
        # equal
        return int(self.page_num) == int(other.page_num) and int(self.surah_num) == int(other.surah_num) and int(self.verse_num) == int(other.verse_num) and int(self.word_num_in_verse) == int(other.word_num_in_verse)

    def __ne__(self, other):
        # not equal
        return not self == other

    def __ge__(self, other):
        # greater or equal
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        # less or equal
        return self.__lt__(other) or self.__eq__(other)

    def __add__(self, other):
        return self.page_num + other.page_num

    def __sub__(self, other):
        return self.page_num - other.page_num

    def __repr__(self):
        return (f"{self.page_num = }\n"
                f"{self.surah_name = }\n"
                f"{self.surah_num = }\n"
                f"{self.verse_num = }\n"
                f"{self.word_num_in_verse = }\n"
                f"{self.word = }")
