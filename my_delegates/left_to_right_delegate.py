from PySide6.QtWidgets import QStyledItemDelegate


class LeftToRightDelegate(QStyledItemDelegate):
    LRM_CHAR = "\u200E"  # Left-To-Right Mark
    def initStyleOption(self, option, index):
        # https://stackoverflow.com/a/79182425/900394
        super().initStyleOption(option, index)
        if not option.text.startswith(self.LRM_CHAR):
            option.text = self.LRM_CHAR + option.text

    # def paint(self, painter, option, index):
    #     Works but messes up hover highlight
    #     painter.save()
    #     text_option = QTextOption()
    #     text_option.setTextDirection(Qt.LayoutDirection.LeftToRight)
    #     painter.drawText(option.rect, option.displayAlignment, index.data())
    #     painter.restore()
