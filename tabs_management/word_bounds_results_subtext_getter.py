import re
from my_widgets.lazy_list_widget import AbstractSubtextGetter


class WordBoundsResultsSubtextGetter(AbstractSubtextGetter):
    ptrn = re.compile(r"(.*):\s+(\d+)")

    def __init__(self):
        super().__init__()

    def find(self, txt):
        matches = self.ptrn.match(txt)
        self.number = None
        self.name = matches.group(1)
        self.result = matches.group(2)
