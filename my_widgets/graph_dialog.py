import networkx as nx
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QWidget


class NetworkXGraph(QWidget):
    def __init__(self, graph, bg):
        super().__init__()
        self.graph = graph
        # Create the matplotlib figure and axis
        self.figure, self.ax = plt.subplots(figsize=(5,5), facecolor=bg)
        self.ax.set_facecolor(bg)
        self.ax.axis('off')
        self.canvas = FigureCanvas(self.figure)
        plt.margins(x=0.4)

        # Draw graph on Matplotlib canvas
        nx.draw_networkx(self.graph, ax=self.ax, with_labels=True, node_color='#0066BE', edge_color='gray',
                 font_color="orange")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.canvas.draw()


class GraphDialog(QDialog):
    """ QDialog to display the NetworkX graph. """

    def __init__(self, graph, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Path")
        self.resize(700, 700)

        bg = "#313131"
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(NetworkXGraph(graph, bg))
        self.setLayout(layout)
