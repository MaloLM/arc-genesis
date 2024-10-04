from abstract_and_reason.assets import calculate_center


class Node:
    def __init__(self, value, x, y) -> None:
        self.value = value
        self.coords = [(x, y)]
        self.connections = []
        self.conn_dists = []
        self.entropies = []
        self.norm_entropies = []

    def get_node_center(self):
        coords = []
        for coord in self.coords:
            coords.append((coord[0], coord[1]))

        return calculate_center(coords)

    def add_connection(self, other_node):

        if other_node not in self.connections:
            self.connections.append(other_node)

    def __hash__(self):
        return hash((self.value, tuple(self.coords)))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value and self.coords == other.coords
        return False

    def __str__(self) -> str:
        coords_str = ";".join([f"({x},{y})" for x, y in self.coords])
        return f"Coords=[{coords_str}], Value={self.value}"
