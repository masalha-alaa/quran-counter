"""A localized empty-state hint without changing the results document.

QTextEdit's native placeholder ignores document paragraph alignment. A passive
viewport label avoids putting instructional text into selectable/searchable
results, and disappears as soon as the document has content.
"""

from PySide6.QtCore import QEvent, QObject, Qt
from PySide6.QtWidgets import QLabel


class ResultsPlaceholder(QObject):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        browser.setPlaceholderText("")
        self.label = QLabel(browser.viewport())
        self.label.setObjectName("resultsPlaceholder")
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignAbsolute)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        browser.viewport().installEventFilter(self)
        browser.textChanged.connect(self._refresh)
        self._refresh()

    def set_text(self, text, *, right_aligned=True):
        self.label.setText(text)
        self.label.setAlignment((Qt.AlignRight if right_aligned else Qt.AlignLeft) | Qt.AlignTop | Qt.AlignAbsolute)
        self._refresh()

    def _refresh(self):
        margin = int(self.browser.document().documentMargin())
        self.label.setGeometry(self.browser.viewport().rect().adjusted(margin, margin, -margin, -margin))
        self.label.setVisible(self.browser.document().isEmpty())

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Resize:
            self._refresh()
        return super().eventFilter(watched, event)
