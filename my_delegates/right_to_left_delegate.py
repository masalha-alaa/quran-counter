from PySide6.QtWidgets import QStyledItemDelegate


class RightToLeftDelegate(QStyledItemDelegate):
    RLM_CHAR = "\u200F"  # Right-To-Left Mark
    def initStyleOption(self, opt, index):
        super().initStyleOption(opt, index)
        if not opt.text.startswith(self.RLM_CHAR):
            opt.text = self.RLM_CHAR + opt.text
