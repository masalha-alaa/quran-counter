from arabic_reformer import strip_last_diacritic


class InsensitiveToLastDiacriticDict(dict):

    def __setitem__(self, key, value):
        key = strip_last_diacritic(key)
        super().__setitem__(key, value)

    def __getitem__(self, key):
        key = strip_last_diacritic(key)
        return super().__getitem__(key)

    def __delitem__(self, key):
        key = strip_last_diacritic(key)
        super().__delitem__(key)

    def __contains__(self, key):
        key = strip_last_diacritic(key)
        return super().__contains__(key)

    def get(self, key, default=None):
        key = strip_last_diacritic(key)
        return super().get(key, default)

    def update(self, other=(), **kwargs):
        for key, value in dict(other, **kwargs).items():
            key = strip_last_diacritic(key)
            self[key] = value


if __name__ == '__main__':
    # TEST
    w1 = "جَنَّةٌ"
    w2 = "جَنَّةٍ"
    w3 = "مَدَّ"
    w4 = "مَدٌّ"
    d = InsensitiveToLastDiacriticDict()
    d[w1] = d.get(w1, 0) + 1
    d[w2] = d.get(w2, 0) + 1
    d[w3] = d.get(w3, 0) + 1
    d[w4] = d.get(w4, 0) + 1
    print(d)  # {'جَنَّة': 2, 'مَد': 2}
