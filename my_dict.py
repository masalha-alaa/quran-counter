from arabic_reformer import diacritics_ending_regex_compiled


class MyDict(dict):

    def _strip_last_diacritic(self, key):
        return diacritics_ending_regex_compiled.sub("", key)

    def __setitem__(self, key, value):
        key = self._strip_last_diacritic(key)
        super().__setitem__(key, value)

    def __getitem__(self, key):
        key = self._strip_last_diacritic(key)
        return super().__getitem__(key)

    def __delitem__(self, key):
        key = self._strip_last_diacritic(key)
        super().__delitem__(key)

    def __contains__(self, key):
        key = self._strip_last_diacritic(key)
        return super().__contains__(key)

    def get(self, key, default=None):
        key = self._strip_last_diacritic(key)
        return super().get(key, default)

    def update(self, other=(), **kwargs):
        for key, value in dict(other, **kwargs).items():
            key = self._strip_last_diacritic(key)
            self[key] = value


if __name__ == '__main__':
    # TEST
    w1 = "جَنَّةٌ"
    w2 = "جَنَّةٍ"
    w3 = "مَدَّ"
    w4 = "مَدٌّ"
    d = MyDict()
    d[w1] = d.get(w1, 0) + 1
    d[w2] = d.get(w2, 0) + 1
    d[w3] = d.get(w3, 0) + 1
    d[w4] = d.get(w4, 0) + 1
    print(d)  # {'جَنَّة': 2, 'مَد': 2}
