import matplotlib.pyplot as plt
import networkx as nx
from PySide6.QtWidgets import QWidget, QLabel
from bidi.algorithm import get_display
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from algos.related_words import RelatedWords
from arabic_reformer import reform_text
from my_utils.my_enums import AppLang


class NodeRoleAttribute:
    SOURCE = 'source'
    DESTINATION = 'destination'
    LEAF = 'leaf'


class NodeAttributeInfo:
    def __init__(self, name, atts):
        self.name = name
        self.atts = atts


class NodeAttribute:
    role = NodeAttributeInfo('role', NodeRoleAttribute)


class NetworkXGraph(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.graph: nx.DiGraph|None = None
        self.bg = ''
        self.figure = None
        self.ax = None
        self.canvas = None
        self._current_lang = None
        self.initialized = False

    def set_data(self, graph, bg, language):
        self.graph = graph
        self.bg = bg
        self._current_lang = language
        self.initialized = True

    def create_graph(self, show_leafs=False):
        if not self.initialized:
            raise Exception('Graph must be initialized before creating a networkx graph')
        # Create the matplotlib figure and axis
        if self.ax is None:
            self.figure, self.ax = plt.subplots(facecolor=self.bg)
            self.ax.set_facecolor(self.bg)
            self.canvas = FigureCanvas(self.figure)
        else:
            self.ax.clear()
        self.ax.margins(0.2)
        self.ax.axis('off')

        # node_mapping = {n: n.replace(" ", "\n") for n in self.graph.nodes()}
        # self.graph = nx.relabel_nodes(self.graph, node_mapping)

        # Draw graph on Matplotlib canvas
        pos = nx.bfs_layout(self.graph,
                            [n for n, d in self.graph.nodes(data=True) if
                             d.get(NodeAttribute.role.name) == NodeAttribute.role.atts.SOURCE][0],
                            align='horizontal')
        # rotate 180
        pos = {node: (-x, -y) for node, (x, y) in pos.items()}

        # put path nodes in the middle horizontally
        current_y = 0
        current_y_nodes = []
        path_node = None
        def _flip(path_node_):
            if path_node_ is not None:
                center_node = current_y_nodes[len(current_y_nodes) // 2]
                temp_x = pos[center_node][0]
                pos[center_node] = (pos[path_node_][0], pos[center_node][1])
                pos[path_node_] = (temp_x, pos[path_node_][1])

        for k, v in pos.items():
            if v[1] != current_y:
                if path_node is not None:
                    _flip(path_node)
                    path_node = None

                current_y = v[1]
                current_y_nodes = []
            if v[1] == current_y:
                current_y_nodes.append(k)
                if self.graph.nodes[k].get(NodeAttribute.role.name) != NodeAttribute.role.atts.LEAF:
                    path_node = k

        # flip last level
        if path_node is not None:
            _flip(path_node)

        outline_nodes, leaf_nodes, other_nodes = {}, {}, {}
        for node in self.graph.nodes():
            if self.graph.nodes[node].get(NodeAttribute.role.name) in [NodeAttribute.role.atts.SOURCE,
                                                                       NodeAttribute.role.atts.DESTINATION]:
                outline_nodes[node] = node
            elif self.graph.nodes[node].get(NodeAttribute.role.name) == NodeAttribute.role.atts.LEAF:
                leaf_nodes[node] = node
            else:
                other_nodes[node] = node

        # Draw transparent edges if not show_leafs and edge connects a leaf
        edges_alpha = []
        for e in self.graph.edges():
            if not show_leafs and (e[0] in leaf_nodes or e[1] in leaf_nodes):
                edges_alpha.append(0.0)
            else:
                edges_alpha.append(1.0)

        nx.draw_networkx_edges(self.graph, pos, ax=self.ax,
                               arrows=False,
                               edge_color="gray",
                               alpha=edges_alpha,
                               hide_ticks=False)
        nx.draw_networkx_nodes(self.graph, pos, ax=self.ax,
                               nodelist=other_nodes,
                               node_color='#0066BE',
                               node_size=2200,
                               hide_ticks=False)
        nx.draw_networkx_nodes(self.graph, pos, ax=self.ax,
                               nodelist=outline_nodes,
                               node_color='#0066BE',
                               edgecolors='#0086DE',
                               linewidths=2,
                               node_size=2200,
                               hide_ticks=False)
        nx.draw_networkx_nodes(self.graph, pos, ax=self.ax,
                               nodelist=leaf_nodes,
                               node_color='#0066BE',
                               alpha=0.5 * show_leafs,  # transparent leafs if not show leafs
                               node_size=1500,
                               hide_ticks=False)

        # Draw labels with custom font weight
        for i, (node, (x, y)) in enumerate(pos.items()):
            # don't print leafs text if not show leafs
            if not show_leafs and node in leaf_nodes:
                continue
            font_weight = 'bold' if node in outline_nodes else 'normal'
            if self._current_lang == AppLang.ENGLISH:
                label = RelatedWords.arb_to_eng.get(node, node)
                label = self._break_label(label)
            else:
                label = self._break_label(node)
                label = self.fix_arabic(label)
            self.ax.text(x, y, label, fontsize=12, fontweight=font_weight,
                             ha='center', va='center', color='orange')

        self.ax.text(-0.15, 0,
                     "Data from http://corpus.quran.com",
                     fontstyle='italic',
                     transform=self.ax.transAxes)

        # Layout
        self.canvas.draw()  # necessary?
        self.layout().addWidget(self.canvas)

    def _break_label(self, label):
        return label.replace(" ", "\n").replace("-", "\n")

    def re_order_nodes_straight_path(self, pos):
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

    def re_order_nodes(self, G, leaf_spacing=6, y_spacing=4):
        # Extract nodes by role

        source = [n for n, d in G.nodes(data=True) if d.get(NodeAttribute.role.name) == NodeAttribute.role.atts.SOURCE]
        destination = [n for n, d in G.nodes(data=True) if
                       d.get(NodeAttribute.role.name) == NodeAttribute.role.atts.DESTINATION]
        path_nodes = [n for n, d in G.nodes(data=True) if d.get(NodeAttribute.role.name) is None]
        leaf_nodes = [n for n, d in G.nodes(data=True) if
                      d.get(NodeAttribute.role.name) == NodeAttribute.role.atts.LEAF]

        if len(source) != 1 or len(destination) != 1:
            raise ValueError("Graph must have exactly one source and one destination node.")

        source = source[0]
        destination = destination[0]

        # Sort path nodes by insertion order (they are added in this order by default)
        path_nodes = [n for n in G.nodes if n in path_nodes]

        # Arrange layers
        layers = {source: 0, destination: len(path_nodes) + 1}

        for i, node in enumerate(path_nodes):
            layers[node] = i + 1

        # Positioning
        pos = {}

        # Source position (top-center)
        pos[source] = (0, (len(path_nodes) + 2) * y_spacing)

        # Path positions (in a straight line)
        for i, node in enumerate(path_nodes):
            pos[node] = (0, (len(path_nodes) - i + 1) * y_spacing)

        # Destination position (bottom-center)
        pos[destination] = (0, 0)

        # Place leaves around their parent
        for node in leaf_nodes:
            parent = next(G.predecessors(node), None)
            if parent is not None:
                siblings = list(G.successors(parent))
                index = siblings.index(node)
                offset = (index - len(siblings) / 2) * leaf_spacing
                pos[node] = (pos[parent][0] + offset, pos[parent][1] - 0.5 * y_spacing)
        return pos

    def fix_arabic(self, w):
        return get_display(reform_text(w))
