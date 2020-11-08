"""
Genetic map network structure
"""


class Network:
    def __init__(self, node=None, edge=None, mst=None, skeleton=None, cutoff=None):
        """
        Genetic map network initialization
        :param node: list of Nodes in the network [Node[]]
        :param edge: list of Edges in the network [Edge[]]
        :param mst: list of Edges forming minimal spanning tree [Edge[]]
        :param skeleton: list of skeletal Nodes [Node[]]
        :param cutoff: cutoff [float]
        """
        self.node = node
        self.edge = edge
        self.mst = mst
        self.skeleton = skeleton
        self.cutoff = cutoff

    def calcMST(self):
        print()

    def checkConnection(self):
        print()
