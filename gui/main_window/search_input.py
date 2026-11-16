"""Arabic query editing independent of the UI and keyboard layout direction."""

from PySide6.QtCore import QCoreApplication, QEvent, QObject, Qt
from PySide6.QtGui import QKeyEvent

from my_utils.my_enums import AppLang


class SearchInput(QObject):
    def __init__(self, field):
        super().__init__(field)
        self.field = field
        self.language = AppLang.DEFAULT_LANGUAGE
        field.setLayoutDirection(Qt.RightToLeft)
        field.installEventFilter(self)
        field.textChanged.connect(self._align)
        self._set_text_direction()

    def _set_text_direction(self):
        # QLineEdit's widget direction only positions its chrome. Its internal
        # text control uses a separate paragraph direction, changed by these
        # native Qt direction keys. LTR paragraphs put Arabic trailing spaces
        # (and the caret) on the wrong side even though insertion is correct.
        QCoreApplication.sendEvent(self.field, QKeyEvent(
            QEvent.KeyPress, Qt.Key_Direction_R, Qt.NoModifier,
        ))

    def set_language(self, language):
        self.language = language
        self._align()

    def _align(self):
        hint_on_left = not self.field.text() and self.language == AppLang.ENGLISH
        self.field.setAlignment((Qt.AlignLeft if hint_on_left else Qt.AlignRight) | Qt.AlignAbsolute)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Direction_L:
            self._set_text_direction()
            return True
        return super().eventFilter(watched, event)
