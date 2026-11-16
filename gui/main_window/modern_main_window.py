"""Presentation layer over the Designer form; all existing controls stay intact.

Keep layout/theme code here rather than editing main_screen.py, which build.bat
regenerates. The original control names and button group remain the controller's
API, including their validators, signals, defaults and custom result widgets.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon, QKeySequence, QPalette, QShortcut
from PySide6.QtWidgets import (
    QFrame, QGridLayout, QHBoxLayout, QLabel, QScrollArea, QSizePolicy, QTabWidget,
    QToolButton, QVBoxLayout, QWidget,
)

from gui.main_window.main_screen import Ui_MainWindow as DesignerUi
from gui.theme import STYLESHEET
from gui.main_window.results_placeholder import ResultsPlaceholder
from my_utils.my_enums import AppLang


class Ui_MainWindow(DesignerUi):
    def setupUi(self, window):
        super().setupUi(window)
        self._language = AppLang.DEFAULT_LANGUAGE
        # Remove the form's old per-widget colors so the theme has one source.
        for widget in self.centralwidget.findChildren(QWidget):
            widget.setStyleSheet("")

        old_central = window.takeCentralWidget()
        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        root = QVBoxLayout(self.centralwidget)
        root.setContentsMargins(16, 4, 16, 16)
        root.setSpacing(8)

        header = QHBoxLayout()
        header.setSpacing(16)
        self.brand_mark = QLabel("۞")
        self.brand_mark.setObjectName("brandMark")
        header.addWidget(self.brand_mark)
        self.title = self._label("title")
        header.addWidget(self.title, 1)
        self.browse_button = QToolButton()
        self.browse_button.setObjectName("browseButton")
        self.browse_button.setDefaultAction(self.mushafNavigationButton)
        self.browse_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        header.addWidget(self.browse_button)
        root.addLayout(header)

        workspace = QHBoxLayout()
        workspace.setSpacing(20)
        self.sidebar = QScrollArea()
        self.sidebar.setObjectName("searchSidebar")
        self.sidebar.setWidgetResizable(True)
        # A scroll area's StrongFocus otherwise steals focus from mouse clicks
        # on its TabFocus-only radio buttons.
        self.sidebar.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.sidebar.setFixedWidth(250)
        self.sidebar.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        modes = QWidget()
        modes.setObjectName("searchModes")
        modes_layout = QVBoxLayout(modes)
        modes_layout.setContentsMargins(16, 18, 16, 18)
        modes_layout.setSpacing(7)
        self.modes_title = self._label("section")
        modes_layout.addWidget(self.modes_title)
        modes_layout.addSpacing(8)
        self.mode_buttons = [
            self.noRestrictionsRadioButton, self.fullWordRadioButton,
            self.beginningOfWordRadioButton, self.endOfWordRadioButton,
            self.rootRadioButton, self.similarWordRadioButton,
            self.relatedWordsRadioButton, self.topicsRadioButton,
            self.regexRadioButton,
        ]
        for button in self.mode_buttons:
            # Mouse selection keeps the query focused; Tab/Space still support
            # keyboard navigation through the modes.
            button.setFocusPolicy(Qt.FocusPolicy.TabFocus)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            modes_layout.addWidget(button)
            if button is self.similarWordRadioButton:
                modes_layout.addLayout(self._threshold_row(self.similarityThresholdSlider, self.similarityThresholdLabel))
            elif button is self.relatedWordsRadioButton:
                modes_layout.addLayout(self._threshold_row(self.relatedWordsThresholdSlider, self.relatedWordsThresholdLabel))
        modes_layout.addStretch()
        self.sidebar.setWidget(modes)

        self.matching_options = QFrame()
        self.matching_options.setObjectName("matchingOptions")
        matching_layout = QHBoxLayout(self.matching_options)
        matching_layout.setContentsMargins(0, 0, 0, 0)
        matching_layout.setSpacing(12)
        self.refinements_title = self._label("muted")
        matching_layout.addWidget(self.refinements_title)
        self.refinements = (self.alifAlifMaksuraCheckbox, self.yaAlifMaksuraCheckbox,
                            self.finalTaCheckbox, self.wordPermutationsCheckbox,
                            self.optionalAlTarifCheckbox)
        for checkbox in self.refinements:
            checkbox.setFocusPolicy(Qt.FocusPolicy.TabFocus)
            matching_layout.addWidget(checkbox)
            checkbox.toggled.connect(self._update_options_summary)
        matching_layout.addStretch()

        content = QVBoxLayout()
        content.setSpacing(6)
        search_grid = QGridLayout()
        search_grid.setHorizontalSpacing(20)
        search_grid.setVerticalSpacing(8)
        search_grid.setColumnStretch(1, 1)
        self.label.setBuddy(self.searchWord)
        self.label.hide()
        self.label.setParent(self.centralwidget)
        self.searchWord.setClearButtonEnabled(True)
        self.searchWord.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.searchWord.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignAbsolute)
        search_grid.addWidget(self.searchWord, 0, 1)
        self.options_button = QToolButton()
        self.options_button.setObjectName("optionsButton")
        self.options_button.setCheckable(True)
        self.options_button.setFixedWidth(250)
        self.options_button.toggled.connect(self._toggle_options)
        self.searchOptionsButtonGroup.buttonToggled.connect(self._update_options_summary)
        search_grid.addWidget(self.options_button, 0, 0)
        search_grid.addWidget(self.matching_options, 1, 1)
        root.addLayout(search_grid)

        self.result_summary = QFrame()
        self.result_summary.setObjectName("resultSummary")
        stats = QHBoxLayout(self.result_summary)
        stats.setContentsMargins(4, 0, 4, 0)
        stats.setSpacing(8)
        for label, value in ((self.label_2, self.matchesNumber),
                             (self.label_4, self.matchesNumberSurahs),
                             (self.label_5, self.matchesNumberVerses)):
            label.setProperty("role", "statLabel")
            value.setProperty("role", "count")
            value.setEnabled(True)
            value.setReadOnly(True)
            value.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            value.setPlaceholderText("0")
            palette = value.palette()
            palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("#a8c4ff"))
            value.setPalette(palette)
            value.textChanged.connect(lambda _text, field=value: self._size_count(field))
            stats.addWidget(value)
            stats.addWidget(label)
            stats.addSpacing(20)
        stats.addStretch()
        content.addWidget(self.result_summary)

        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.tabBar().setDrawBase(False)
        self.tabWidget.setMinimumHeight(300)
        self.tabWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        content.addWidget(self.tabWidget, 1)
        # Put result actions on one toolbar, leaving the full width for verses.
        self.horizontalLayout_3.addWidget(self.colorizeCheckbox)
        self.horizontalLayout_5.removeItem(self.verticalLayout_9)
        self.line_3.hide()
        self.results_placeholder = ResultsPlaceholder(self.foundVerses)
        word_options = QHBoxLayout()
        for checkbox in (self.diacriticsCheckbox, self.wordTransliterationCheckbox,
                         self.wordMeaningCheckbox):
            word_options.addWidget(checkbox)
        word_options.addStretch()
        self.horizontalLayout_11.removeItem(self.verticalLayout_16)
        self.line_2.hide()
        self.line_9.hide()
        self.verticalLayout_5.insertLayout(0, word_options)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout_4.insertWidget(0, self.allResultsCheckbox)
        self.horizontalLayout_9.removeItem(self.verticalLayout_14)
        # Detail instructions belong to table tooltips; keep search requirements
        # visible, including the controller's validation feedback on those labels.
        for hint in (self.label_7, self.label_8, self.label_10):
            hint.hide()
        for hint in (self.minimum_letters_restriction_lbl, self.minimum_letters_restriction_lbl_2):
            hint.setProperty("role", "muted")
        for table in (self.surahResultsTableWidget, self.wordResultsTableWidget,
                      self.topicResultsTableWidget):
            table.setAlternatingRowColors(True)
            table.setShowGrid(False)
            table.setMinimumHeight(110)
            table.verticalHeader().setDefaultSectionSize(46)
        workspace.addWidget(self.sidebar)
        workspace.addLayout(content, 1)
        root.addLayout(workspace, 1)
        window.setCentralWidget(self.centralwidget)
        old_central.deleteLater()
        self.statusbar.hide()
        window.setMinimumSize(940, 640)
        window.resize(1220, 860)
        self.search_shortcut = QShortcut(QKeySequence("Ctrl+F"), window)
        self.search_shortcut.activated.connect(self._focus_search)
        focus_order = [self.searchWord, self.options_button, *self.refinements,
                       *self.mode_buttons[:6], self.similarityThresholdSlider,
                       self.relatedWordsRadioButton, self.relatedWordsThresholdSlider,
                       self.topicsRadioButton, self.regexRadioButton, self.tabWidget]
        for previous, following in zip(focus_order, focus_order[1:]):
            QWidget.setTabOrder(previous, following)
        window.setStyleSheet(STYLESHEET)
        self.set_language(window, self._language)
        self.options_button.setChecked(True)
        self.searchWord.setFocus()

    @staticmethod
    def _label(role):
        label = QLabel()
        label.setProperty("role", role)
        return label

    @staticmethod
    def _threshold_row(slider, label):
        row = QHBoxLayout()
        row.setContentsMargins(20, 0, 20, 4)
        row.setSpacing(12)
        row.addWidget(slider, 1)
        row.addWidget(label)
        return row

    def _focus_search(self):
        self.searchWord.setFocus()
        self.searchWord.selectAll()

    def _toggle_options(self, expanded):
        self.sidebar.setVisible(expanded)
        self._update_options_summary()
        if not expanded:
            self.searchWord.setFocus()

    def _update_options_summary(self, *_args):
        arabic = self._language == AppLang.ARABIC
        mode = self.searchOptionsButtonGroup.checkedButton().text()
        count = sum(checkbox.isChecked() for checkbox in self.refinements)
        label = "خيارات البحث" if arabic else "Search options"
        suffix = f" (+{count})" if count else ""
        self.options_button.setText(label)
        self.options_button.setAccessibleName(f"{label} · {mode}{suffix}")
        self.options_button.setToolTip(
            ("إخفاء خيارات البحث" if arabic else "Hide search options")
            if self.options_button.isChecked() else
            ("إظهار خيارات البحث" if arabic else "Show search options")
        )
        self.options_button.setToolTip(f"{self.options_button.toolTip()}\n{mode}{suffix}")

    @staticmethod
    def _size_count(field):
        field.setFixedWidth(max(28, field.fontMetrics().horizontalAdvance(field.text() or "0") + 12))

    def retranslateUi(self, window):
        super().retranslateUi(window)
        if hasattr(self, "title"):
            self.set_language(window, self._language)

    def set_language(self, window, language):
        """Localize added chrome and mirror the layout alongside existing .qm text."""
        self._language = language
        arabic = language == AppLang.ARABIC
        window.setLayoutDirection(Qt.LayoutDirection.RightToLeft if arabic else Qt.LayoutDirection.LeftToRight)
        # AlignRight alone is mirrored by Qt for RTL text. AlignAbsolute pins
        # both the entered query and its placeholder to the physical right.
        self.searchWord.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.searchWord.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignAbsolute)
        text = lambda ar, en: ar if arabic else en
        self.title.setText(text("عدّاد القرآن الكريم", "Quran Counter"))
        self.modes_title.setText(text("طريقة البحث", "SEARCH MODE"))
        self.refinements_title.setText(text("خيارات المطابقة", "Matching options"))
        self.refinements_title.setToolTip(text(
            "متاحة للبحث دون تقييد أو عن كلمة كاملة أو بداية كلمة أو نهايتها",
            "Available for unrestricted, full-word, beginning-of-word and end-of-word searches.",
        ))
        self.label_2.setText(text("نتيجة", "Matches"))
        self.label_4.setText(text("سورة", "Surahs"))
        self.label_5.setText(text("آية", "Verses"))
        self.searchWord.setPlaceholderText(text("اكتب كلمة أو عبارة…", "Search an Arabic word or phrase…"))
        self.searchWord.setAccessibleName(text("البحث في القرآن", "Search the Quran"))
        self.searchWord.setToolTip(text("تظهر النتائج أثناء الكتابة · Ctrl+F", "Results update as you type · Ctrl+F"))
        self.results_placeholder.set_text(text("ابدأ البحث لاستكشاف الآيات هنا", "Start a search to explore matching verses here."))
        self.filterButton.setText(text("تصفية ذكية", "Smart filter"))
        self.clearFilterButton.setText(text("مسح التصفية", "Clear filter"))
        for table, hint in ((self.surahResultsTableWidget, self.label_8),
                            (self.wordResultsTableWidget, self.label_7),
                            (self.topicResultsTableWidget, self.label_10)):
            table.setToolTip(hint.text())
        self.wordPermutationsCheckbox.setAccessibleName(self.wordPermutationsCheckbox.toolTip())
        self.wordPermutationsCheckbox.setText(text("تبديل ترتيب الكلمات", "Any word order"))
        self.wordPermutationsCheckbox.setIcon(QIcon())
        for menu, ar, en in ((self.menu_Language, "اللغة", "Language"),
                             (self.mushafViewButton, "المصحف", "Quran"),
                             (self.menuChatGPT, "المساعد", "Assistant"),
                             (self.helpMenuButton, "مساعدة", "Help")):
            menu.setIcon(QIcon())
            menu.setTitle(text(ar, en))
        for label, value in ((self.label_2, self.matchesNumber),
                             (self.label_4, self.matchesNumberSurahs),
                             (self.label_5, self.matchesNumberVerses)):
            value.setAccessibleName(label.text())
            value.setAlignment(Qt.AlignmentFlag.AlignRight if arabic else Qt.AlignmentFlag.AlignLeft)
        for widget in [window, *window.findChildren(QWidget)]:
            widget.setProperty("arabic", arabic)
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.updateGeometry()
        for field in (self.matchesNumber, self.matchesNumberSurahs, self.matchesNumberVerses):
            self._size_count(field)
        self._update_options_summary()
