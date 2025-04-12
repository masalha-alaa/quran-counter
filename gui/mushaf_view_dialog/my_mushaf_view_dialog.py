import re
from json import load
from datetime import datetime
from enum import Enum, auto
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QDialog
from gui.mushaf_view_dialog.mushaf_view import Ui_MushafViewDialog
from my_widgets.spinning_loader import SpinningLoader
from PySide6.QtCore import Qt, QMutex, QTimer
from PySide6.QtGui import QCursor, QIntValidator, QPixmap
from my_utils.my_data_loader import MyDataLoader
from text_validators.arabic_only_validator import ArabicOnlyValidator
from worker_threads.span_info_thread import SpanInfo, SpanInfoThread
from models.cursor_position_info import CursorPositionInfo
from my_utils.utils import AppLang, translate_text, resource_path


class SurahInPage:
    def __init__(self):
        self.surah_name = None
        self.surah_num = None
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


class SelectionType(Enum):
    NO_SELECTION = 0
    BY_TEXT = auto()
    BY_REF = auto()
    BY_PAGE = auto()


class MySpanInfoMetaData:
    def __init__(self, surah_id=0, total_surahs=0, get_exclusive=False):
        self.current_surah_id = surah_id
        self.total_surahs_in_page = total_surahs
        self.get_exclusive = get_exclusive


