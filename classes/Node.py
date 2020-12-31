from classes.Marker import Marker


class Node:
    def __init__(self, id=-1, index=-1, marker=Marker(), edges=[], caption="", bCoorKnown=False, x=0, y=0, ic="red",
                 bc="black", shape="ellipse"):
        """
        Graph node initialization
        :param id: ID of graph node
        :param marker: Marker of this node
        :param edge(edge): Edges connected to the node(marker)
        """
        self.id = id
        self.index = index
        self.marker = marker
        self.edges = edges
        self.caption = caption
        self.bCoorKnown = bCoorKnown
        self.x = x
        self.y = y
        self.ic = ic
        self.bc = bc
        self.shape = shape

    def copy(self, idSet):
        return Node(id=idSet, index=self.index, marker=self.marker, edges=self.edges, caption=self.caption,
                    bCoorKnown=self.bCoorKnown, x=self.x, y=self.y, ic=self.ic, bc=self.bc, shape=self.shape)

    def check(self):
        print()

    def print(self):
        print()

    def add_edge(self, edge):
        self.edges.append(edge)

    def printToFilePajek(self, index, file):
        # 1 "pe0" ic LightGreen 0.5 0.5 box
        # 1 "NODE_1000_length_42440_cov_2.75993_B0" 16.165 -0.638 sh ellipse x_fact 1 y_fact 1 ic red bc black
        s = str(index) + " \"" + self.caption + "\""
        if self.bCoorKnown:
            s += ' ' + str(self.x)
            s += ' ' + str(self.y)
        s += " sh " + self.shape
        s += " ic " + self.ic
        s += " bc " + self.bc
        file.write(s + '\n')

    def bShape(self, shape):
        return True if shape in ["box", "ellipse", "triangle"] else False

    def __eq__(self, other):
        return self.id == other.id
