"""
Genetic map network structure
"""
from classes.Marker import Marker
from classes.Node import Node


class Network:
    def __init__(self, nodes=[], edges=[], mst=None, skeleton=None, cutoff=0.5):
        """
        Genetic map network initialization
        :param node: list of Nodes in the network [Node[]]
        :param edge: list of Edges in the network [Edge[]]
        :param mst: list of Edges forming minimal spanning tree [Edge[]]
        :param skeleton: list of skeletal Nodes [Node[]]
        :param cutoff: cutoff [float]
        """
        self.nodes = nodes
        self.edges = edges
        self.mst = mst
        self.skeleton = skeleton
        self.cutoff = cutoff

    def MST(self):
        print()

    def calcRanksOfNodes(self, idNodeStart, bPrint):
        pass

    def checkConnection(self):
        print()

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)
