from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QDialog, QApplication
from gui.relations_graph.relations_graph import Ui_RelationsGraphDialog
from PySide6.QtCore import Qt
from my_utils.utils import AppLang
from networkx import DiGraph
from matplotlib import pyplot as plt


class MyRelationsGraphDialog(QDialog, Ui_RelationsGraphDialog):
    def __init__(self, language: None | AppLang):
        super(MyRelationsGraphDialog, self).__init__()
        self.setupUi(self)
        self.expandedGraphCheckbox.setChecked(True)  # don't change initial value - otherwise graph will be messed up
        self._current_lang = None
        self.expanded = False
        self._apply_language(language)
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowMaximizeButtonHint |
                            Qt.WindowType.WindowMinimizeButtonHint)
        # Manually resize to the screen size
        screen_geometry = QApplication.primaryScreen().geometry()
        self.resize(screen_geometry.width(), screen_geometry.height())

        # Optionally center the dialog
        self.move(screen_geometry.topLeft())

        self.setup_events()

    def setup_events(self):
        self.expandedGraphCheckbox.stateChanged.connect(self._toggle_expanded_graph)

    def set_language(self, lang):
        self._apply_language(lang)

    def _apply_language(self, lang):
        if lang != self._current_lang:
            self.retranslateUi(self)
            # self.set_font_for_language(lang)
            self._current_lang = lang

    def set_data(self, graph: DiGraph):
        self.graphWidget.set_data(graph, "#313131", self._current_lang)

    # SIGNALS
    def _toggle_expanded_graph(self, state):
        plt.close()
        self._show_graph(self.expandedGraphCheckbox.isChecked())

    def showEvent(self, event):
        super().showEvent(event)
        self._show_graph(self.expandedGraphCheckbox.isChecked())

    def _show_graph(self, expanded=False):
        QTimer.singleShot(40, lambda: self.graphWidget.create_graph(expanded))  # solves white flicker problem

    def closeEvent(self, event):
        plt.close()
        event.accept()
