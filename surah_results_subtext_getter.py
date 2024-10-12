import re
from lazy_list_widget import AbstractSubtextGetter


class SurahResultsSubtextGetter(AbstractSubtextGetter):
    ptrn = re.compile(r"(.*)\s+\(#(\d{,3})\):\s+(\d+)")

    def __init__(self):
        super().__init__()

    def find(self, txt):
        matches = self.ptrn.match(txt)
        self.name = matches.group(1)
        self.number = matches.group(2)
        self.result = matches.group(3)
