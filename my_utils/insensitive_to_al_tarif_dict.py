class InsensitiveToAlTarifDict(dict):

    def __setitem__(self, key:str, value):
        key = key[2:] if key.startswith("ال") else key
        super().__setitem__(key, value)

    def __getitem__(self, key):
        key = key[2:] if key.startswith("ال") else key
        return super().__getitem__(key)

    def __delitem__(self, key):
        key = key[2:] if key.startswith("ال") else key
        super().__delitem__(key)

    def __contains__(self, key):
        key = key[2:] if key.startswith("ال") else key
        return super().__contains__(key)

    def get(self, key, default=None):
        key = key[2:] if key.startswith("ال") else key
        return super().get(key, default)

    def update(self, other=(), **kwargs):
        for key, value in dict(other, **kwargs).items():
            key = key[2:] if key.startswith("ال") else key
            self[key] = value


if __name__ == '__main__':
    # TEST
    w1 = "كهف"
    w2 = "الكهف"
    w3 = "كوثر"
    w4 = "الكوثر"
    d = InsensitiveToAlTarifDict()
    d[w1] = d.get(w1, 0) + 1
    d[w2] = d.get(w2, 0) + 1
    d[w3] = d.get(w3, 0) + 1
    d[w4] = d.get(w4, 0) + 1
    print(d)  # {'كهف': 2, 'كوثر': 2}
