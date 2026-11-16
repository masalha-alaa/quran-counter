"""Keep a temporarily busy filter visually steady without enabling stale actions."""

from PySide6.QtCore import QObject
from PySide6.QtGui import QIcon


class SearchFilter(QObject):
    def __init__(self, button):
        super().__init__(button)
        self.button = button
        self.pending = False
        self._icon = QIcon(button.icon())
        self._busy_icon = QIcon(self._icon)
        ratio = button.devicePixelRatioF()
        pixmap = self._icon.pixmap(button.iconSize() * ratio)
        pixmap.setDevicePixelRatio(ratio)
        self._busy_icon.addPixmap(pixmap, QIcon.Disabled)

    def begin(self):
        # Keep the last settled appearance across overlapping searches. The
        # real button is disabled immediately, so it cannot filter old results.
        if not self.pending:
            hold_enabled = self.button.isEnabled()
            self.button.setProperty("pendingSearch", hold_enabled)
            if hold_enabled:
                self.button.setIcon(self._busy_icon)
        self.pending = True
        self.button.setEnabled(False)
        self._polish()

    def complete(self, available):
        self.pending = False
        self.button.setEnabled(available)
        self.button.setProperty("pendingSearch", False)
        self.button.setIcon(self._icon)
        self._polish()

    def _polish(self):
        self.button.style().unpolish(self.button)
        self.button.style().polish(self.button)
        self.button.update()
