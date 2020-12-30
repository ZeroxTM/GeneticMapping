"""
Genetic map network structure
"""
import itertools

from Macros import calculate_recombination_rate
from classes.Edge import Edge
from classes.Linkage import get_shared_alleles
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

    def create_edges(self, linkage_groups):
        """
        :param indexes_of_linkages: list of linkage (linkageGroup)
        :return:
        """
        id = -1
        node_id = -1

        for linkage in linkage_groups:
            for marker in linkage:
                node_id += 1
                self.addNode(Node(id=node_id, marker=marker))

        for linkage in linkage_groups:
            combinations = itertools.combinations(linkage, 2)
            for comb in combinations:
                ns = get_shared_alleles(comb[0].alleles, comb[1].alleles)
                if type(ns) != str:
                    recombination_rate = calculate_recombination_rate(ns[0], ns[1], ns[2], ns[3])
                    if recombination_rate <= 0.15:
                        id += 1
                        edge = Edge(id=id, start_node=comb[0], end_node=comb[1], recombination_rate=recombination_rate)
                        self.addEdge(edge)
                        node1 = next((node for node in self.nodes if node.marker == comb[0]), None)
                        node2 = next((node for node in self.nodes if node.marker == comb[1]), None)
                        node1.add_edge(edge)
                        node2.add_edge(edge)

        """
        combinations = itertools.combinations(self.nodes, 2)
        for comb in combinations:
            ns = get_shared_alleles(comb[0].alleles, comb[1].alleles)
            if type(ns) != str:
                recombination_rate = calculate_recombination_rate(ns[0], ns[1], ns[2], ns[3])
                if recombination_rate <= 0.15:
                    id += 1
                    edge = Edge(id=id, start_node=comb[0], end_node=comb[1],
                                recombination_rate=recombination_rate)
                    node1 = next((node for node in self.nodes if node.marker == comb[0]), None)
                    node2 = next((node for node in self.nodes if node.marker == comb[1]), None)
                    node1.add_edge(edge)
                    node2.add_edge(edge)
                    """
