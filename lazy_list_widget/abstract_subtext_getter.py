from abc import ABC, abstractmethod


class AbstractSubtextGetter(ABC):
    def __init__(self):
        self.number = None
        self.name = None
        self.result = None

    @abstractmethod
    def find(self, txt):
        pass
