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
        self.figure, self.ax = plt.subplots(facecolor=bg)
        self.ax.set_facecolor(bg)
        self.ax.axis('off')
        self.canvas = FigureCanvas(self.figure)
        plt.margins(x=0.4)

        # Draw graph on Matplotlib canvas
        pos = self.re_order_nodes(nx.spring_layout(self.graph))  # Layout for consistent node positions
        outline_nodes = [(g_nodes := list(self.graph))[0]] + [g_nodes[-1]]
        nx.draw_networkx(self.graph, pos, ax=self.ax,
                         with_labels=False,
                         node_color='#0066BE',
                         font_color="orange",
                         node_size=2000,
                         edge_color='gray',)
        nx.draw_networkx_nodes(self.graph, pos,
                               nodelist=outline_nodes,
                               node_color='#0066BE',
                               edgecolors='#0086DE',
                               linewidths=2,
                               node_size=2000,)
        # Draw labels with custom font weight
        for i, (node, (x, y)) in enumerate(pos.items()):
            font_weight = 'bold' if i in [0, len(pos) - 1] else 'normal'
            plt.text(x, y, str(node), fontsize=12, fontweight=font_weight,
                     ha='center', va='center', color='orange')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.canvas.draw()

    def re_order_nodes(self, pos):
        pos_keys = list(pos)
        first_node_y = pos[pos_keys[0]][1]
        last_node_y = pos[pos_keys[-1]][1]
        if first_node_y < last_node_y:
            new_pos = {}
            p = 0
            q = len(pos_keys) - 1
            while p < len(pos_keys) and q >= 0:
                new_pos[pos_keys[p]] = pos[pos_keys[q]]
                p += 1
                q -= 1
            return new_pos
        return pos


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
