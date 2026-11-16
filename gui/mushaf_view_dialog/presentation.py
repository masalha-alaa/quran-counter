"""Theme the original Mushaf form without moving or mirroring its controls."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QToolButton, QWidget

from gui.theme import STYLESHEET


# Preserve the form's compact controls and original typography hierarchy. The
# shared theme supplies the colors; its larger control padding would otherwise
# crowd the original navigation rows and the 85-pixel letter histogram.
MUSHAF_STYLESHEET = STYLESHEET + """
QDialog#MushafViewDialog QWidget { font-size: 17pt; }
QDialog#MushafViewDialog QFrame#frame_2,
QDialog#MushafViewDialog QFrame#frame_2 QWidget { font-size: 14pt; }
QDialog#MushafViewDialog QLabel#label_16 { font-size: 10pt; font-style: italic; }
QDialog#MushafViewDialog QFrame#frame_4,
QDialog#MushafViewDialog QFrame#frame_4 QWidget { font-size: 15pt; }
QDialog#MushafViewDialog QFrame#frame,
QDialog#MushafViewDialog QFrame#frame QWidget { font-size: 11pt; }
QDialog#MushafViewDialog QTableWidget,
QDialog#MushafViewDialog QHeaderView { font-size: 12pt; }
QDialog#MushafViewDialog QPushButton { padding: 2px; }
QDialog#MushafViewDialog QLineEdit { padding: 2px; }
QDialog#MushafViewDialog QCheckBox { padding: 0; }
QDialog#MushafViewDialog QTextBrowser,
QDialog#MushafViewDialog QTableWidget { padding: 0; }
QDialog#MushafViewDialog QHeaderView::section { padding: 4px; }
QDialog#MushafViewDialog QTableWidget::item { padding: 0; }
QToolButton#statsToggle { padding: 0; border-radius: 5px; }
"""


def style_mushaf(dialog, ui):
    # Keep every Designer layout, stretch factor, margin, widget constraint,
    # alignment and explicit direction. Only replace the old inline styling.
    for widget in dialog.findChildren(QWidget):
        widget.setStyleSheet("")
        if isinstance(widget, QFrame) and widget.frameShape() in (QFrame.HLine, QFrame.VLine):
            widget.setProperty("role", "separator")
    for frame in (ui.frame_2, ui.frame_4, ui.frame, ui.exclusiveWordsFrame, ui.frame_3):
        frame.setProperty("role", "panel")
    dialog.setStyleSheet(MUSHAF_STYLESHEET)

    # The sole addition to the existing layout: a small icon in the page bar.
    # It remains accessible while the stats frame is hidden. The histogram is
    # a separate sibling in the original form and is never hidden or moved.
    ui.stats_toggle = QToolButton(ui.frame_4)
    ui.stats_toggle.setObjectName("statsToggle")
    ui.stats_toggle.setFixedSize(24, 24)
    ui.stats_toggle.setCheckable(True)
    ui.stats_toggle.setChecked(True)
    ui.stats_toggle.setToolButtonStyle(Qt.ToolButtonIconOnly)
    ui.horizontalLayout_2.addWidget(ui.stats_toggle)

    def toggle(expanded):
        ui.frame.setVisible(expanded)
        update_stats_toggle(ui, bool(dialog.property("arabic")))

    ui.stats_toggle.toggled.connect(toggle)


def update_stats_toggle(ui, arabic):
    expanded = ui.stats_toggle.isChecked()
    ui.stats_toggle.setArrowType(Qt.UpArrow if expanded else Qt.DownArrow)
    text = ("إخفاء الإحصاءات" if expanded else "إظهار الإحصاءات") if arabic else (
        "Collapse statistics" if expanded else "Expand statistics"
    )
    ui.stats_toggle.setToolTip(text)
    ui.stats_toggle.setAccessibleName(text)
