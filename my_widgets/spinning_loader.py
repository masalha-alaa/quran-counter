from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QColor, QPen, QFont


class SpinningLoader(QWidget):
    def __init__(self, radius=20):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        self.hide()
        self.radius = radius
        self.setMinimumSize(24, 24)  # Set minimum size for the widget
        self.angle = 0  # Angle for rotation
        self.timer = QTimer()
        self._is_started = False
        self.text = ""  # Text to display below the spinner

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

    def setText(self, text):
        """Set the text to display below the spinner."""
        self.text = text
        self.update()  # Repaint the widget

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # Enable anti-aliasing

        # Draw a spinning circle
        center = self.rect().center()
        radius = self.radius  # Radius of the circle
        pen = QPen(QColor(0, 150, 150))
        pen.setWidth(4)
        painter.setPen(pen)  # Green color for the spinner
        painter.setBrush(Qt.BrushStyle.NoBrush)  # No fill color for the arc

        # Draw the spinner as an arc
        # Adjust the start angle and sweep angle to create a spinning effect
        painter.drawArc(center.x() - radius, center.y() - radius,
                        radius * 2, radius * 2,
                        int(self.angle * 16),  # Start angle
                        180 * 16)  # Sweep angle (120 degrees)

        # Draw the text below the spinner
        if self.text:
            font = QFont("Arial", 10)
            painter.setFont(font)
            text_width = painter.fontMetrics().horizontalAdvance(self.text)
            text_height = painter.fontMetrics().height()
            text_x = center.x() - (text_width // 2)
            text_y = center.y() + radius + (text_height // 2) + 10
            painter.drawText(text_x, text_y, self.text)
