class Node:
    def __init__(self, id=-1, index=-1, marker=None, edges=[], caption="", bCoorKnown=False, x=0, y=0, ic="Red",
                 bc="Black", shape="ellipse"):
        """
        Graph node initialization
        :param id: ID of graph node
        :param marker: Marker of this node
        :param edge(edge): Edges connected to the node(marker)
        """
        self.id = id  # Arbitrary sequenced number 0...+
        self.index = index  # marker.id
        self.marker = marker  # Marker obj
        self.edges = edges  # list of edges connected
        self.caption = caption
        self.bCoorKnown = bCoorKnown
        self.x = x
        self.y = y
        self.ic = ic
        self.bc = bc
        self.shape = shape

    def copy(self, idSet, edges=None):
        if edges is None:
            edges = self.edges
        return Node(id=idSet, index=self.index, marker=self.marker, edges=edges, caption=self.caption,
                    bCoorKnown=self.bCoorKnown, x=self.x, y=self.y, ic=self.ic, bc=self.bc, shape=self.shape)

    def edge_exist_to_node(self, node):  # def bExistEdgeToNodeID(self,idTo):
        """
        Checks if a given node is connected to this node
        :param node:
        :return: True if an edge exists, else false
        """
        for edge in self.edges:
            if edge.node1 == node or edge.node2 == node:
                return True
        return False

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_node_data(self):
        # 1 "pe0" ic LightGreen 0.5 0.5 box
        # 1 "NODE_1000_length_42440_cov_2.75993_B0" 16.165 -0.638 sh ellipse x_fact 1 y_fact 1 ic red bc black
        s = str(self.id) + " \"" + self.caption + "\"" # s = str(self.index) + " \"" + self.caption + "\""
        if self.bCoorKnown:
            s += ' ' + str(self.x)
            s += ' ' + str(self.y)
        s += " sh " + self.shape
        s += " ic " + self.ic
        s += " bc " + self.bc
        return s

    def bShape(self, shape):
        return True if shape in ["box", "ellipse", "triangle"] else False

    def __eq__(self, other):
        return self.index == other.index
