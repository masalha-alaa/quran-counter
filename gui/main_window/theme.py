"""Main-window theme, kept in Python so frozen builds need no extra assets."""

STYLESHEET = """
QWidget {
    color: #e6eeeb;
    font-family: "Segoe UI", "Noto Sans", sans-serif;
    font-size: 11pt;
}
QMainWindow, QWidget#centralwidget { background: #101b1d; }
QWidget[arabic="true"] { font-family: "Noto Naskh Arabic"; font-size: 13pt; }
QLabel, QCheckBox, QRadioButton { background: transparent; }
QLabel[role="title"] { font-size: 22pt; font-weight: 600; color: #f3f4e9; }
QLabel[role="subtitle"], QLabel[role="muted"] { color: #9fb6b1; }
QLabel[role="subtitle"], QLabel[role="statLabel"] { color: #9fb6b1; font-size: 10pt; }
QLabel[role="section"] { color: #b8d2c9; font-weight: 600; }
QLabel#brandMark { color: #8de0bd; font-size: 30pt; }
QFrame[role="card"], QScrollArea#searchSidebar {
    background: #172629; border: 1px solid #2b4142; border-radius: 14px;
}
QWidget#searchModes { background: transparent; }
QFrame[role="stat"] { background: #1a2e30; border: 1px solid #304746; border-radius: 12px; }
QLineEdit {
    background: #101f22; border: 1px solid #3a5353; border-radius: 8px;
    padding: 7px 10px; selection-background-color: #34755e; selection-color: #ffffff;
}
QLineEdit:focus { border: 1px solid #8de0bd; }
QLineEdit#searchWord { font-family: "Noto Naskh Arabic"; font-size: 22pt; padding: 8px 14px; }
QLineEdit[role="count"] {
    background: transparent; border: none; color: #8de0bd; font-size: 26pt;
    font-family: "Segoe UI", "Noto Sans", sans-serif; font-weight: 600; padding: 0;
}
QLineEdit:disabled { color: #b8d2c9; background: #203438; }
QLineEdit#wordSum, QLineEdit#surahResultsSum, QLineEdit#topicSum { padding: 2px 8px; }
QPushButton, QToolButton {
    background: #24473e; border: 1px solid #3c6556; border-radius: 8px;
    color: #e0f4e9; padding: 7px 12px;
}
QPushButton:hover, QToolButton:hover { background: #305b4c; border-color: #8de0bd; }
QPushButton:pressed, QToolButton:pressed { background: #386e59; }
QPushButton:focus, QToolButton:focus { border: 1px solid #c8ddb5; }
QPushButton:disabled { background: #223133; border-color: #304244; color: #829894; }
QToolButton#browseButton { background: #a6e5c4; color: #122b25; font-weight: 600; }
QToolButton#browseButton:hover { background: #c4f1d8; }
QCheckBox { spacing: 7px; padding: 4px; }
QRadioButton { spacing: 10px; padding: 7px 9px; border: 1px solid transparent; border-radius: 8px; }
QRadioButton:hover { background: #223a3a; }
QRadioButton:checked { background: #24453e; color: #b5efcd; border-color: #3b6556; }
QRadioButton:focus, QCheckBox:focus { border: 1px solid #8de0bd; border-radius: 6px; }
QRadioButton:disabled, QCheckBox:disabled { color: #728b86; }
QRadioButton::indicator, QCheckBox::indicator {
    width: 14px; height: 14px; border: 1px solid #6f9187; background: #101f22;
}
QRadioButton::indicator { border-radius: 8px; }
QCheckBox::indicator { border-radius: 4px; }
QRadioButton::indicator:checked, QCheckBox::indicator:checked {
    background: #9de0bb; border: 3px solid #426c58;
}
QSlider::groove:horizontal { background: #364d4b; height: 4px; border-radius: 2px; }
QSlider::handle:horizontal { background: #a6e5c4; width: 14px; margin: -5px 0; border-radius: 7px; }
QSlider::handle:horizontal:disabled { background: #647b77; }
QSlider:focus { border: 1px solid #8de0bd; border-radius: 4px; }
QTabWidget::pane { background: #172629; border: 1px solid #2b4142; border-radius: 10px; top: -1px; }
QTabBar::tab { background: transparent; color: #a3bdb5; padding: 10px 20px; border-bottom: 3px solid transparent; }
QTabBar::tab:selected { color: #a6e5c4; border-bottom-color: #a6e5c4; }
QTabBar::tab:hover { background: #203638; }
QTextBrowser, QTableWidget {
    background: #142225; alternate-background-color: #1b2d30; color: #e6eeeb;
    border: none; border-radius: 8px; padding: 10px;
    selection-background-color: #335b4c; selection-color: #f0fff5; gridline-color: #2b4142;
}
QTextBrowser#foundVerses { font-family: "Noto Naskh Arabic"; font-size: 19pt; }
QTableWidget::item { padding: 8px; border-bottom: 1px solid #263e3f; }
QTableWidget::item:selected { background: #335b4c; color: #f0fff5; }
QHeaderView { background: #213a3b; }
QHeaderView::section { background: #213a3b; color: #b9d8cb; border: none; padding: 9px; }
QTableCornerButton::section { background: #213a3b; border: none; }
QMenuBar { background: #101b1d; color: #a3bdb5; padding: 3px 14px; }
QMenuBar::item { padding: 6px 10px; background: transparent; }
QMenuBar::item:selected, QMenu::item:selected { background: #2b5146; border-radius: 5px; }
QMenu { background: #1a2e30; border: 1px solid #3a5353; padding: 6px; }
QMenu::item { padding: 7px 20px; }
QToolTip { background: #e3f0e6; color: #17382e; border: none; padding: 6px; font-size: 11pt; }
QScrollBar:vertical { background: transparent; width: 8px; margin: 2px; }
QScrollBar:horizontal { background: transparent; height: 8px; margin: 2px; }
QScrollBar::handle { background: #46645d; border-radius: 3px; min-height: 24px; min-width: 24px; }
QScrollBar::handle:hover { background: #719588; }
QScrollBar::add-line, QScrollBar::sub-line { width: 0; height: 0; }
QScrollBar::add-page, QScrollBar::sub-page { background: transparent; }
"""
