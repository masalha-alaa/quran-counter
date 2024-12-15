from typing import List, Iterator
from PySide6.QtWidgets import QTextBrowser
from my_utils.emphasizer import emphasize_span, CssColors
from arabic_reformer import reform_text
from models.match_item import MatchItem


class LazyTextBrowser(QTextBrowser):
    _exhausted = object()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._items_num_to_load = 20
        self._colorize = False

        self._prev_scrolling_value = 0
        self._adding_items = False
        self._filtered_matches_iter: Iterator[MatchItem] = None
        self._filtered_matches_idx = []
        self.verticalScrollBar().actionTriggered.connect(self.before_scroll)
        self.verticalScrollBar().valueChanged.connect(self.after_scroll)

    def set_colorize(self, colorize: bool):
        self._colorize = colorize

    def set_items_num_to_load(self, items_num_to_load):
        self._items_num_to_load = items_num_to_load

    def before_scroll(self):
        scrollbar = self.verticalScrollBar()
        self._prev_scrolling_value = scrollbar.value()

    def after_scroll(self):
        if self._adding_items or ((scrollbar := self.verticalScrollBar()).value() < self._prev_scrolling_value):
            return "break"
        current_val = scrollbar.value()
        # print(f"{scrollbar.value()}/{scrollbar.maximum()}")
        if scrollbar.value() > 0.85 * scrollbar.maximum():  # At the bottom
            self.load_more_items(self._items_num_to_load)
            scrollbar.setValue(min(scrollbar.maximum(), current_val))

    # def update_filtered_matches_idx(self, matches_idx):
    #     # Deprecated
    #     self._filtered_matches_idx = matches_idx

    def save_values_and_refresh(self, all_matches, matches_idx: list | range, colorize: bool | None = None):
        if colorize is not None:
            self._colorize = colorize
        self._filtered_matches_idx = matches_idx
        filtered_matches: List[MatchItem] = []
        surahs = set()
        matches_num = 0
        for idx in self._filtered_matches_idx:
            filtered_matches.append(all_matches[idx])
            match_item = all_matches[idx]
            surahs.add(match_item.surah_num)
            matches_num += len(match_item.spans)

        self._filtered_matches_iter = iter(filtered_matches)
        self.clear()
        if self._filtered_matches_idx:
            self.load_more_items(self._items_num_to_load, prevent_scrolling=True, colorize=colorize)

        matched_verses_num = str(len(self._filtered_matches_idx))
        return matches_num, matched_verses_num, len(surahs)

    def reset_iter_and_refresh(self, all_matches, colorize: bool | None = None):
        if colorize is not None:
            self._colorize = colorize
        self._filtered_matches_iter = iter([all_matches[idx] for idx in self._filtered_matches_idx])
        self.clear()
        if self._filtered_matches_idx:
            self.load_more_items(self._items_num_to_load, prevent_scrolling=True, colorize=colorize)

    def load_more_items(self, items_to_load=None, prevent_scrolling=False, colorize: bool | None = None):
        def _done():
            if prevent_scrolling:
                scrollbar.setValue(current_scroll_value)
            self._adding_items = False
            return

        self._adding_items = True
        if colorize is None:
            colorize = self._colorize
        if items_to_load is None:
            items_to_load = self._items_num_to_load
        scrollbar = self.verticalScrollBar()
        current_scroll_value = scrollbar.value()
        for _ in range(items_to_load):
            if (match_item := next(self._filtered_matches_iter, LazyTextBrowser._exhausted)) is LazyTextBrowser._exhausted:
                return _done()
            surah_num, verse_num, verse, spans = match_item.surah_num, match_item.verse_num, match_item.verse_text, match_item.spans
            ref = f"{surah_num}:{verse_num}"
            if colorize:
                verse = self.reform_and_color(verse, spans)
            line = f"<p>{ref}: {verse}</p>"
            # line = f"{ref}: {verse}"
            self.append(line)

        return _done()

    def reform_and_color(self, verse, spans):
        verse = reform_text(verse, text_may_contain_diacritics=True)
        # TODO: maybe reform only span +-? See reformer.reform_span() -- didn't work so good
        # verse = self.reformer.reform_span(verse, spans, text_may_contain_diacritics=True)
        verse = emphasize_span(verse, spans, capitalize=False, underline=False, color=CssColors.CYAN, css=True)
        return verse
