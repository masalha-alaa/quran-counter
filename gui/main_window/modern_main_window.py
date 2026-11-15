"""Presentation layer over the Designer form; all existing controls stay intact.

Keep layout/theme code here rather than editing main_screen.py, which build.bat
regenerates. The original control names and button group remain the controller's
API, including their validators, signals, defaults and custom result widgets.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon, QKeySequence, QPalette, QShortcut
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QScrollArea, QSizePolicy, QTabWidget,
    QToolButton, QVBoxLayout, QWidget,
)

from gui.main_window.main_screen import Ui_MainWindow as DesignerUi
from gui.main_window.theme import STYLESHEET
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
        root.setContentsMargins(24, 12, 24, 22)
        root.setSpacing(16)

        header = QHBoxLayout()
        header.setSpacing(16)
        self.brand_mark = QLabel("۞")
        self.brand_mark.setObjectName("brandMark")
        header.addWidget(self.brand_mark)
        heading = QVBoxLayout()
        heading.setSpacing(2)
        self.title = self._label("title")
        self.subtitle = self._label("subtitle")
        heading.addWidget(self.title)
        heading.addWidget(self.subtitle)
        header.addLayout(heading, 1)
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
        self.sidebar.setMinimumWidth(250)
        self.sidebar.setMaximumWidth(310)
        self.sidebar.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        modes = QWidget()
        modes.setObjectName("searchModes")
        modes_layout = QVBoxLayout(modes)
        modes_layout.setContentsMargins(16, 18, 16, 18)
        modes_layout.setSpacing(7)
        self.modes_title = self._label("section")
        self.modes_hint = self._label("muted")
        self.modes_hint.setWordWrap(True)
        modes_layout.addWidget(self.modes_title)
        modes_layout.addWidget(self.modes_hint)
        modes_layout.addSpacing(8)
        self.mode_buttons = [
            self.noRestrictionsRadioButton, self.fullWordRadioButton,
            self.beginningOfWordRadioButton, self.endOfWordRadioButton,
            self.rootRadioButton, self.similarWordRadioButton,
            self.relatedWordsRadioButton, self.topicsRadioButton,
            self.regexRadioButton,
        ]
        for button in self.mode_buttons:
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            modes_layout.addWidget(button)
            if button is self.similarWordRadioButton:
                modes_layout.addLayout(self._threshold_row(self.similarityThresholdSlider, self.similarityThresholdLabel))
            elif button is self.relatedWordsRadioButton:
                modes_layout.addLayout(self._threshold_row(self.relatedWordsThresholdSlider, self.relatedWordsThresholdLabel))
        modes_layout.addStretch()
        self.sidebar.setWidget(modes)
        workspace.addWidget(self.sidebar)

        content = QVBoxLayout()
        content.setSpacing(16)
        search_card, search_layout = self._card()
        self.label.setProperty("role", "section")
        self.label.setBuddy(self.searchWord)
        self.label.hide()
        self.label.setParent(search_card)
        self.searchWord.setClearButtonEnabled(True)
        self.searchWord.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.searchWord.setAlignment(Qt.AlignmentFlag.AlignRight)
        search_layout.addWidget(self.searchWord)
        options = QHBoxLayout()
        options.setSpacing(14)
        for checkbox in (self.alifAlifMaksuraCheckbox, self.yaAlifMaksuraCheckbox,
                         self.finalTaCheckbox, self.wordPermutationsCheckbox,
                         self.optionalAlTarifCheckbox):
            options.addWidget(checkbox)
        options.addStretch()
        search_layout.addLayout(options)
        content.addWidget(search_card)

        stats = QHBoxLayout()
        stats.setSpacing(12)
        for label, value in ((self.label_2, self.matchesNumber),
                             (self.label_4, self.matchesNumberSurahs),
                             (self.label_5, self.matchesNumberVerses)):
            card, layout = self._card("stat")
            label.setProperty("role", "statLabel")
            value.setProperty("role", "count")
            value.setEnabled(True)
            value.setReadOnly(True)
            value.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            value.setPlaceholderText("0")
            palette = value.palette()
            palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("#8de0bd"))
            value.setPalette(palette)
            value.setMinimumWidth(0)
            value.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
            layout.addWidget(value)
            layout.addWidget(label)
            stats.addWidget(card, 1)
        content.addLayout(stats)

        self.results_title = self._label("section")
        content.addWidget(self.results_title)
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
        workspace.addLayout(content, 1)
        root.addLayout(workspace, 1)
        window.setCentralWidget(self.centralwidget)
        old_central.deleteLater()
        self.statusbar.hide()
        window.setMinimumSize(940, 780)
        window.resize(1220, 860)
        self.search_shortcut = QShortcut(QKeySequence("Ctrl+F"), window)
        self.search_shortcut.activated.connect(self._focus_search)
        focus_order = [self.searchWord, self.alifAlifMaksuraCheckbox,
                       self.yaAlifMaksuraCheckbox, self.finalTaCheckbox,
                       self.wordPermutationsCheckbox, self.optionalAlTarifCheckbox,
                       *self.mode_buttons[:6], self.similarityThresholdSlider,
                       self.relatedWordsRadioButton, self.relatedWordsThresholdSlider,
                       self.topicsRadioButton, self.regexRadioButton, self.tabWidget]
        for previous, following in zip(focus_order, focus_order[1:]):
            QWidget.setTabOrder(previous, following)
        window.setStyleSheet(STYLESHEET)
        self.set_language(window, self._language)
        self.searchWord.setFocus()

    @staticmethod
    def _label(role):
        label = QLabel()
        label.setProperty("role", role)
        return label

    @staticmethod
    def _card(role="card"):
        card = QFrame()
        card.setProperty("role", role)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(18, 12, 18, 12)
        layout.setSpacing(4)
        return card, layout

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

    def retranslateUi(self, window):
        super().retranslateUi(window)
        if hasattr(self, "title"):
            self.set_language(window, self._language)

    def set_language(self, window, language):
        """Localize added chrome and mirror the layout alongside existing .qm text."""
        self._language = language
        arabic = language == AppLang.ARABIC
        window.setLayoutDirection(Qt.LayoutDirection.RightToLeft if arabic else Qt.LayoutDirection.LeftToRight)
        text = lambda ar, en: ar if arabic else en
        self.title.setText(text("عدّاد القرآن الكريم", "Quran Counter"))
        self.subtitle.setText(text("رحلة في كلمات القرآن ومعانيه", "Explore the words. Discover the connections."))
        self.modes_title.setText(text("طريقة البحث", "SEARCH MODE"))
        self.modes_hint.setText(text("اختر كيف تبحث في القرآن", "Choose how you explore the Quran."))
        self.results_title.setText(text("نتائج البحث", "YOUR RESULTS"))
        self.searchWord.setPlaceholderText(text("اكتب كلمة أو عبارة…", "Search an Arabic word or phrase…"))
        self.searchWord.setAccessibleName(text("البحث في القرآن", "Search the Quran"))
        self.searchWord.setToolTip(text("تظهر النتائج أثناء الكتابة · Ctrl+F", "Results update as you type · Ctrl+F"))
        self.foundVerses.setPlaceholderText(text("ابدأ البحث لاستكشاف الآيات هنا", "Start a search to explore matching verses here."))
        self.filterButton.setText(text("تصفية ذكية", "Smart filter"))
        self.clearFilterButton.setText(text("مسح التصفية", "Clear filter"))
        for table, hint in ((self.surahResultsTableWidget, self.label_8),
                            (self.wordResultsTableWidget, self.label_7),
                            (self.topicResultsTableWidget, self.label_10)):
            table.setToolTip(hint.text())
        self.wordPermutationsCheckbox.setAccessibleName(self.wordPermutationsCheckbox.toolTip())
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
