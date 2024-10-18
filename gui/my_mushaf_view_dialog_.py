import re
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QDialog
from gui.mushaf_view import Ui_MushafViewDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QIntValidator
from my_data_loader import MyDataLoader
from validators import ArabicOnlyValidator
from span_info_thread import SpanInfo, SpanInfoThread
from cursor_position_info import CursorPositionInfo
from PySide6.QtWidgets import QApplication


class SurahInPage:
    def __init__(self):
        self.surah_name = None
        self.basmalah = None
        # self.verses = []
        self.start_idx = 0
        self.end_idx = 0
        self.verses_start_idx = 0


class Page:
    def __init__(self):
        self.surahs: list[SurahInPage] = []

    def clear(self):
        self.surahs.clear()


class MyMushafViewDialog(QDialog, Ui_MushafViewDialog):
    FIRST_PAGE = 1
    LAST_PAGE = 604
    FIRST_SURAH = 1
    LAST_SURAH = 114
    MIN_VERSE = 1
    MAX_VERSE = 286
    basmalah = "بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ"
    verse_num_pattern = re.compile(r"\((\d{,3})\)")

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

        self.running_threads = set()
        self.nextPushButton.clicked.connect(self.next_button_clicked)
        self.prevPushButton.clicked.connect(self.prev_button_clicked)
        self.goToPageButton.clicked.connect(self.go_to_page)
        self.goToRefButton.clicked.connect(self.go_to_surah_verse)
        self.goToSurahNameButton.clicked.connect(self.go_to_surah_name)
        self.pageInput.returnPressed.connect(self.go_to_ref)
        self.surahNumInput.returnPressed.connect(self.go_to_ref)
        self.surahNameInput.returnPressed.connect(self.go_to_ref)
        self.verseInput.returnPressed.connect(self.go_to_ref)
        self.textBrowser.cursorPositionChanged.connect(self.on_cursor_position_changed)
        self.selectionStartButton.clicked.connect(self.selection_start_button_clicked)
        self.selectionEndButton.clicked.connect(self.selection_end_button_clicked)
        self._setup_validators()

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.show_verses_from_page(self._current_page)
        self.clear_results()
        self.clear_selection_info()

    def clear_results(self):
        self.wordsInSelection.setText("0")
        self.wordsFromBeginOfSurah.setText("0")
        self.wordsFromBeginOfMushaf.setText("0")
        self.lettersInSelection.setText("0")
        self.lettersFromBeginOfSurah.setText("0")
        self.lettersFromBeginOfMushaf.setText("0")

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

        self.pageInput.textChanged.connect(self.check_page_input)
        self.surahNumInput.textChanged.connect(self.check_surah_num_input)
        self.verseInput.textChanged.connect(self.check_verse_input)
        self.surahNameInput.textChanged.connect(self.check_surah_name_input)

    def check_page_input(self):
        if not (text := self.pageInput.text()):
            return
        if int(text) > self.LAST_PAGE:
            self.pageInput.setText(str(self.LAST_PAGE))
        if int(text) < self.FIRST_PAGE:
            self.pageInput.setText(str(self.FIRST_PAGE))
        self.surahNumInput.clear()
        self.verseInput.clear()
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

    def check_surah_name_input(self):
        if not (text := self.surahNameInput.text()):
            return
        # if MyDataLoader.get_surah_num(text):
        self.surahNumInput.clear()
        self.verseInput.clear()
        self.pageInput.clear()

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
            should_center = al_fatiha or al_baqara_first_page
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
            surah_in_page.basmalah = needs_basmalah
            self.page.surahs.append(surah_in_page)

        self.textBrowser.verticalScrollBar().setValue(0)
        self.beam_cursor()
        self.surahNumDisplay.setText(", ".join(surahs_nums))

        # print(self.textBrowser.toPlainText())

    def next_button_clicked(self):
        if self._current_page < self.LAST_PAGE:
            self._current_page += 1
            self.show_verses_from_page(self._current_page)

    def prev_button_clicked(self):
        if self._current_page > self.FIRST_PAGE:
            self._current_page -= 1
            self.show_verses_from_page(self._current_page)

    def go_to_ref(self):
        # current_focus = QApplication.focusWidget()
        if self.pageInput.text():
            self.go_to_page()
        elif self.verseInput.text() and self.surahNumInput.text():
            self.go_to_surah_verse()
        elif self.surahNumInput.text():
            self.go_to_surah_verse()
        elif self.surahNameInput.text():
            self.go_to_surah_name()
        # current_focus.setFocus()  # TODO: not working

    def go_to_page(self):
        if self.pageInput.text():
            self.show_verses_from_page(self.pageInput.text())
            self.current_page = self.pageInput.text()

    def go_to_surah_verse(self):
        if self.verseInput.text() and self.surahNumInput.text():
            self.current_page = self.show_verses_from_surah_verse_ref(self.surahNumInput.text(), self.verseInput.text())
        elif self.surahNumInput.text():
            page_num = self.show_verses_from_beginning_of_surah(self.surahNumInput.text())
            self.current_page = page_num

    def go_to_surah_name(self):
        if self.surahNameInput.text():
            if (page := self.show_verses_from_surah_name(self.surahNameInput.text())) is not None:
                self.current_page = page

    def on_cursor_position_changed(self):
        cursor = self.textBrowser.textCursor()
        span = (cursor.selectionStart(), cursor.selectionEnd())
        # print(span)
        if span[0] != span[1]:
            # print(span)
            # TODO: Not sure a thread is needed here but ok
            # TODO: Need to verify threads finish in the right order!

            span_thread = SpanInfoThread()
            span_thread.from_text(cursor.selection().toPlainText())
            span_thread.result_ready.connect(self.span_info_completed)
            self.running_threads.add(span_thread)
            span_thread.start()
        # else:
        #     self.clear_results()

    def span_info_completed(self, span_info: SpanInfo, caller_thread: SpanInfoThread):
        caller_thread.result_ready.disconnect(self.span_info_completed)
        self.running_threads.remove(caller_thread)
        self.wordsInSelection.setText(str(span_info.words_in_selection))
        self.lettersInSelection.setText(str(span_info.letters_in_selection))
        # print(f"{count.words_in_selection = }")

    def selection_start_button_clicked(self):
        self.selectionStartInfo = self.get_selection_info()
        if self.selectionStartInfo is not None:
            if self.selectionEndInfo is not None and self.selectionStartInfo >= self.selectionEndInfo:
                self.selectionEndInfo.clear()
                self.selectionEndLabel.clear()
            surah_name, verse_num, word = self.selectionStartInfo.surah_name, self.selectionStartInfo.verse_num, self.selectionStartInfo.word
            aya = "اية"
            self.selectionStartLabel.setText(f"[{surah_name} - {aya} {verse_num} - {word}]")
        self.textBrowser.setFocus()
        self.beam_cursor()

    def selection_end_button_clicked(self):
        self.selectionEndInfo = self.get_selection_info()
        if self.selectionEndInfo is not None:
            if self.selectionStartInfo is not None and self.selectionEndInfo <= self.selectionStartInfo:
                self.selectionStartInfo.clear()
                self.selectionStartLabel.clear()
            surah_name, verse_num, word = self.selectionEndInfo.surah_name, self.selectionEndInfo.verse_num, self.selectionEndInfo.word
            aya = "اية"
            self.selectionEndLabel.setText(f"[{surah_name} - {aya} {verse_num} - {word}]")

            span_thread = SpanInfoThread()
            span_thread.from_ref(self.selectionStartInfo, self.selectionEndInfo)
            span_thread.result_ready.connect(self.span_info_completed)
            self.running_threads.add(span_thread)
            span_thread.start()

        self.textBrowser.setFocus()
        self.beam_cursor()

    def get_selection_info(self) -> CursorPositionInfo | None:
        selection_start, selection_end = self.textBrowser.textCursor().selectionStart(), self.textBrowser.textCursor().selectionEnd()
        if selection_end > selection_start:
            selection_start_info = self.get_info_of_cursor_position(selection_start)
            # print(selection_start_info)
            return selection_start_info if selection_start_info.is_valid() else None
        return None

    def get_info_of_cursor_position(self, cursor_position: int) -> CursorPositionInfo:
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
                    prev_verse_idx_span = -1
                # count spaces to know place of current word
                current_word_num = text.count(" ", prev_verse_idx_span + 1, cursor_position)
                cursor_position_info.word_num_in_verse = current_word_num
                cursor_position_info.verse_num = int(my_verse_num)
                # get word / part of word between cursor and next space
                next_space_idx = text.find(" ", cursor_position + 1)
                cursor_position_info.word = text[cursor_position:next_space_idx].strip()
                break
        return cursor_position_info