class MyMushafViewDialog(QDialog, Ui_MushafViewDialog):
    FIRST_PAGE = 1
    LAST_PAGE = 604
    FIRST_SURAH = 1
    LAST_SURAH = 114
    MIN_VERSE = 1
    MAX_VERSE = 286
    FIRST_JUZ = 1
    LAST_JUZ = 30
    REMOVE_THREAD_AFTER_MS = 500
    MIN_PAGES_FOR_WAITING = 100
    basmalah = "بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ"
    verse_num_pattern = re.compile(r"\((\d{,3})\)")
    CURRENT_SURAH_STATS_MUTEX = QMutex()
    # CURRENT_SURAH_STATS_MUTEX = threading.Lock()
    # RUNNING_THREADS_MUTEX = QMutex()

    def __init__(self, language: None | AppLang):
        super(MyMushafViewDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowMaximizeButtonHint |
                            Qt.WindowType.WindowMinimizeButtonHint)
        self._current_lang = None
        self._apply_language(language)
        self.spinner = SpinningLoader()
        self.df = MyDataLoader.get_data()
        self._current_page = 1
        self._current_surah = 1
        self.page = Page()
        self.selectionStartInfo: CursorPositionInfo | None = None
        self.selectionEndInfo: CursorPositionInfo | None = None
        # self.stats_widgets = [self.wordsInSelection,]
        self.stats_widgets = []

        self.running_threads = set()
        self._thread_id = -1
        self._last_thread_id = -1
        self.last_selection_type: None | SelectionType = None
        self.nextPushButton.clicked.connect(self.next_button_clicked)
        self.prevPushButton.clicked.connect(self.prev_button_clicked)
        self.nextSurahButton.clicked.connect(self.next_surah_button_clicked)
        self.prevSurahButton.clicked.connect(self.prev_surah_button_clicked)
        self.nextJuzButton.clicked.connect(self.next_juz_button_clicked)
        self.prevJuzButton.clicked.connect(self.prev_juz_button_clicked)
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
        self.lettersHistogram.itemSelectionChanged.connect(self.letters_histogram_selection_changed)

        self.exclusive_words_uni = None
        self.exclusive_words_uni_diff_roots = None
        self.exclusive_words_bi = None
        self.exclusive_words_tri = None
        self.resetStatsButton.clicked.connect(self.restart_stats_button_clicked)
        self.selectionResetButton.clicked.connect(self.restart_stats_button_clicked)
        self.refreshExclusiveWordsButton.clicked.connect(self.refresh_exclusive_words_buton_clicked)
        self.wawIsAWordCheckbox.stateChanged.connect(self.waw_is_a_word_checkbox_state_changed)
        self.waykaannaTwoWordsCheckbox.stateChanged.connect(self.waykaanna_two_words_checkbox_state_changed)
        self.huroofMaaniCheckbox.stateChanged.connect(self.huroof_maani_checkbox_state_changed)
        self.differentRootCheckBox.stateChanged.connect(self.diff_roots_checkbox_state_changed)

        self._setup_validators()

    def set_language(self, lang):
        self._apply_language(lang)

    def _apply_language(self, lang):
        if lang != self._current_lang:
            self.retranslateUi(self)
            # self.set_font_for_language(lang)
            self._current_lang = lang

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.show_verses_from_page(self._current_page)
        self.last_selection_type = SelectionType.BY_PAGE
        self.align_titles(self._current_lang)
        self.clear_results()
        self.clear_selection_info()
        self.get_current_surah_stats()
        self.load_exclusive_words_data()

    def closeEvent(self, event):
        self.exclusive_words_uni = None
        self.exclusive_words_uni_diff_roots = None
        self.exclusive_words_bi = None
        self.exclusive_words_tri = None
        self.accept()

    def add_thread(self, thread):
        # MyMushafViewDialog.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.add(thread)
        # MyMushafViewDialog.RUNNING_THREADS_MUTEX.unlock()

    def remove_thread(self, thread):
        # MyMushafViewDialog.RUNNING_THREADS_MUTEX.lock()
        self.running_threads.remove(thread)
        # MyMushafViewDialog.RUNNING_THREADS_MUTEX.unlock()

    def align_titles(self, lang: AppLang):
        if lang == AppLang.ENGLISH:
            self.allWordsNum.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.uniqueWordsNum.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.mostRepeatedWords.setAlignment(Qt.AlignmentFlag.AlignRight)
        else:
            self.allWordsNum.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.uniqueWordsNum.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.mostRepeatedWords.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def load_exclusive_words_data(self):
        self.exclusive_words_uni = load(open(resource_path("data/exclusive_per_surah_uni.json"), mode='r', encoding='utf-8'))
        self.exclusive_words_uni_diff_roots = load(open(resource_path("data/exclusive_per_surah_uni_diff_roots.json"), mode='r', encoding='utf-8'))
        self.exclusive_words_bi = load(open(resource_path("data/exclusive_per_surah_bi.json"), mode='r', encoding='utf-8'))
        self.exclusive_words_tri = load(open(resource_path("data/exclusive_per_surah_tri.json"), mode='r', encoding='utf-8'))

    def get_current_surah_stats(self, clear_current=False, get_exclusive_phrases=True):
        if self.selectionStartInfo is not None or self.selectionEndInfo is not None:
            return False
        if clear_current:
            self.surahUniqueWords.setText("")
            # self.mostRepeatedLetter.setText("")
            self.mostRepeatedWord.setText("")
            self.surahWordsNum.setText("")
            self.clear_histogram()
        for i, surah in enumerate(self.page.surahs):
            span_thread = SpanInfoThread(surah_name=surah.surah_name,
                                         count_waw_as_a_word=self.wawIsAWordCheckbox.isChecked(),
                                         count_waikaana_as_two_words=self.waykaannaTwoWordsCheckbox.isChecked(),
                                         count_huroof_maani=self.huroofMaaniCheckbox.isChecked(),
                                         metadata=MySpanInfoMetaData(i,
                                                                     len(self.page.surahs),
                                                                     get_exclusive_phrases))
            span_thread.from_text('\n'.join(MyDataLoader.get_surah(surah.surah_num)))
            span_thread.result_ready.connect(self.current_surah_stats_callback)
            self.add_thread(span_thread)
            span_thread.start()

        return True

    def current_surah_stats_callback(self, span_info: SpanInfo, thread_id, caller_thread: SpanInfoThread):
        caller_thread.result_ready.disconnect(self.current_surah_stats_callback)
        QTimer.singleShot(MyMushafViewDialog.REMOVE_THREAD_AFTER_MS, lambda: self.remove_thread(caller_thread))

        # --- MUTEX LOCK ---
        MyMushafViewDialog.CURRENT_SURAH_STATS_MUTEX.lock()

        unique_words_percent = int(span_info.surah_unique_words_num) / int(span_info.words_in_selection) * 100
        # if span_info.metadata.total_surahs_in_page == 1:
        #     self.surahUniqueWords.setText(f"{span_info.surah_unique_words_num} ({unique_words_percent:.0f}%)")
        #     self.mostRepeatedWord.setText(f"{span_info.most_repeated_word[0]} ({span_info.most_repeated_word[1]})")
        #     self.surahWordsNum.setText(f"{span_info.words_in_selection}")
        # else:
        # MULTI SURAH [BEGIN]
        # unique words num
        unique_words_num_new_text = (self.surahUniqueWords.text() + ", " + f"{span_info.surah_name}: {span_info.surah_unique_words_num} ({unique_words_percent:.0f}%)").strip(", ")
        unique_words_num_sorted_results = sorted(unique_words_num_new_text.split(", "), key=lambda x: MyDataLoader.get_surah_num(x.split(": ")[0]))
        self.surahUniqueWords.setText(", ".join(unique_words_num_sorted_results))

        # most repeated word
        word, repetitions = span_info.most_repeated_word
        most_repeated_word_new_text = (self.mostRepeatedWord.text() + ", " + f"{span_info.surah_name}: '{word}' ({repetitions})").strip(", ")
        most_repeated_word_sorted_results = sorted(most_repeated_word_new_text.split(", "), key=lambda x: MyDataLoader.get_surah_num(x.split(": ")[0]))
        self.mostRepeatedWord.setText(", ".join(most_repeated_word_sorted_results))

        # surah words num
        surah_words_num_new_text = (self.surahWordsNum.text() + ", " + f"{span_info.surah_name}: {span_info.words_in_selection}").strip(", ")
        surah_words_num_sorted_results = sorted(surah_words_num_new_text.split(", "), key=lambda x: MyDataLoader.get_surah_num(x.split(": ")[0]))
        self.surahWordsNum.setText(", ".join(surah_words_num_sorted_results))
        # MULTI SURAH [END]

        # surah exclusive phrases
        # Surah x: a (#), bc (#), def (#)
        if span_info.metadata.get_exclusive:
            self.fill_exclusive_words(span_info)

        # histogram
        self.fill_histogram(span_info.letters_histogram)
        # Note: letters sum may count letters not included in histogram
        self.lettersSumTableWidget.item(0,0).setText(f"{span_info.letters_in_selection:,}")

        # --- MUTEX UNLOCK ---
        MyMushafViewDialog.CURRENT_SURAH_STATS_MUTEX.unlock()

    def clear_histogram(self):
        for i in range(self.lettersHistogram.columnCount()):
            self.lettersHistogram.item(0, i).setText("")
            self.lettersHistogram.item(0, i).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lettersSumTableWidget.item(0, 0).setText("")
        self.lettersSumTableWidget.item(0, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def fill_histogram(self, data: list):
        self.lettersHistogram.clearSelection()
        for i,cnt in enumerate(data):
            self.lettersHistogram.item(0, i).setText(str(cnt))

    def fill_exclusive_words(self, span_info):
        span_info.surah_exclusive_words = self.exclusive_words_uni[str(span_info.surah_num)]
        span_info.surah_exclusive_words_diff_roots = self.exclusive_words_uni_diff_roots[str(span_info.surah_num)]
        span_info.surah_exclusive_bigrams = self.exclusive_words_bi[str(span_info.surah_num)]
        span_info.surah_exclusive_trigrams = self.exclusive_words_tri[str(span_info.surah_num)]

        if self.differentRootCheckBox.isChecked():
            uni = span_info.surah_exclusive_uni_diff_roots_random
        else:
            uni = span_info.surah_exclusive_uni_random
        bi = span_info.surah_exclusive_bi_random
        tri = span_info.surah_exclusive_tri_random
        ptrn = r"((?: |^)و) "
        bi = re.sub(ptrn, r"\1", bi)
        tri = re.sub(ptrn, r"\1", tri)
        txt_details = f"{uni}, {bi}, {tri}".strip(", ")
        txt = f"{span_info.surah_name}: {txt_details}"
        match span_info.metadata.current_surah_id:
            case 0:
                self.exclusivePhrasesInSurah1.setText(txt)
            case 1:
                self.exclusivePhrasesInSurah2.setText(txt)
            case 2:
                self.exclusivePhrasesInSurah3.setText(txt)

        if span_info.metadata.total_surahs_in_page == 1:
            self.exclusivePhrasesInSurah2.setText("")
            self.exclusivePhrasesInSurah3.setText("")

        if span_info.metadata.total_surahs_in_page == 2:
            self.exclusivePhrasesInSurah3.setText("")

    def clear_results(self):
        # self.wordsInSelection.setText("0")
        self.surahUniqueWords.setText("")
        # self.mostRepeatedLetter.setText("")
        self.mostRepeatedWord.setText("")
        self.surahWordsNum.setText("")
        self.clear_histogram()

    def clear_selection_info(self):
        self.selectionStartLabel.setText("")
        self.selectionEndLabel.setText("")
        self.selectionStartInfo = None
        self.selectionEndInfo = None
        self.lettersHistogram.clearSelection()
        cursor = self.textBrowser.textCursor()
        if cursor.selectionStart() != cursor.selectionEnd():
            cursor.setPosition(cursor.selectionStart())
            self.textBrowser.setTextCursor(cursor)

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
        self.surahNameInput.setStyleSheet("")
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

    def show_verses_from_surah_verse_ref(self, surah_num, verse_num):
        if surah_num and verse_num:
            page_num = MyDataLoader.get_verses_of_surah_verse_ref(surah_num, verse_num)
            self.show_verses_from_page(page_num)
            return page_num
        return None

    def show_verses_from_page(self, page_num):
        page_num = int(page_num)
        self.textBrowser.clear()
        self.pageNumDisplay.setText(f"{translate_text('صفحة')} {page_num}")
        if page_num % 2 == 1:
            self.pageSideIcon.setPixmap(QPixmap(u":/right-page-icon.png"))
        else:
            self.pageSideIcon.setPixmap(QPixmap(u":/left-page-icon.png"))
        self.juzzNumDisplay.setText(f"{translate_text('جزء')} {MyDataLoader.page_to_juzz(page_num)}")

        surahs_nums = []
        surahs_names = []
        verses_counts = []
        current_idx = 0
        self.page.clear()
        for data in MyDataLoader.get_verses_of_page(page_num):
            verses_start_offset = 0
            surah_in_page = SurahInPage()
            surah_num, verses_range, verses = data.surah_num, data.verses_range, data.verses
            has_next = data.has_next
            surahs_nums.append(str(surah_num))
            verses_counts.append(str(MyDataLoader.get_number_of_verses(surah_num)))
            al_fatiha = surah_num == 1
            al_baqara_first_page = (surah_num == 2) and (verses_range[0] == 1)
            should_center = al_fatiha or al_baqara_first_page or surah_num >= 103
            separator = '<br>' if should_center else ' '
            self.textBrowser.setAlignment(Qt.AlignmentFlag.AlignCenter)
            needs_basmalah = self.needsBasmalah(surah_num) and verses_range[0] == 1
            surah_name = MyDataLoader.get_surah_name(surah_num)
            surahs_names.append(translate_text(surah_name))
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
        self.surahNumDisplay.setText(f"{translate_text('رقم')}: {', '.join(surahs_nums)}")
        self.versesCountDisplay.setText(f"{translate_text('آيات')}: {', '.join(verses_counts)}")
        self.surahNameDisplay.setText(", ".join(surahs_names))

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

    def next_surah_button_clicked(self):
        if self.page.surahs[-1].surah_num < self.LAST_SURAH:
            self._current_page = MyDataLoader.get_first_page_of_surah(self.page.surahs[-1].surah_num + 1)
            self.show_verses_from_page(self._current_page)
            self.get_current_surah_stats(clear_current=True)

    def prev_surah_button_clicked(self):
        if self.page.surahs[0].surah_num > self.FIRST_SURAH:
            self._current_page = MyDataLoader.get_first_page_of_surah(self.page.surahs[0].surah_num - 1)
            self.show_verses_from_page(self._current_page)
            self.get_current_surah_stats(clear_current=True)

    def next_juz_button_clicked(self):
        current_juz = MyDataLoader.page_to_juzz(self.current_page)
        if current_juz < self.LAST_JUZ:
            self._current_page = MyDataLoader.juz_to_page(current_juz + 1)
            self.show_verses_from_page(self._current_page)
            self.get_current_surah_stats(clear_current=True)

    def prev_juz_button_clicked(self):
        current_juz = MyDataLoader.page_to_juzz(self.current_page)
        if current_juz > self.FIRST_JUZ:
            self._current_page = MyDataLoader.juz_to_page(current_juz - 1)
            self.show_verses_from_page(self._current_page)
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
                if self.get_current_surah_stats(clear_current=True):
                    self.last_selection_type = SelectionType.BY_PAGE

    def go_to_ref_by_surah_num_and_verse_num(self):
        prev_surahs = tuple(surah.surah_num for surah in self.page.surahs)
        if self.verseInput.text() and self.surahNumInput.text():
            self.current_page = self.show_verses_from_surah_verse_ref(self.surahNumInput.text(), self.verseInput.text())
        elif self.surahNumInput.text():
            page_num = self.show_verses_from_beginning_of_surah(self.surahNumInput.text())
            self.current_page = page_num
        new_surahs = tuple(surah.surah_num for surah in self.page.surahs)
        if prev_surahs != new_surahs:
            if self.get_current_surah_stats(clear_current=True):
                self.last_selection_type = SelectionType.BY_PAGE

    def go_to_ref_by_surah_name_and_verse_num(self):
        prev_surahs = tuple(surah.surah_num for surah in self.page.surahs)
        surah_num = MyDataLoader.get_surah_num(self.surahNameInput.text())
        if surah_num is None:
            if self.surahNameInput.text():
                self.surahNameInput.setStyleSheet("color: red")
            return
        if self.verseInput_2.text() and self.surahNameInput.text():
            self.current_page = self.show_verses_from_surah_verse_ref(surah_num, self.verseInput_2.text())
        elif self.surahNameInput.text():
            page_num = self.show_verses_from_beginning_of_surah(surah_num)
            self.current_page = page_num
        new_surahs = tuple(surah.surah_num for surah in self.page.surahs)
        if prev_surahs != new_surahs:
            if self.get_current_surah_stats(clear_current=True):
                self.last_selection_type = SelectionType.BY_PAGE

    def valid_selection(self):
        cursor = self.textBrowser.textCursor()
        span = (cursor.selectionStart(), cursor.selectionEnd())
        return span[0] != span[1]

    def on_cursor_position_changed(self):
        # cursor = self.textBrowser.textCursor()
        # span = (cursor.selectionStart(), cursor.selectionEnd())
        # print(span)
        if self.valid_selection():
            # cursor = self.textBrowser.textCursor()
            # span = (cursor.selectionStart(), cursor.selectionEnd())
            # print(span)
            self.start_span_info_thread(SelectionType.BY_TEXT)
        # else:
        # elif self.last_selection_type == SelectionType.BY_TEXT:
        # tried to refresh current surah stats upon clearing selection,
        # but this function is also called after the next / prev buttons are called,
        # and the problem is that this function is called first.
        # so this will trigger either way, and then the button's function will trigger,
        # causing a double call to self.get_current_surah_stats()
        # so right now the only option to refresh current surah stats after text selection is
        # to click the refresh button.
        #     if self.get_current_surah_stats(clear_current=True, get_exclusive_phrases=False):
        #         self.last_selection_type = SelectionType.BY_PAGE

    def span_info_completed(self, span_info: SpanInfo, thread_id, caller_thread: SpanInfoThread):
        caller_thread.result_ready.disconnect(self.span_info_completed)
        QTimer.singleShot(MyMushafViewDialog.REMOVE_THREAD_AFTER_MS, lambda: self.remove_thread(caller_thread))
        if thread_id < self._last_thread_id:
            return
        self._last_thread_id = thread_id

        # self.wordsInSelection.setText(str(span_info.words_in_selection))
        self.surahUniqueWords.setText(str(span_info.surah_unique_words_num))
        if len(span_info.most_repeated_word) == 2:
            self.mostRepeatedWord.setText(f"{span_info.most_repeated_word[0]} ({span_info.most_repeated_word[1]})")
        else:
            self.mostRepeatedWord.setText("")
        self.surahWordsNum.setText(f"{span_info.words_in_selection}")
        self.fill_histogram(span_info.letters_histogram)
        # Note: letters sum may count letters not included in histogram
        self.lettersSumTableWidget.item(0,0).setText(f"{span_info.letters_in_selection:,}")

        self.finished_waiting()
        # print(f"{count.words_in_selection = }")

    def selection_start_button_clicked(self):
        self.selectionStartInfo = self.get_selection_info()
        if self.selectionStartInfo is not None:
            if self.selectionEndInfo is not None and self.selectionStartInfo >= self.selectionEndInfo:
                self.selectionEndInfo = None
                self.selectionEndLabel.clear()
            surah_name, verse_num, word = self.selectionStartInfo.surah_name, self.selectionStartInfo.verse_num, self.selectionStartInfo.word
            aya = translate_text("آية")
            self.selectionStartLabel.setText(f"[{translate_text(surah_name)} - {aya} {verse_num} - {word}]")
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
            aya = translate_text("آية")
            self.selectionEndLabel.setText(f"[{translate_text(surah_name)} - {aya} {verse_num} - {word}]")
            if self.selectionStartInfo is not None and self.selectionEndInfo > self.selectionStartInfo:
                self.start_span_info_thread(SelectionType.BY_REF)

        self.textBrowser.setFocus()
        self.beam_cursor()

    def letters_histogram_selection_changed(self):
        total = sum(int(item.text()) for item in self.lettersHistogram.selectedItems())
        self.lettersSumTableWidget.item(0,0).setText(str(total))

    def valid_selection_span(self):
        if self.selectionStartInfo is None or self.selectionEndInfo is None:
            return False
        if self.selectionStartInfo < self.selectionEndInfo:
            return True
        return False

    def start_span_info_thread(self, selection_type: SelectionType):
        self.last_selection_type = selection_type
        self._thread_id = datetime.now().timestamp()
        span_thread = SpanInfoThread(self._thread_id,
                                     count_waw_as_a_word=self.wawIsAWordCheckbox.isChecked(),
                                     count_waikaana_as_two_words=self.waykaannaTwoWordsCheckbox.isChecked(),
                                     count_huroof_maani=self.huroofMaaniCheckbox.isChecked())
        if selection_type == SelectionType.BY_TEXT:
            span_thread.from_text(self.textBrowser.textCursor().selection().toPlainText())
        elif selection_type == SelectionType.BY_REF:
            span_thread.from_ref(self.selectionStartInfo, self.selectionEndInfo)
        else:
            return
        span_thread.result_ready.connect(self.span_info_completed)
        self.add_thread(span_thread)

        span_thread.start()
        if selection_type == SelectionType.BY_REF and self.selectionEndInfo - self.selectionStartInfo >= MyMushafViewDialog.MIN_PAGES_FOR_WAITING:
            self.waiting()

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
        # if self.last_selection_type == SelectionType.BY_PAGE:
        self.get_current_surah_stats(clear_current=True, get_exclusive_phrases=False)
        if self.valid_selection() or self.valid_selection_span():
            self.start_span_info_thread(self.last_selection_type)

    def waykaanna_two_words_checkbox_state_changed(self, state):
        if self.last_selection_type == SelectionType.NO_SELECTION:
            return
        # if self.last_selection_type == SelectionType.BY_PAGE:
        self.get_current_surah_stats(clear_current=True, get_exclusive_phrases=False)
        if self.valid_selection() or self.valid_selection_span():
            self.start_span_info_thread(self.last_selection_type)

    def huroof_maani_checkbox_state_changed(self, state):
        if self.last_selection_type == SelectionType.NO_SELECTION:
            return
        # if self.last_selection_type == SelectionType.BY_PAGE:
        self.get_current_surah_stats(clear_current=True, get_exclusive_phrases=False)
        if self.valid_selection() or self.valid_selection_span():
            self.start_span_info_thread(self.last_selection_type)

    def diff_roots_checkbox_state_changed(self, state):
        self.refresh_exclusive_words_buton_clicked()

    def restart_stats_button_clicked(self):
        for widget in self.stats_widgets:
            widget.setText("0")
        self.clear_selection_info()
        if self.get_current_surah_stats(clear_current=True, get_exclusive_phrases=False):
            self.last_selection_type = SelectionType.BY_PAGE

    def refresh_exclusive_words_buton_clicked(self):
        for i, surah in enumerate(self.page.surahs):
            span_info = SpanInfo()
            span_info.surah_num = surah.surah_num
            span_info.surah_name = surah.surah_name
            span_info.metadata = MySpanInfoMetaData(i)
            self.fill_exclusive_words(span_info)

    def enable_inputs(self,
                      page_input: bool = True,
                      surah_num: bool = True,
                      verse_num_1: bool = True,
                      surah_name: bool = True,
                      verse_num_2: bool = True,
                      text_browser: bool = True,):
        if page_input:
            self.pageInput.setEnabled(True)
        if surah_num:
            self.surahNumInput.setEnabled(True)
        if verse_num_1:
            self.verseInput.setEnabled(True)
        if surah_name:
            self.surahNameInput.setEnabled(True)
        if verse_num_2:
            self.verseInput_2.setEnabled(True)
        if text_browser:
            self.textBrowser.setEnabled(True)

    def disable_inputs(self,
                       page_input: bool = True,
                       surah_num: bool = True,
                       verse_num_1: bool = True,
                       surah_name: bool = True,
                       verse_num_2: bool = True,
                       text_browser: bool = True):
        if page_input:
            self.pageInput.setEnabled(False)
        if surah_num:
            self.surahNumInput.setEnabled(False)
        if verse_num_1:
            self.verseInput.setEnabled(False)
        if surah_name:
            self.surahNameInput.setEnabled(False)
        if verse_num_2:
            self.verseInput_2.setEnabled(False)
        if text_browser:
            self.textBrowser.setEnabled(False)

    def waiting(self, text=""):
        self.spinner.setText(text)
        self.spinner.start()
        self.disable_inputs()

    def finished_waiting(self):
        self.spinner.stop()
        self.enable_inputs()
