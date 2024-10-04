from abstract_and_reason.assets import manhattan_distance, calculate_center, shuffle_list, arc_agi_colormap
from .node import Node
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import plotly.graph_objs as go
import networkx as nx


class Graph:

    def __init__(self, board) -> None:
        self.board = board
        self.nodes = []
        self.color_map = arc_agi_colormap
        self.to_nodes()
        self.check_node_integrity()

        self.distribution = None
        self.entropies = None
        self.min_entropy = None
        self.max_entropy = None

        self.compute_distances()
        self.compute_distribution()
        self.compute_entropies()
        self.attach_entropies_to_connections()

    def compute_distribution(self):
        connections = []
        for node in self.nodes:
            for conn in node.connections:
                connections.append(
                    (node.value, conn.value, node.conn_dists[node.connections.index(conn)]))

        total_connections = len(connections)
        connection_counts = Counter(connections)
        self.distribution = {k: v/total_connections for k,
                             v in connection_counts.items()}

    def compute_entropies(self):
        self.entropies = {k: -p * np.log2(p)
                          for k, p in self.distribution.items()}

        self.min_entropy = min(self.entropies.values()) if len(
            self.entropies.values()) > 0 else 0
        self.max_entropy = max(self.entropies.values()) if len(
            self.entropies.values()) > 0 else 0

    def attach_entropies_to_connections(self):
        if self.entropies is not None:
            for node in self.nodes:
                for i, connection in enumerate(node.connections):
                    res = (node.value, connection.value, node.conn_dists[i])
                    entropy = self.entropies[res]
                    node.entropies.append(entropy)
                    normalized_entropy = 1 - (
                        entropy - self.min_entropy) / (self.max_entropy - self.min_entropy)
                    node.norm_entropies.append(normalized_entropy)

                assert len(node.entropies) == len(
                    node.connections) and len(node.norm_entropies) == len(
                    node.connections), f"Bizzare... pas autant d'entropies que de connexions? {len(node.norm_entropies)} vs {len(node.connections)} et {len(node.entropies)} vs {len(node.connections)}"

    def check_node_integrity(self):
        summing = 0
        for node in self.nodes:
            summing += len(node.connections)

            nb_nodes = len(self.nodes)

        assert summing == nb_nodes * \
            (nb_nodes-1), "Bizare ? Il y a un problème entre le nombre de connexions réelles et le nombre de connexions attendues..."

    def to_nodes(self):
        for x, row in enumerate(self.board):
            for y, _ in enumerate(row):
                new_node = Node(self.board[x][y], x, y)
                self.nodes.append(new_node)
        self.connect_nodes()

    def compute_distances(self):
        for node in self.nodes:
            center = node.get_node_center()
            for conn in node.connections:
                node_center = calculate_center(conn.coords)
                distance = manhattan_distance(
                    center[0], center[1], node_center[0], node_center[1])
                node.conn_dists.append(distance)

    def get_nodes_coords(self):
        coords = []
        for node in self.nodes:
            coords.append(node.coords)
        return coords

    def connect_nodes(self):
        for current_node in self.nodes:
            for other_node in self.nodes:
                if other_node != current_node:
                    current_node.add_connection(other_node)
                    other_node.add_connection(current_node)

    def graph_network_to_board(self):
        nb_nodes = len(self.nodes)
        colors_idx = [node for node in range(nb_nodes)]
        colors_idx = shuffle_list(colors_idx)
        filled_array = np.full(self.board.shape, -1)

        for i, node in enumerate(self.nodes):
            for coord in node.coords:
                x = coord[0]
                y = coord[1]
                filled_array[x][y] = colors_idx[i]

        return filled_array

    def draw(self):
        G = nx.Graph()

        for node in self.nodes:
            G.add_node(node, label=node.value)

        for node in self.nodes:
            for connected_node in node.connections:
                if not G.has_edge(node, connected_node):
                    entropy = node.norm_entropies[node.connections.index(
                        connected_node)]

                    G.add_edge(
                        node, connected_node, weight=entropy, alpha=entropy)

        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
        edge_alphas = [G[u][v]['alpha'] for u, v in G.edges()]

        max_weight = max(edge_weights) if edge_weights else 1

        edge_widths = [w / max_weight * 1 for w in edge_weights]

        plt.figure(figsize=(16, 12), facecolor="#2b2d31")

        pos = nx.spring_layout(G)

        node_colors = [self.color_map[node.value] for node in G.nodes()]

        nx.draw_networkx_nodes(G, pos, node_size=500, node_color=node_colors)

        nx.draw_networkx_edges(G, pos, width=edge_widths,
                               edge_color='#dddddd', label='', alpha=edge_alphas)

        plt.title('Graph Network Visualization', color="#dddddd")
        plt.axis('off')
        plt.show()

    def draw_with_plotly(self):
        G = nx.Graph()

        for node in self.nodes:
            G.add_node(node, label=node.value)

        for node in self.nodes:
            for connected_node in node.connections:
                if not G.has_edge(node, connected_node):
                    entropy = node.entropies[node.connections.index(
                        connected_node)]
                    normalized_entropy = 1 - \
                        (entropy - self.min_entropy) / \
                        (self.max_entropy - self.min_entropy)
                    G.add_edge(
                        node, connected_node, weight=normalized_entropy, alpha=normalized_entropy)

        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
        edge_alphas = [G[u][v]['alpha'] for u, v in G.edges()]
        max_weight = max(edge_weights) if edge_weights else 1
        edge_widths = [w / max_weight * 5 for w in edge_weights]

        pos = nx.spring_layout(G, dim=3)

        x_edges = []
        y_edges = []
        z_edges = []
        edge_widths_trace = []
        edge_opacity_trace = []

        for i, edge in enumerate(G.edges()):
            x0, y0, z0 = pos[edge[0]]
            x1, y1, z1 = pos[edge[1]]
            x_edges += [x0, x1, None]
            y_edges += [y0, y1, None]
            z_edges += [z0, z1, None]
            edge_widths_trace.append(edge_widths[i])
            edge_opacity_trace.append(edge_alphas[i])

        edge_trace = go.Scatter3d(
            x=x_edges,
            y=y_edges,
            z=z_edges,
            mode='lines',
            # Use the first width as a default
            line=dict(color='lightgrey', width=edge_widths_trace[0]),
            # Use the first opacity as a default
            opacity=edge_opacity_trace[0],
            hoverinfo='none',
            name='Edges'
        )

        node_trace = go.Scatter3d(
            x=[pos[n][0] for n in G.nodes()],
            y=[pos[n][1] for n in G.nodes()],
            z=[pos[n][2] for n in G.nodes()],
            mode='markers',
            marker=dict(
                size=8,
                color=[self.color_map[node.value] for node in G.nodes()],
                colorscale='Viridis'
            ),
            text=[f'Node: {node.value}' for node in G.nodes()],
            hoverinfo='text',
            name='Nodes'
        )

        layout = go.Layout(
            title="Graph Network Visualization in 3D",
            showlegend=False,
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                bgcolor="#000000"
            ),
            margin=dict(l=0, r=0, b=0, t=50),
            height=800,
            width=800,
            updatemenus=[dict(
                type="buttons",
                direction="right",
                buttons=[
                    dict(
                        args=[{"visible": [True, True]}, {
                            "line.width": edge_widths_trace, "opacity": edge_opacity_trace}],
                        label="Show Edges",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, True]}],
                        label="Hide Edges",
                        method="update"
                    )
                ],
                font={
                    "color": "#dddddd"
                },
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0,  # Position at the far right
                xanchor="left",
                y=0,  # Position at the bottom
                yanchor="bottom",
                bgcolor="#2d2d2d",
                borderwidth=1,
                bordercolor="lightgrey"
            )],
            paper_bgcolor="#2d2d2d",
            font=dict(color="white")
        )

        fig = go.Figure(data=[edge_trace, node_trace], layout=layout)
        fig.show()
