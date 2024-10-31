from abc import ABC, abstractmethod


class AbstractSubtextGetter(ABC):
    def __init__(self):
        self.number = None
        self.name = None
        self.result = None

    @abstractmethod
    def find(self, txt):
        pass

    def find_number(self, txt):
        self.find(txt)
        return self.number

    def find_name(self, txt):
        self.find(txt)
        return self.name

    def find_result(self, txt):
        self.find(txt)
        return self.result
