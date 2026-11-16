"""Modern presentation for all Designer dialogs, without editing generated code."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QCheckBox, QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QLayout, QLineEdit, QListWidget,
    QScrollArea, QSizePolicy, QTabWidget, QTableWidget, QTextBrowser,
    QToolButton, QVBoxLayout, QWidget,
)

from gui.theme import STYLESHEET
from my_utils.my_enums import AppLang


def prepare_dialog(dialog, ui, kind):
    """Preserve control identities/signals while updating layout and appearance."""
    dialog._modern_ui = ui
    dialog._modern_kind = kind
    for widget in dialog.findChildren(QWidget):
        widget.setStyleSheet("")
        widget.setFont(QFont())
        if isinstance(widget, QFrame) and widget.frameShape() in (QFrame.HLine, QFrame.VLine):
            widget.setProperty("role", "separator")
        elif isinstance(widget, QFrame):
            widget.setFrameShape(QFrame.NoFrame)
        if isinstance(widget, (QCheckBox, QLabel, QListWidget)):
            widget.unsetLayoutDirection()
        if isinstance(widget, QTableWidget):
            widget.setAlternatingRowColors(True)
            widget.setShowGrid(False)
        if isinstance(widget, QTextBrowser) and widget.objectName() == "textBrowser":
            widget.setProperty("role", "quran")
            widget.setLayoutDirection(Qt.RightToLeft)
        if isinstance(widget, QLineEdit):
            widget.setMinimumHeight(34)
    dialog.setStyleSheet(STYLESHEET)
    dialog.setMaximumSize(16777215, 16777215)
    for layout in dialog.findChildren(QLayout):
        layout.setSpacing(8)

    if kind == "mushaf":
        _layout_mushaf(dialog, ui)
    elif kind == "details":
        ui.horizontalLayout.removeItem(ui.verticalLayout)
        ui.verticalLayout_2.insertWidget(0, ui.colorizeCheckbox)
        ui.textBrowser.setMinimumHeight(220)
        close = QDialogButtonBox()
        # A custom button keeps Qt's deferred LanguageChange event from
        # replacing our Arabic caption with an untranslated standard caption.
        dialog._modern_close = close.addButton("", QDialogButtonBox.RejectRole)
        close.rejected.connect(dialog.reject)
        ui.verticalLayout_2.addWidget(close)
    elif kind == "key":
        ui.enterKeyLineEdit.setLayoutDirection(Qt.LeftToRight)
        ui.enterKeyLineEdit.setAlignment(Qt.AlignLeft | Qt.AlignAbsolute)
        ui.label_2.setWordWrap(True)
        ui.label_3.setWordWrap(True)
        ui.label_2.setProperty("role", "muted")
        ui.label_3.setProperty("role", "muted")
    elif kind == "disambiguation":
        ui.instructionsLabel.setWordWrap(True)
        ui.instructionsWordLabel.setProperty("role", "section")
        ui.resultsListWidget.setMinimumHeight(180)
        ui.verticalLayout.removeItem(ui.horizontalLayout_2)
        ui.horizontalLayout_2.removeItem(ui.spinnerParentLayout)
        ui.spinnerParentLayout.setParent(None)
        instructions = QHBoxLayout()
        instructions.addWidget(ui.instructionsLabel)
        instructions.addWidget(ui.instructionsWordLabel)
        instructions.addStretch()
        instructions.addLayout(ui.spinnerParentLayout)
        ui.verticalLayout.insertLayout(0, instructions)
        ui.verticalLayout.setStretch(0, 0)
        ui.verticalLayout.setStretch(1, 1)
        ui.verticalLayout.setStretch(2, 0)
    elif kind == "download":
        ui.questionLabel.setWordWrap(True)
        ui.detailsLabel.setProperty("role", "muted")
    elif kind == "update":
        ui.statusLabel.setWordWrap(True)
        ui.statusLabel.setProperty("role", "muted")
    elif kind == "waiting":
        ui.label.setProperty("role", "muted")

    for name in ("okButton", "yesButton", "downloadButton"):
        if hasattr(ui, name):
            getattr(ui, name).setProperty("role", "primary")
    root = dialog.layout()
    root.setContentsMargins(20, 16, 20, 20)
    root.setSpacing(12)
    dialog._modern_title = QLabel()
    dialog._modern_title.setProperty("role", "dialogTitle")
    dialog._modern_title.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    root.insertWidget(0, dialog._modern_title)
    sizes = {
        "mushaf": (1100, 820), "details": (960, 640), "relations": (1060, 720),
        "key": (620, 340), "disambiguation": (680, 470), "download": (620, 420),
        "update": (500, 220), "waiting": (420, 240),
    }
    dialog.resize(*sizes[kind])
    set_dialog_language(dialog, AppLang.DEFAULT_LANGUAGE)


def set_dialog_language(dialog, language):
    arabic = language != AppLang.ENGLISH
    dialog.setLayoutDirection(Qt.RightToLeft if arabic else Qt.LeftToRight)
    if hasattr(dialog, "_modern_title"):
        dialog._modern_title.setText(dialog.windowTitle())
    if hasattr(dialog, "_modern_close"):
        dialog._modern_close.setText("إغلاق" if arabic else "Close")
    if getattr(dialog, "_modern_kind", None) == "mushaf":
        ui = dialog._modern_ui
        ui.reader_tabs.setTabText(0, "القراءة" if arabic else "Reading")
        ui.reader_tabs.setTabText(1, "الإحصاءات" if arabic else "Statistics")
        ui.selection_toggle.setText("أدوات التحديد" if arabic else "Selection tools")
        ui.surahNameInput.setLayoutDirection(Qt.RightToLeft)
        ui.surahNameInput.setAlignment(Qt.AlignRight | Qt.AlignAbsolute)
    for widget in [dialog, *dialog.findChildren(QWidget)]:
        widget.setProperty("arabic", arabic)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.updateGeometry()


def _layout_mushaf(dialog, ui):
    root = dialog.layout()
    # Keep detached layout objects alive; the controller retains references to
    # several of them, while their actual controls move to the new pages.
    dialog._old_layout_items = [root.takeAt(0) for _ in range(root.count())]
    navigation = QFrame()
    navigation.setProperty("role", "panel")
    nav_layout = QGridLayout(navigation)
    nav_layout.setContentsMargins(12, 8, 12, 8)
    nav_layout.setHorizontalSpacing(12)
    nav_layout.setVerticalSpacing(8)
    for column, widget in ((0, ui.label), (1, ui.pageInput), (2, ui.goToPageButton),
                           (4, ui.label_4), (5, ui.surahNumInput), (6, ui.label_5),
                           (7, ui.verseInput), (8, ui.goToRefButton)):
        nav_layout.addWidget(widget, 0, column)
    nav_layout.addWidget(ui.label_6, 1, 0)
    nav_layout.addWidget(ui.surahNameInput, 1, 1, 1, 5)
    nav_layout.addWidget(ui.label_17, 1, 6)
    nav_layout.addWidget(ui.verseInput_2, 1, 7)
    nav_layout.addWidget(ui.goToRef_2, 1, 8)
    nav_layout.setColumnStretch(3, 1)
    for separator in (ui.line_2, ui.line_3, ui.line_4):
        separator.hide()
    root.addWidget(navigation)
    ui.surahNameInput.setProperty("role", "arabicInput")
    for name in ("pageInput", "surahNumInput", "verseInput", "verseInput_2"):
        field = getattr(ui, name)
        field.setMinimumWidth(64)
        field.setMaximumWidth(100)
    ui.reader_tabs = QTabWidget()
    ui.reader_tabs.setDocumentMode(True)
    ui.reader_tabs.tabBar().setDrawBase(False)
    reading = QWidget()
    reading_layout = QVBoxLayout(reading)
    reading_layout.setContentsMargins(0, 8, 0, 0)
    ui.textBrowser.setMinimumHeight(260)
    reading_layout.addWidget(ui.textBrowser, 1)
    ui.frame_4.setProperty("role", "panel")
    reading_layout.addWidget(ui.frame_4)
    ui.selection_toggle = QToolButton()
    ui.selection_toggle.setCheckable(True)
    ui.selection_toggle.toggled.connect(ui.frame_2.setVisible)
    reading_layout.addWidget(ui.selection_toggle)
    ui.frame_2.setProperty("role", "panel")
    ui.label_16.setWordWrap(True)
    ui.label_16.setProperty("role", "muted")
    reading_layout.addWidget(ui.frame_2)
    ui.frame_2.hide()
    ui.reader_tabs.addTab(reading, "")

    statistics = QScrollArea()
    statistics.setWidgetResizable(True)
    stats_content = QWidget()
    stats_content.setObjectName("readerStatistics")
    stats_layout = QVBoxLayout(stats_content)
    stats_layout.setContentsMargins(0, 8, 0, 0)
    stats_layout.addWidget(ui.frame)
    ui.horizontalLayout_24.setParent(None)
    stats_layout.addLayout(ui.horizontalLayout_24)
    stats_layout.addStretch()
    statistics.setWidget(stats_content)
    ui.reader_tabs.addTab(statistics, "")
    for name in ("exclusiveWordsFrame", "frame_3"):
        getattr(ui, name).setProperty("role", "panel")
    for name in ("exclusivePhrasesInSurah1", "exclusivePhrasesInSurah2", "exclusivePhrasesInSurah3"):
        getattr(ui, name).setWordWrap(True)
    for name in ("surahUniqueWords", "surahWordsNum", "mostRepeatedWord"):
        getattr(ui, name).setProperty("role", "statValue")
    for table in (ui.lettersSumTableWidget, ui.lettersHistogram):
        table.setMinimumHeight(110)
        table.setMaximumHeight(140)
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    root.addWidget(ui.reader_tabs, 1)
