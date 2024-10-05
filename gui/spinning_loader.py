from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QColor
import sys


class SpinningLoader(QWidget):
    def __init__(self):
        super().__init__()
        self.hide()
        self.setMinimumSize(24, 24)  # Set minimum size for the widget
        self.angle = 0  # Angle for rotation
        self.timer = QTimer()
        self._is_started = False

    def update_angle(self):
        self.angle = (self.angle + 10) % 360  # Increment angle and wrap around
        self.update()  # Request a repaint

    def start(self):
        if not self._is_started:
            self.show()
            self.timer.timeout.connect(self.update_angle)
            self.timer.start(35)  # ms
            self._is_started = True

    def stop(self):
        if self._is_started:
            self.timer.stop()
            self.hide()
            self._is_started = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # Enable anti-aliasing

        # Draw a spinning circle
        center = self.rect().center()
        radius = 10  # Radius of the circle
        painter.setPen(QColor(0, 150, 150))  # Green color for the spinner
        painter.setBrush(Qt.BrushStyle.NoBrush)  # No fill color for the arc

        # Draw the spinner as an arc
        # Adjust the start angle and sweep angle to create a spinning effect
        painter.drawArc(center.x() - radius, center.y() - radius,
                        radius * 2, radius * 2,
                        int(self.angle * 16),  # Start angle
                        180 * 16)  # Sweep angle (120 degrees)
