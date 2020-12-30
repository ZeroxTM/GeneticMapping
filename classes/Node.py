from classes.Marker import Marker


class Node:
    def __init__(self, id=-1, marker=Marker(), edges=[], caption="", bCoorKnown=False, x=0, y=0):
        """
        Graph node initialization
        :param id: ID of graph node
        :param marker: Marker of this node
        :param edge(edge): Edges connected to the node(marker)
        """
        self.id = id
        self.marker = marker
        self.edges = edges
        self.caption = caption
        self.bCoorKnown = bCoorKnown
        self.x = x
        self.y = y
        self.ic = "red"
        self.bc = "black"
        self.shape = "ellipse"

    def check(self):
        print()

    def print(self):
        print()

    def add_edge(self, edge):
        self.edges.append(edge)

    def __eq__(self, other):
        return self.id == other.id
