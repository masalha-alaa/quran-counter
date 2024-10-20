import threading
import traceback
import re
from enum import Enum, auto
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QDialog
from gui.mushaf_view import Ui_MushafViewDialog
from PySide6.QtCore import Qt, QMutex, QTimer
from PySide6.QtGui import QCursor, QIntValidator
from my_data_loader import MyDataLoader
from validators import ArabicOnlyValidator
from span_info_thread import SpanInfo, SpanInfoThread
from cursor_position_info import CursorPositionInfo
from PySide6.QtWidgets import QApplication


class SurahInPage:
    def __init__(self):
        self.surah_name = None
        self.surah_num = None
        self.basmalah = None
        # self.verses = []
        self.start_idx = 0
        self.end_idx = 0
        self.verses_start_idx = 0


class SurahStats:
    def __init__(self):
        self.words_count = 0
        self.letters_count = 0
        self.most_repeated_letter = None


class Page:
    def __init__(self):
        self.surahs: list[SurahInPage] = []

    def clear(self):
        self.surahs.clear()


class SelectionType(Enum):
    NO_SELECTION = 0
    BY_TEXT = auto()
    BY_REF = auto()
    BY_PAGE = auto()


class MyMushafViewDialog(QDialog, Ui_MushafViewDialog):
    FIRST_PAGE = 1
    LAST_PAGE = 604
    FIRST_SURAH = 1
    LAST_SURAH = 114
    MIN_VERSE = 1
    MAX_VERSE = 286
    REMOVE_THREAD_AFTER_MS = 1000
    basmalah = "بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ"
    verse_num_pattern = re.compile(r"\((\d{,3})\)")
    CURRENT_SURAH_STATS_MUTEX = QMutex()
    # CURRENT_SURAH_STATS_MUTEX = threading.Lock()
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self):
        super(MyMushafViewDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowMaximizeButtonHint |
                            Qt.WindowType.WindowMinimizeButtonHint)
        self.df = MyDataLoader.get_data()
        self._current_page = 1
        self._current_surah = 1
        self.page = Page()
        self.selectionStartInfo: CursorPositionInfo | None = None
        self.selectionEndInfo: CursorPositionInfo | None = None
        self.stats_widgets = [self.wordsInSelection,]

        self.running_threads = set()
        self.current_surah_stats = SurahStats()
        self.last_selection_type: None | SelectionType = None
        self.nextPushButton.clicked.connect(self.next_button_clicked)
        self.prevPushButton.clicked.connect(self.prev_button_clicked)
        self.goToPageButton.clicked.connect(self.go_to_page)
        self.goToRefButton.clicked.connect(self.go_to_ref_by_surah_num_and_verse_num)
        self.goToRef_2.clicked.connect(self.go_to_ref_by_surah_name_and_verse_num)
        self.pageInput.returnPressed.connect(self.go_to_ref)
        self.surahNumInput.returnPressed.connect(self.go_to_ref)
        self.verseInput.returnPressed.connect(self.go_to_ref)
        self.surahNameInput.returnPressed.connect(self.go_to_ref)
        self.verseInput_2.returnPressed.connect(self.go_to_ref)
        self.textBrowser.cursorPositionChanged.connect(self.on_cursor_position_changed)
        self.selectionStartButton.clicked.connect(self.selection_start_button_clicked)
        self.selectionEndButton.clicked.connect(self.selection_end_button_clicked)
        self.resetStatsButton.clicked.connect(self.restart_stats_button_clicked)
        self.wawIsAWordCheckbox.stateChanged.connect(self.waw_is_a_word_checkbox_state_changed)
        self.waykaannaTwoWordsCheckbox.stateChanged.connect(self.waykaanna_two_words_checkbox_state_changed)

        self._setup_validators()

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.show_verses_from_page(self._current_page)
        self.last_selection_type = SelectionType.BY_PAGE
        self.clear_results()
        self.clear_selection_info()
        self.get_current_surah_stats()

    def add_thread(self, thread):
        # MyMushafViewDialog.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.add(thread)
        # MyMushafViewDialog.RUNNING_THREADS_MUTEX.unlock()

    def remove_thread(self, thread):
        # MyMushafViewDialog.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.remove(thread)
        # MyMushafViewDialog.RUNNING_THREADS_MUTEX.unlock()

    def get_current_surah_stats(self, clear_current=False):
        if clear_current:
            self.surahLettersNum.setText("")
            self.mostRepeatedLetter.setText("")
            self.surahWordsNum.setText("")
        for surah in self.page.surahs:
            span_thread = SpanInfoThread(surah_name=surah.surah_name,
                                         count_waw_as_a_word=self.wawIsAWordCheckbox.isChecked(),
                                         count_waikaana_as_two_words=self.waykaannaTwoWordsCheckbox.isChecked())
            span_thread.from_text('\n'.join(MyDataLoader.get_surah(surah.surah_num)))
            span_thread.result_ready.connect(self.current_surah_stats_callback)
            self.add_thread(span_thread)
            span_thread.start()

    def current_surah_stats_callback(self, span_info: SpanInfo, caller_thread: SpanInfoThread):
        caller_thread.result_ready.disconnect(self.current_surah_stats_callback)
        QTimer.singleShot(MyMushafViewDialog.REMOVE_THREAD_AFTER_MS, lambda: self.remove_thread(caller_thread))

        MyMushafViewDialog.CURRENT_SURAH_STATS_MUTEX.lock()
        # letters num
        letters_num_new_text = (self.surahLettersNum.text() + ", " + f"{span_info.surah_name}: {span_info.letters_in_selection}").strip(", ")
        letters_num_sorted_results = sorted(letters_num_new_text.split(", "), key=lambda x: MyDataLoader.get_surah_num(x.split(": ")[0]))
        self.surahLettersNum.setText(", ".join(letters_num_sorted_results))

        # most repeated letter
        letter, repetitions = span_info.most_repeated_letter
        most_repeated_letter_new_text = (self.mostRepeatedLetter.text() + ", " + f"{span_info.surah_name}: '{letter}' ({repetitions})").strip(", ")
        most_repeated_letter_sorted_results = sorted(most_repeated_letter_new_text.split(", "), key=lambda x: MyDataLoader.get_surah_num(x.split(": ")[0]))
        self.mostRepeatedLetter.setText(", ".join(most_repeated_letter_sorted_results))

        # surah words num
        surah_words_num_new_text = (self.surahWordsNum.text() + ", " + f"{span_info.surah_name}: {span_info.words_in_selection}").strip(", ")
        surah_words_num_sorted_results = sorted(surah_words_num_new_text.split(", "), key=lambda x: MyDataLoader.get_surah_num(x.split(": ")[0]))
        self.surahWordsNum.setText(", ".join(surah_words_num_sorted_results))
        MyMushafViewDialog.CURRENT_SURAH_STATS_MUTEX.unlock()

    def clear_results(self):
        self.wordsInSelection.setText("0")
        self.surahLettersNum.setText("")
        self.mostRepeatedLetter.setText("")
        self.surahWordsNum.setText("")

    def clear_selection_info(self):
        self.selectionStartLabel.setText("")
        self.selectionEndLabel.setText("")

    def beam_cursor(self):
        self.textBrowser.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))

    # def closeEvent(self, event: QCloseEvent):
    #     self.textBrowser.clear()
    #     event.accept()

    def needsBasmalah(self, surah_num):
        return surah_num not in [1, 9]

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, page_number):
        self._current_page = int(page_number)

    def _setup_validators(self):
        self.pageInput.setValidator(QIntValidator(self.FIRST_PAGE, self.LAST_PAGE, self))
        self.surahNumInput.setValidator(QIntValidator(self.FIRST_SURAH, self.LAST_SURAH, self))
        self.verseInput.setValidator(QIntValidator(self.MIN_VERSE, self.MAX_VERSE, self))
        self.surahNameInput.setValidator(ArabicOnlyValidator())
        self.verseInput_2.setValidator(QIntValidator(self.MIN_VERSE, self.MAX_VERSE, self))

        self.pageInput.textChanged.connect(self.check_page_input)
        self.surahNumInput.textChanged.connect(self.check_surah_num_input)
        self.verseInput.textChanged.connect(self.check_verse_input)
        self.surahNameInput.textChanged.connect(self.check_surah_name_input)
        self.verseInput_2.textChanged.connect(self.check_verse_input)

    def check_page_input(self):
        if not (text := self.pageInput.text()):
            return
        if int(text) > self.LAST_PAGE:
            self.pageInput.setText(str(self.LAST_PAGE))
        if int(text) < self.FIRST_PAGE:
            self.pageInput.setText(str(self.FIRST_PAGE))
        self.surahNumInput.clear()
        self.verseInput.clear()
        self.verseInput_2.clear()
        self.surahNameInput.clear()

    def check_surah_num_input(self):
        if not (text := self.surahNumInput.text()):
            return
        if int(text) > self.LAST_SURAH:
            self.surahNumInput.setText(str(self.LAST_SURAH))
        elif int(text) < self.FIRST_SURAH:
            self.surahNumInput.setText(str(self.FIRST_SURAH))
        if self.verseInput.text():
            self.check_verse_input()

        self.pageInput.clear()
        self.surahNameInput.clear()
        self.verseInput_2.clear()

    def check_verse_input(self):
        if not ((verse_num := self.verseInput.text()) and (surah_num := self.surahNumInput.text())):
            return

        max_verse_in_surah = MyDataLoader.get_num_of_last_verse_in_surah(surah_num)
        if int(verse_num) > max_verse_in_surah:
            self.verseInput.setText(str(max_verse_in_surah))
        elif int(verse_num) < 1:
            self.verseInput.setText(str(self.MIN_VERSE))
        self.pageInput.clear()
        self.surahNameInput.clear()
        self.verseInput_2.clear()

    def check_surah_name_input(self):
        if not (text := self.surahNameInput.text()):
            return
        if self.verseInput_2.text():
            self.check_verse_input_2()
        # if MyDataLoader.get_surah_num(text):
        self.surahNumInput.clear()
        self.verseInput.clear()
        self.pageInput.clear()

    def check_verse_input_2(self):
        if not ((verse_num := self.verseInput_2.text()) and
                (surah_name := self.surahNameInput.text()) and
                (surah_num := MyDataLoader.get_surah_num(surah_name))):
            return

        max_verse_in_surah = MyDataLoader.get_num_of_last_verse_in_surah(surah_num)
        if int(verse_num) > max_verse_in_surah:
            self.verseInput_2.setText(str(max_verse_in_surah))
        elif int(verse_num) < 1:
            self.verseInput_2.setText(str(self.MIN_VERSE))
        self.pageInput.clear()
        self.surahNumInput.clear()
        self.verseInput.clear()

    def show_verses_from_beginning_of_surah(self, surah_num):
        if surah_num:
            page_num = MyDataLoader.get_first_page_of_surah(surah_num)
            self.show_verses_from_page(page_num)
            return page_num
        return None

    def show_verses_from_surah_name(self, surah_name):
        if surah_name:
            surah_num = MyDataLoader.get_surah_num(surah_name)
            return self.show_verses_from_beginning_of_surah(surah_num)
        return None

    def show_verses_from_surah_verse_ref(self, surah_num, verse_num):
        if surah_num and verse_num:
            page_num = MyDataLoader.get_verses_of_surah_verse_ref(surah_num, verse_num)
            self.show_verses_from_page(page_num)
            return page_num
        return None

    def show_verses_from_page(self, page_num):
        self.textBrowser.clear()
        self.pageNumDisplay.setText(str(page_num))

        surahs_nums = []
        current_idx = 0
        self.page.clear()
        for data in MyDataLoader.get_verses_of_page(page_num):
            verses_start_offset = 0
            surah_in_page = SurahInPage()
            surah_num, verses_range, verses = data.surah_num, data.verses_range, data.verses
            has_next = data.has_next
            surahs_nums.append(str(surah_num))
            al_fatiha = surah_num == 1
            al_baqara_first_page = (surah_num == 2) and (verses_range[0] == 1)
            should_center = al_fatiha or al_baqara_first_page or surah_num >= 103
            separator = '<br>' if should_center else ' '
            self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignCenter)
            needs_basmalah = self.needsBasmalah(surah_num) and verses_range[0] == 1
            surah_name = MyDataLoader.get_surah_name(surah_num)
            verses_start_offset += len(surah_name)
            if needs_basmalah:
                self.textBrowser.insertHtml(
                    f"""<h3 style="text-align: center;">{surah_name}</h3><h4 style="text-align: center">{self.basmalah}</h4><br>""")
                # self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignCenter)
                # self.textBrowser.insertHtml(f"""<h3>{self.basmalah}</h3><br>""")
                verses_start_offset += len(self.basmalah)
                verses_start_offset += 3  # +1 new line after title, +2 new lies after basmalah
            else:
                self.textBrowser.insertHtml(
                    f"""<h3 style="text-align: center;">{surah_name}</h3><br>""")
                verses_start_offset += 2  # +2 new lines after title
            if should_center:
                self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignCenter)
            else:
                self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignJustify)
            for i, verse in enumerate(verses):
                verse_display = f"{verse} ({verses_range[0] + i}){separator if i < len(verses) - 1 else ''}"
                self.textBrowser.insertHtml(verse_display)
                # surah_in_page.verses.append(verse_display)
            if has_next:
                self.textBrowser.insertHtml("<br><br>")

            surah_in_page.start_idx = current_idx
            surah_in_page.verses_start_idx = surah_in_page.start_idx + verses_start_offset
            current_idx = len(self.textBrowser.toPlainText())
            surah_in_page.end_idx = current_idx
            surah_in_page.surah_name = surah_name
            surah_in_page.surah_num = surah_num
            surah_in_page.basmalah = needs_basmalah
            self.page.surahs.append(surah_in_page)

        self.textBrowser.verticalScrollBar().setValue(0)
        self.beam_cursor()
        self.surahNumDisplay.setText(", ".join(surahs_nums))

        # print(self.textBrowser.toPlainText())

    def next_button_clicked(self):
        if self._current_page < self.LAST_PAGE:
            prev_surahs = tuple(surah.surah_num for surah in self.page.surahs)
            self._current_page += 1
            self.show_verses_from_page(self._current_page)
            new_surahs = tuple(surah.surah_num for surah in self.page.surahs)
            if prev_surahs != new_surahs:
                self.get_current_surah_stats(clear_current=True)

    def prev_button_clicked(self):
        if self._current_page > self.FIRST_PAGE:
            prev_surahs = tuple(surah.surah_num for surah in self.page.surahs)
            self._current_page -= 1
            self.show_verses_from_page(self._current_page)
            new_surahs = tuple(surah.surah_num for surah in self.page.surahs)
            if prev_surahs != new_surahs:
                self.get_current_surah_stats(clear_current=True)

    def go_to_ref(self):
        # current_focus = QApplication.focusWidget()
        if self.pageInput.text():
            self.go_to_page()
        elif self.verseInput.text() and self.surahNumInput.text():
            self.go_to_ref_by_surah_num_and_verse_num()
        elif self.surahNumInput.text():
            self.go_to_ref_by_surah_num_and_verse_num()
        elif self.verseInput_2.text() and self.surahNameInput.text():
            self.go_to_ref_by_surah_name_and_verse_num()
        elif self.surahNameInput.text():
            self.go_to_ref_by_surah_name_and_verse_num()
        # current_focus.setFocus()  # TODO: not working

    def go_to_page(self):
        if self.pageInput.text():
            prev_surahs = tuple(surah.surah_num for surah in self.page.surahs)
            self.show_verses_from_page(self.pageInput.text())
            self.current_page = self.pageInput.text()
            new_surahs = tuple(surah.surah_num for surah in self.page.surahs)
            if prev_surahs != new_surahs:
                self.last_selection_type = SelectionType.BY_PAGE
                self.get_current_surah_stats(clear_current=True)

    def go_to_ref_by_surah_num_and_verse_num(self):
        prev_surahs = tuple(surah.surah_num for surah in self.page.surahs)
        if self.verseInput.text() and self.surahNumInput.text():
            self.current_page = self.show_verses_from_surah_verse_ref(self.surahNumInput.text(), self.verseInput.text())
        elif self.surahNumInput.text():
            page_num = self.show_verses_from_beginning_of_surah(self.surahNumInput.text())
            self.current_page = page_num
        new_surahs = tuple(surah.surah_num for surah in self.page.surahs)
        if prev_surahs != new_surahs:
            self.last_selection_type = SelectionType.BY_PAGE
            self.get_current_surah_stats(clear_current=True)

    def go_to_ref_by_surah_name_and_verse_num(self):
        prev_surahs = tuple(surah.surah_num for surah in self.page.surahs)
        surah_num = MyDataLoader.get_surah_num(self.surahNameInput.text())
        if self.verseInput_2.text() and self.surahNameInput.text():
            self.current_page = self.show_verses_from_surah_verse_ref(surah_num, self.verseInput_2.text())
        elif self.surahNameInput.text():
            page_num = self.show_verses_from_beginning_of_surah(surah_num)
            self.current_page = page_num
        new_surahs = tuple(surah.surah_num for surah in self.page.surahs)
        if prev_surahs != new_surahs:
            self.last_selection_type = SelectionType.BY_PAGE
            self.get_current_surah_stats(clear_current=True)

    def valid_selection(self):
        cursor = self.textBrowser.textCursor()
        span = (cursor.selectionStart(), cursor.selectionEnd())
        return span[0] != span[1]

    def on_cursor_position_changed(self):
        if self.valid_selection():
            # print(span)
            # TODO: Not sure a thread is needed here but ok
            # TODO: Need to verify threads finish in the right order!
            self.start_span_info_thread(SelectionType.BY_TEXT)
        # else:
        #     self.clear_results()

    def span_info_completed(self, span_info: SpanInfo, caller_thread: SpanInfoThread):
        caller_thread.result_ready.disconnect(self.span_info_completed)
        QTimer.singleShot(MyMushafViewDialog.REMOVE_THREAD_AFTER_MS, lambda: self.remove_thread(caller_thread))
        self.wordsInSelection.setText(str(span_info.words_in_selection))
        # print(f"{count.words_in_selection = }")

    def selection_start_button_clicked(self):
        self.selectionStartInfo = self.get_selection_info()
        if self.selectionStartInfo is not None:
            if self.selectionEndInfo is not None and self.selectionStartInfo >= self.selectionEndInfo:
                self.selectionEndInfo = None
                self.selectionEndLabel.clear()
            surah_name, verse_num, word = self.selectionStartInfo.surah_name, self.selectionStartInfo.verse_num, self.selectionStartInfo.word
            aya = "اية"
            self.selectionStartLabel.setText(f"[{surah_name} - {aya} {verse_num} - {word}]")
            if self.selectionEndInfo is not None and self.selectionStartInfo < self.selectionEndInfo:
                self.start_span_info_thread(SelectionType.BY_REF)
        self.textBrowser.setFocus()
        self.beam_cursor()

    def selection_end_button_clicked(self):
        self.selectionEndInfo = self.get_selection_info()
        if self.selectionEndInfo is not None:
            if self.selectionStartInfo is not None and self.selectionEndInfo <= self.selectionStartInfo:
                self.selectionStartInfo = None
                self.selectionStartLabel.clear()
            surah_name, verse_num, word = self.selectionEndInfo.surah_name, self.selectionEndInfo.verse_num, self.selectionEndInfo.word
            aya = "اية"
            self.selectionEndLabel.setText(f"[{surah_name} - {aya} {verse_num} - {word}]")
            if self.selectionStartInfo is not None and self.selectionEndInfo > self.selectionStartInfo:
                self.start_span_info_thread(SelectionType.BY_REF)

        self.textBrowser.setFocus()
        self.beam_cursor()

    def valid_selection_span(self):
        if self.selectionStartInfo is None or self.selectionEndInfo is None:
            return False
        if self.selectionStartInfo < self.selectionEndInfo:
            return True
        return False

    def start_span_info_thread(self, selection_type: SelectionType):
        self.last_selection_type = selection_type
        span_thread = SpanInfoThread(count_waw_as_a_word=self.wawIsAWordCheckbox.isChecked(),
                                     count_waikaana_as_two_words=self.waykaannaTwoWordsCheckbox.isChecked())
        if selection_type == SelectionType.BY_TEXT:
            span_thread.from_text(self.textBrowser.textCursor().selection().toPlainText())
        elif selection_type == SelectionType.BY_REF:
            span_thread.from_ref(self.selectionStartInfo, self.selectionEndInfo)
        else:
            return
        span_thread.result_ready.connect(self.span_info_completed)
        self.add_thread(span_thread)
        span_thread.start()

    def get_selection_info(self, snap_to_beginning_of_word=True) -> CursorPositionInfo | None:
        selection_start, selection_end = self.textBrowser.textCursor().selectionStart(), self.textBrowser.textCursor().selectionEnd()
        if selection_end > selection_start:
            selection_start_info = self.get_info_of_cursor_position(selection_start, snap_to_beginning_of_word=snap_to_beginning_of_word)
            # print(selection_start_info)
            return selection_start_info if selection_start_info.is_valid() else None
        return None

    def get_info_of_cursor_position(self, cursor_position: int, snap_to_beginning_of_word=True) -> CursorPositionInfo:
        text = self.textBrowser.toPlainText()

        cursor_position_info = CursorPositionInfo()
        while (current_char := text[cursor_position:cursor_position + 1]).isspace():
            cursor_position += 1
            if cursor_position >= len(text):
                return cursor_position_info
        if current_char == "(":  # looks like in arabic it's automatically reversed, so this is the opening bracket
            cursor_position += 3
        elif current_char == ")":  # looks like in arabic it's automatically reversed, so this is the closing bracket
            cursor_position += 1
        elif current_char.isdigit():
            cursor_position += 2

        for surah in self.page.surahs:
            if surah.verses_start_idx <= cursor_position < surah.end_idx:
                cursor_position_info.surah_name = surah.surah_name
                cursor_position_info.surah_num = int(MyDataLoader.get_surah_num(surah.surah_name))
                cursor_position_info.page_num = self.current_page

                # search verse num after cursor position
                my_verse_num = self.verse_num_pattern.search(text[cursor_position:]).group(1)
                # search prev verse num (last one before cursor position)
                try:
                    *_, prev_verse_idx_match = self.verse_num_pattern.finditer(text[:cursor_position])
                    prev_verse_idx_span = prev_verse_idx_match.span()[1]
                except ValueError:
                    prev_verse_idx_span = list(re.finditer(r"\n", text[:cursor_position]))[-1].span()[0]
                # count spaces to know place of current word
                # current_word_num = text.count(" ", prev_verse_idx_span + 1, cursor_position)
                spaces_before = list(re.finditer(r"\s", text[prev_verse_idx_span + 1:cursor_position]))
                current_word_num = len(spaces_before)
                if snap_to_beginning_of_word:
                    last_space = spaces_before[-1].span()[1] if spaces_before else 0
                    cursor_position = prev_verse_idx_span + 1 + last_space
                cursor_position_info.word_num_in_verse = current_word_num
                cursor_position_info.verse_num = int(my_verse_num)
                # get word / part of word between cursor and next space
                next_space_idx = text.find(" ", cursor_position + 1)
                cursor_position_info.word = text[cursor_position:next_space_idx].strip()
                break
        return cursor_position_info

    def waw_is_a_word_checkbox_state_changed(self, state):
        if self.last_selection_type == SelectionType.NO_SELECTION:
            return
        if self.last_selection_type == SelectionType.BY_PAGE:
            self.get_current_surah_stats(clear_current=True)
        if self.valid_selection() or self.valid_selection_span():
            self.start_span_info_thread(self.last_selection_type)

    def waykaanna_two_words_checkbox_state_changed(self, state):
        if self.last_selection_type == SelectionType.NO_SELECTION:
            return
        if self.last_selection_type == SelectionType.BY_PAGE:
            self.get_current_surah_stats(clear_current=True)
        if self.valid_selection() or self.valid_selection_span():
            self.start_span_info_thread(self.last_selection_type)

    def restart_stats_button_clicked(self):
        for widget in self.stats_widgets:
            widget.setText("0")
