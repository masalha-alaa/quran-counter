"""Modern presentation for all Designer dialogs, without editing generated code."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QCheckBox, QDialogButtonBox, QFrame, QHBoxLayout, QLabel, QLayout, QLineEdit, QListWidget,
    QSizePolicy, QTableWidget, QTextBrowser, QWidget,
)

from gui.theme import STYLESHEET
from my_utils.my_enums import AppLang


def prepare_dialog(dialog, ui, kind):
    """Preserve control identities/signals while updating layout and appearance."""
    dialog._modern_ui = ui
    dialog._modern_kind = kind
    if kind == "mushaf":
        from gui.mushaf_view_dialog.presentation import style_mushaf
        style_mushaf(dialog, ui)
        set_dialog_language(dialog, AppLang.DEFAULT_LANGUAGE)
        return
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

    if kind == "details":
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
        "details": (960, 640), "relations": (1060, 720),
        "key": (620, 340), "disambiguation": (680, 470), "download": (620, 420),
        "update": (500, 220), "waiting": (420, 240),
    }
    dialog.resize(*sizes[kind])
    set_dialog_language(dialog, AppLang.DEFAULT_LANGUAGE)


def set_dialog_language(dialog, language):
    arabic = language != AppLang.ENGLISH
    is_mushaf = getattr(dialog, "_modern_kind", None) == "mushaf"
    # The Mushaf Designer form already positions its Arabic controls explicitly.
    # Mirroring the dialog reverses the original navigation/statistics layout.
    dialog.setLayoutDirection(Qt.LeftToRight if is_mushaf or not arabic else Qt.RightToLeft)
    if hasattr(dialog, "_modern_title"):
        dialog._modern_title.setText(dialog.windowTitle())
    if hasattr(dialog, "_modern_close"):
        dialog._modern_close.setText("إغلاق" if arabic else "Close")
    if is_mushaf:
        from gui.mushaf_view_dialog.presentation import update_stats_toggle
        update_stats_toggle(dialog._modern_ui, arabic)
    for widget in [dialog, *dialog.findChildren(QWidget)]:
        widget.setProperty("arabic", arabic)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.updateGeometry()
