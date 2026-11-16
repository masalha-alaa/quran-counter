"""Shared desktop theme, kept in Python so frozen builds need no extra assets."""

STYLESHEET = """
QWidget {
    color: #e7eaf1;
    font-family: "Segoe UI", "Noto Sans", sans-serif;
    font-size: 11pt;
}
QMainWindow, QDialog, QWidget#centralwidget, QWidget#readerStatistics { background: #15171c; }
QMessageBox { background: #1d2028; }
QWidget[arabic="true"] { font-family: "Noto Naskh Arabic"; font-size: 13pt; }
QLabel, QCheckBox, QRadioButton { background: transparent; }
QLabel[role="title"] { font-size: 16pt; font-weight: 600; color: #f4f5f9; }
QLabel[role="dialogTitle"] { font-size: 18pt; font-weight: 600; color: #f4f5f9; }
QLabel[role="statValue"] { font-size: 18pt; color: #a8c4ff; }
QFrame[role="panel"] { background: #1d2028; border: 1px solid #343945; border-radius: 10px; }
QFrame[role="separator"] { background: #343945; border: none; }
QLabel[role="muted"] { color: #a8b0c1; }
QLabel[role="statLabel"] { color: #a8b0c1; font-size: 11pt; }
QLabel[role="section"] { color: #c3ccdd; font-weight: 600; }
QLabel#brandMark { color: #a8c4ff; font-size: 20pt; }
QScrollArea#searchSidebar {
    background: #1d2028; border: 1px solid #343945; border-radius: 14px;
}
QWidget#searchModes { background: transparent; }
QLineEdit {
    background: #171a21; border: 1px solid #485162; border-radius: 8px;
    padding: 7px 10px; selection-background-color: #3c568a; selection-color: #ffffff;
}
QLineEdit:focus { border: 1px solid #a8c4ff; }
QLineEdit#searchWord { font-family: "Noto Naskh Arabic"; font-size: 18pt; padding: 4px 12px; }
QLineEdit[role="count"] {
    background: transparent; border: none; color: #a8c4ff; font-size: 14pt;
    font-family: "Segoe UI", "Noto Sans", sans-serif; font-weight: 600; padding: 0;
}
QLineEdit:disabled { color: #c3ccdd; background: #282e3a; }
QLineEdit#wordSum, QLineEdit#surahResultsSum, QLineEdit#topicSum { padding: 2px 8px; }
QPushButton, QToolButton {
    background: #2c3851; border: 1px solid #4b6085; border-radius: 8px;
    color: #e5edff; padding: 7px 12px;
}
QPushButton:hover, QToolButton:hover { background: #394b6d; border-color: #a8c4ff; }
QPushButton[role="primary"] { background: #a8c4ff; color: #182642; font-weight: 600; }
QPushButton[role="primary"]:hover { background: #c8daff; }
QPushButton[role="primary"]:disabled { background: #39414e; color: #929caf; }
QPushButton:pressed, QToolButton:pressed { background: #465f8c; }
QPushButton:focus, QToolButton:focus { border: 1px solid #c8d8ff; }
QPushButton:disabled { background: #282d37; border-color: #39414e; color: #929caf; }
QToolButton#browseButton { background: #a8c4ff; color: #182642; font-weight: 600; }
QToolButton#browseButton:hover { background: #c8daff; }
QToolButton#optionsButton:checked { background: #354a72; border-color: #a8c4ff; }
QCheckBox { spacing: 7px; padding: 4px; }
QRadioButton { spacing: 10px; padding: 7px 9px; border: 1px solid transparent; border-radius: 8px; }
QRadioButton:hover { background: #29313e; }
QRadioButton:checked { background: #2b3851; color: #c9dbff; border-color: #4b628a; }
QRadioButton:focus, QCheckBox:focus { border: 1px solid #a8c4ff; border-radius: 6px; }
QRadioButton:disabled, QCheckBox:disabled { color: #8792a6; }
QRadioButton::indicator, QCheckBox::indicator {
    width: 14px; height: 14px; border: 1px solid #8191ad; background: #171a21;
}
QRadioButton::indicator { border-radius: 8px; }
QCheckBox::indicator { border-radius: 4px; }
QRadioButton::indicator:checked, QCheckBox::indicator:checked {
    background: #a8c4ff; border: 3px solid #506994;
}
QSlider::groove:horizontal { background: #424c5e; height: 4px; border-radius: 2px; }
QSlider::handle:horizontal { background: #a8c4ff; width: 14px; margin: -5px 0; border-radius: 7px; }
QSlider::handle:horizontal:disabled { background: #758299; }
QSlider:focus { border: 1px solid #a8c4ff; border-radius: 4px; }
QTabWidget::pane { background: #1d2028; border: 1px solid #343945; border-radius: 10px; top: -1px; }
QTabBar::tab { background: transparent; color: #b0bdd3; padding: 6px 18px; border-bottom: 3px solid transparent; }
QTabBar::tab:selected { color: #a8c4ff; border-bottom-color: #a8c4ff; }
QTabBar::tab:hover { background: #28303f; }
QTextBrowser, QTableWidget, QListWidget {
    background: #191c23; alternate-background-color: #222731; color: #e7eaf1;
    border: none; border-radius: 8px; padding: 10px;
    selection-background-color: #354a72; selection-color: #f2f6ff; gridline-color: #343945;
}
QTextBrowser#foundVerses { font-family: "Noto Naskh Arabic"; font-size: 19pt; }
QTextBrowser[role="quran"] { font-family: "Noto Naskh Arabic"; font-size: 19pt; }
QLineEdit[role="arabicInput"] { font-family: "Noto Naskh Arabic"; font-size: 15pt; }
QListWidget::item { padding: 10px; border-radius: 6px; }
QListWidget::item:selected { background: #354a72; color: #f2f6ff; }
QProgressBar { border: 1px solid #485162; border-radius: 7px; background: #171a21; text-align: center; min-height: 24px; }
QProgressBar::chunk { background: #4b628a; border-radius: 6px; }
QScrollArea { background: transparent; border: none; }
QLabel#resultsPlaceholder { color: #a8b0c1; font-family: "Noto Naskh Arabic"; font-size: 19pt; background: transparent; }
QTableWidget::item { padding: 8px; border-bottom: 1px solid #313948; }
QTableWidget::item:selected { background: #354a72; color: #f2f6ff; }
QHeaderView { background: #2b3342; }
QHeaderView::section { background: #2b3342; color: #c5d3ed; border: none; padding: 9px; }
QTableCornerButton::section { background: #2b3342; border: none; }
QMenuBar { background: #15171c; color: #b0bdd3; padding: 3px 14px; }
QMenuBar::item { padding: 6px 10px; background: transparent; }
QMenuBar::item:selected, QMenu::item:selected { background: #334566; border-radius: 5px; }
QMenu { background: #222630; border: 1px solid #485162; padding: 6px; }
QMenu::item { padding: 7px 20px; }
QToolTip { background: #e6ecf8; color: #23334f; border: none; padding: 6px; font-size: 11pt; }
QScrollBar:vertical { background: transparent; width: 8px; margin: 2px; }
QScrollBar:horizontal { background: transparent; height: 8px; margin: 2px; }
QScrollBar::handle { background: #53627a; border-radius: 3px; min-height: 24px; min-width: 24px; }
QScrollBar::handle:hover { background: #8295b5; }
QScrollBar::add-line, QScrollBar::sub-line { width: 0; height: 0; }
QScrollBar::add-page, QScrollBar::sub-page { background: transparent; }
"""
