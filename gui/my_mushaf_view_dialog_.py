from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QDialog
from gui.mushaf_view import Ui_MushafViewDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QIntValidator
from my_data_loader import MyDataLoader
from validators import ArabicOnlyValidator


class MyMushafViewDialog(QDialog, Ui_MushafViewDialog):
    FIRST_PAGE = 1
    LAST_PAGE = 604
    FIRST_SURAH = 1
    LAST_SURAH = 114
    MIN_VERSE = 1
    MAX_VERSE = 286
    basmalah = "بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ"

    def __init__(self):
        super(MyMushafViewDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowMaximizeButtonHint |
                            Qt.WindowType.WindowMinimizeButtonHint)
        self.df = MyDataLoader.get_data()
        self._working_col = MyDataLoader.get_working_col()
        self._current_page = 1
        self._current_surah = 1
        self.nextPushButton.clicked.connect(self.next_button_clicked)
        self.prevPushButton.clicked.connect(self.prev_button_clicked)
        self.goToPageButton.clicked.connect(self.go_to_page)
        self.goToRefButton.clicked.connect(self.go_to_surah_verse)
        self.goToSurahNameButton.clicked.connect(self.go_to_surah_name)
        self.pageInput.returnPressed.connect(self.go_to_ref)
        self.surahNumInput.returnPressed.connect(self.go_to_ref)
        self.surahNameInput.returnPressed.connect(self.go_to_ref)
        self.verseInput.returnPressed.connect(self.go_to_ref)
        self._setup_validators()

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.show_verses_from_page(self._current_page)

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
        for data in MyDataLoader.get_verses_of_page(page_num):
            surah_num, verses_range, verses = data.surah_num, data.verses_range, data.verses
            has_next = data.has_next
            surahs_nums.append(str(surah_num))
            al_fatiha = surah_num == 1
            al_baqara_first_page = (surah_num == 2) and (verses_range[0] == 1)
            should_center = al_fatiha or al_baqara_first_page
            separator = '<br>' if should_center else ' '
            self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if self.needsBasmalah(surah_num) and verses_range[0] == 1:
                self.textBrowser.insertHtml(
                    f"""<h2 style="text-align: center; line-height: 0.7">{MyDataLoader.get_surah_name(surah_num)}</h2>\n<h3 style="text-align: center">{self.basmalah}</h3><br>""")
                # self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignCenter)
                # self.textBrowser.insertHtml(f"""<h3>{self.basmalah}</h3><br>""")
            else:
                self.textBrowser.insertHtml(
                    f"""<h2 style="text-align: center;">{MyDataLoader.get_surah_name(surah_num)}</h2><br>""")
            if should_center:
                self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignCenter)
            else:
                self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignJustify)
            for i, verse in enumerate(verses):
                self.textBrowser.insertHtml(f"{verse} ({verses_range[0] + i}){separator if i < len(verses) - 1 else ''}")
            if has_next:
                self.textBrowser.insertHtml("<br><br>")

        self.textBrowser.verticalScrollBar().setValue(0)
        self.textBrowser.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.surahNumDisplay.setText(", ".join(surahs_nums))

    def next_button_clicked(self):
        if self._current_page < self.LAST_PAGE:
            self._current_page += 1
            self.show_verses_from_page(self._current_page)

    def prev_button_clicked(self):
        if self._current_page > self.FIRST_PAGE:
            self._current_page -= 1
            self.show_verses_from_page(self._current_page)

    def go_to_ref(self):
        if self.pageInput.text():
            self.go_to_page()
        elif self.verseInput.text() and self.surahNumInput.text():
            self.go_to_surah_verse()
        elif self.surahNumInput.text():
            self.go_to_surah_verse()
        elif self.surahNameInput.text():
            self.go_to_surah_name()

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

    # def closeEvent(self, event: QCloseEvent):
    #     self.textBrowser.clear()
    #     event.accept()
