import re
from enum import Enum, auto
import json
from PySide6.QtCore import Signal, QThread


class AskGptThread(QThread):
    class Command(Enum):
        NONE = auto()
        GET_MEANINGS = auto()
        GET_RELEVANT_VERSES = auto()

    # Signal to send the result of the task back to the main thread
    meanings_result_ready = Signal(tuple, QThread)
    relevant_verses_result_ready = Signal(list, QThread)

    def __init__(self, disambiguator):
        super().__init__()
        self.disambiguator = disambiguator
        self.command = AskGptThread.Command.NONE
        self.word = None
        self.meaning = None
        self.verses = None
        self.language = None

    def _reset_input(self):
        self.word = None
        self.verses = None
        self.meaning = None

    def set_command_get_meanings(self, word, language):
        self.language = language
        self.word = word
        self.command = AskGptThread.Command.GET_MEANINGS

    def set_command_get_relevant_verses(self, word, verses, meaning):
        self.word = word
        self.verses = verses
        self.meaning = meaning
        self.command = AskGptThread.Command.GET_RELEVANT_VERSES

    def _ask_gpt_for_relevant_verses(self):
        # sorted verses_ref for caching purposes
        # TODO:
        # match == surah_num, verse_num, verse, spans, other
        verse_refs = []
        verses = []
        for surah_num, verse_num, verse, _, _ in self.verses:
            verse_refs.append(f"{surah_num}:{verse_num}")
            verses.append(verse)
        verse_refs = tuple(sorted(verse_refs))
        relevant_verses = self.disambiguator.get_relevant_verses(self.word, self.meaning, verse_refs, verses)
        return relevant_verses

    def _ask_gpt_for_meanings(self):
        # TODO: Exception handling
        success, data = self.disambiguator.get_chatgpt_response(self.word, self.language)
        return success, json.loads(data) if success else data

    def run(self):
        match self.command:
            case AskGptThread.Command.GET_MEANINGS:
                results = self._ask_gpt_for_meanings()
                self.meanings_result_ready.emit(results, self)
            case AskGptThread.Command.GET_RELEVANT_VERSES:
                results = self._ask_gpt_for_relevant_verses()
                self.relevant_verses_result_ready.emit(results, self)
