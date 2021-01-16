"""
Genetic map network structure
"""
import copy
import itertools
import random

from Macros import calculate_recombination_rate
from classes.Edge import Edge
from classes.Linkage import get_shared_alleles
from classes.Node import Node


class Network:
    low_quality_markers = 0
    no_data_markers = 0
    pajek_color = ['GreenYellow', 'Yellow', 'Goldenrod', 'Dandelion', 'Apricot', 'Peach', 'Melon', 'YellowOrange',
                   'Orange', 'BurntOrange', 'Bittersweet', 'RedOrange', 'Mahogany', 'Red', 'OrangeRed', 'RubineRed',
                   'WildStrawberry', 'Fuchsia', 'Lavender', 'Thistle', 'Orchid', 'DarkOrchid', 'Purple', 'Plum',
                   'Violet', 'RoyalPurple', 'BlueViolet', 'Periwinkle', 'CadetBlue', 'CornflowerBlue', 'MidnightBlue',
                   'NavyBlue', 'RoyalBlue', 'Blue', 'Cerulean', 'Cyan', 'ProcessBlue', 'SkyBlue']

    def __init__(self, nodes=[], edges=[], mst=None, skeleton=None, cutoff=0.15):
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


    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)

    def initialize_network(self, linkage_groups, filterate=False):
        """
        :param indexes_of_linkages: list of linkage (linkageGroup)
        :return:
        """
        Network.low_quality_markers = 0
        Network.no_data_markers = 0
        id = -1
        node_id = -1
        print("\nAdding Nodes to the network ..\n")
        random.shuffle(Network.pajek_color)
        for i, linkage_group in enumerate(linkage_groups):
            print("\nAdding nodes to network from linkage: " + str(linkage_group.id) + "\n")
            for marker in linkage_group.markers:
                if len(marker.alleles) != 0:
                    if filterate:
                        if marker.segregation < 3.84 and marker.p_missing < 0.2:  # Filter out markers with no data, and low quality markers (segregation quality X^2 > 3.84 or pmiss > 20%)
                            node_id += 1
                            self.addNode(
                                Node(id=node_id, index=marker.id, marker=marker, edges=[], ic=Network.pajek_color[i],
                                     caption=marker.name))
                        else:
                            Network.low_quality_markers += 1
                    else:
                        node_id += 1
                        self.addNode(
                            Node(id=node_id, index=marker.id, marker=marker, edges=[], ic=Network.pajek_color[i],
                                 caption=marker.name))
                else:
                    Network.no_data_markers += 1
        print("\nDone Adding Nodes to the network!")
        print("\nAdding edges to the network ..\n")
        l = []
        for linkage_group in linkage_groups:
            print("\nAdding Edges to network from linkage group: " + str(linkage_group.id))
            l.append(linkage_group.markers)
        if filterate:
            l = [marker for linkage_markers in l for marker in linkage_markers if len(marker.alleles) != 0 if marker.segregation < 3.84 and marker.p_missing < 0.2]
        else:
            l = [marker for linkage_markers in l for marker in linkage_markers if len(marker.alleles) != 0]
        combinations = itertools.combinations(l, 2)
        for comb in combinations:
            ns = get_shared_alleles(comb[0].alleles, comb[1].alleles)
            if type(ns) != str:
                recombination_rate = calculate_recombination_rate(ns[0], ns[1], ns[2], ns[3])
                if recombination_rate <= self.cutoff:
                    id += 1
                    print("Recombination rate: " + str(recombination_rate) + "")
                    node1 = next((node for node in self.nodes if node.marker == comb[0]), None)
                    node2 = next((node for node in self.nodes if node.marker == comb[1]), None)
                    edge = Edge(id=id, start_node=node1, end_node=node2, recombination_rate=recombination_rate)
                    self.addEdge(edge)
                    print("Added edge ID " + str(edge.id) + " to network.")
                    node1.add_edge(edge)
                    node2.add_edge(edge)
                    print("Added edge to nodes[" + str(node1.id) + "," + str(node2.id) + "]")

        print("Network was built successfully")
        print(f"Network:\n\t#Nodes: {len(self.nodes)}\n\t#Edges:{len(self.edges)}")

    def get_node(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node

    """
        find mst fo this network
        """

    def calc_MST_net(self, bPrint=False, bPrintDetails=False):
        mst_net = Network(nodes=[], edges=[], mst=None, skeleton=None, cutoff=0.5)
        for i, node in enumerate(self.nodes):
            mst_net.addNode(node.copy(i, edges=[]))

        if len(self.edges) < 1:
            return mst_net

        # rank in MST
        rankInMST = [-1] * (len(self.nodes))
        idEdgeShortestFromMST = [-1] * (len(self.nodes))
        if bPrint:
            print("Minimal spanning tree (MST) for net with nNodes=" + str(len(self.nodes)) + " and nEdges=" + str(
                len(self.edges)) + "...")

        i = 0
        rankInMST[i] = 0  # rankInMST[i] = r = 0
        linkedWithMST = []
        node = self.nodes[i]
        idsNodeInMST = [i]
        for edge in node.edges:
            end_node_id = edge.get_end_node(node).id  # k = edge.idNodeEnd(i) #
            if end_node_id > i:
                linkedWithMST.append(end_node_id)
                idEdgeShortestFromMST[end_node_id] = edge.id

        while len(linkedWithMST) > 0:
            bStop = False
            iNodeAdd = linkedWithMST[0]
            minLength = self.edges[idEdgeShortestFromMST[iNodeAdd]].recombination_rate
            for i in linkedWithMST:
                myLen = self.edges[idEdgeShortestFromMST[i]].recombination_rate
                if i in idsNodeInMST:
                    print("problem here: i=" + str(i))
                    bStop = True
                    print("idsNodeInMST: " + str(idsNodeInMST))
                    print("linkedWithMST: " + str(linkedWithMST))
                if minLength > myLen:
                    minLength = myLen
                    iNodeAdd = i

            # add
            edge = self.edges[idEdgeShortestFromMST[iNodeAdd]]
            k = edge.get_end_node(mst_net.get_node(iNodeAdd)).id
            nodeStart, nodeEnd = Edge.sort2(edge.start_node, edge.end_node)  # Returns NODES NOT ID
            #### Find MST net reference of Start and End that is identical to Net node
            nodeStart = mst_net.nodes[nodeStart.id]
            nodeEnd = mst_net.nodes[nodeEnd.id]

            eNew = edge.copy(nodeStart, nodeEnd)
            #
            mst_net.addEdge(eNew)
            nodeStart.add_edge(eNew)
            nodeEnd.add_edge(eNew)
            rankInMST[iNodeAdd] = rankInMST[k] + 1
            if rankInMST[iNodeAdd] < 0:
                print("problem")
            idsNodeInMST.append(iNodeAdd)
            linkedWithMST.remove(iNodeAdd)
            node = self.nodes[iNodeAdd]

            for edge in node.edges:
                k = edge.get_end_node(mst_net.get_node(iNodeAdd)).id
                if rankInMST[k] < 0:
                    if not (k in linkedWithMST):
                        if (k in linkedWithMST) or (k in idsNodeInMST):
                            print("problem: k=" + str(k) + ", rank=" + str(rankInMST[k]))
                            print(str(linkedWithMST))
                            print(idsNodeInMST)
                        linkedWithMST.append(k)
                        idEdgeShortestFromMST[k] = edge.id
                    else:
                        edge1 = self.edges[idEdgeShortestFromMST[k]]
                        if edge.recombination_rate < edge1.recombination_rate:
                            idEdgeShortestFromMST[k] = edge.id

            if bPrintDetails:
                print("in MST " + str(len(idsNodeInMST)) + " of n=" + str(len(self.nodes)))
            if bStop:
                linkedWithMST = []

        if bPrint:
            idsNodeInMST.sort()
            print(
                f"...Finished \n\t#Total nodes in MST: {len(mst_net.nodes)}\n\t#Nodes in MST: {len(idsNodeInMST)}\n\t#Edges in MST: {len(mst_net.edges)}\n\tNodes IDs: {str(idsNodeInMST)}")

        return mst_net

    # def calc_max_MST(self):
    #     max_mst = None
    #     longest_path = 0
    #    # l = []
    #     for node in self.nodes:
    #         mst_net = self.calc_MST_net(from_node=node, bPrint=True)
    #         mst_nodes = mst_net.idNodesOnPathLongest()
    #         if len(mst_nodes) > longest_path:
    #             longest_path = len(mst_nodes)
    #             max_mst = mst_net
    #             ids = mst_nodes
    #     print(f"\nCalculate Max MST:\n\tNodes on longest path: {ids}\n\tLongest MST path: {longest_path}")
    #     return max_mst

    """
        calculate the rank of nodes bya7as to another node that we chose (idNodeStart)
        """

    def calcRanksOfNodes(self, idNodeStart, bPrint=False):
        rank = [-1] * len(self.nodes)
        if bPrint:
            print("calcRanksOfNodes=" + str(len(self.nodes)) + " and nEdges=" + str(len(self.edges)) + "...")
        rank[idNodeStart] = 0
        currentSet = [idNodeStart]
        # set=[idNodeStart]
        set = []
        r = 0
        while len(currentSet) > 0:
            nextSet = []
            for j in currentSet:
                node = self.nodes[j]
                for edge in node.edges:
                    k = edge.get_end_node(node).id
                    if rank[k] < 0:
                        nextSet.append(k)
                        rank[k] = r + 1
                        set.append(k)
            if len(nextSet) > 0:
                r += 1
            currentSet = nextSet
        rankMax = max(rank)
        withRank = []
        # print("rank: "+str(rank))
        # print("rankMax: "+str(rankMax))
        for i in range(rankMax + 1):
            withRank.append([])
        for i in range(len(self.nodes)):
            # rank[i]
            withRank[rank[i]].append(i)
        # print("withRank: "+str(withRank))

        if bPrint:
            print(f"rankMax: {str(rankMax)} \n rank: {rank} \n withRank: {withRank}")
            print("calcRanksOfNodes=" + str(len(self.nodes)) + " and nEdges=" + str(len(self.edges)) + "...Finished\n")

        return rank, rankMax, withRank

    """
    Find which nodes are on the longest path of mst
    """

    def idNodesOnPathLongest(self, bPrintDetails=False):
        print("\nidNodesOnPathLongest for net of " + str(len(self.nodes)) + " nodes...")
        mst_net = self  # self.calc_MST_net()
        rank, rankMax, withRank = mst_net.calcRanksOfNodes(self.nodes[0].id)
        starts = withRank[rankMax]
        myList = []
        argMax = -1
        for start in starts:
            rank, rankMax, withRank = mst_net.calcRanksOfNodes(self.nodes[start].id)
            if argMax < 1:
                argMax = 0
                myList = [rank, rankMax, withRank]
            else:
                if argMax > myList[1]:
                    myList = [rank, rankMax, withRank]
        if bPrintDetails:
            print("LenOfLongestPath=" + str(rankMax + 1) + " nodes")

        idNode = withRank[rankMax][0]
        idNodes = [idNode]
        r = rankMax
        while r > 0:
            idNodeNext = -1
            for edge in mst_net.nodes[idNode].edges:
                k = edge.get_end_node(mst_net.nodes[idNode]).id
                if rank[k] < r:
                    idNodeNext = k
            idNodes.append(idNodeNext)
            r -= 1
            idNode = idNodeNext
        if bPrintDetails:
            print("Nodes of path: " + str(idNodes))
        i = 0
        if bPrintDetails:
            print("i\tidInLG\tnameOfNode")
        for id in idNodes:
            i += 1
            if bPrintDetails:
                print(str(i) + " " + str(id) + " " + self.nodes[id].caption)
        # begin: NODE_11323_length_3805_cov_2.15481_B0
        # end: NODE_7765_length_7967_cov_2.01428_B0
        print(
            "\tLongest path length:" + str(len(idNodes)) + "\n\tNodes on longest path:" + str(idNodes) + "\nFinished\n")
        return idNodes

    """
    print the network to pajek file
    """

    @staticmethod
    def print_pajek_network(plot_net, sFileName='output.net', bPrintDetails=False):
        # *Network
        # *Vertices 3
        # 1 "pe0" ic LightGreen 0.5 0.5 box
        # 2 "pe1" ic LightYellow 0.8473 0.4981 ellipse
        # 3 "pe2" ic LightYellow 0.6112 0.8387 triangle
        # *Arcs
        # 1 2 1 c black
        # 1 3 -1 c red
        # *Edges
        # 2 3 1 c black w 1
        print("\nPrinting network to file " + sFileName + "...\n")

        with open(sFileName, 'w') as file:
            # Print Pajek file header
            file.write("*Network" + '\n')
            file.write("*Vertices " + str(len(plot_net.nodes)) + '\n')

            # Print nodes data
            for node in plot_net.nodes:
                file.write(node.get_node_data() + '\n')

            file.write("*Edges " + str(len(plot_net.edges)) + '\n')
            for i, edge in enumerate(plot_net.edges):
                file.write(edge.get_edge_data())

                if bPrintDetails and len(plot_net.edges) > 10000:
                    if i % 1000 == 1:
                        print(str(i) + " of " + str(len(plot_net.edges)) + " edges are processed")

        print("Network was printed to: " + sFileName + "...Finished")

    """
    divide the whole network to parts that the edges between these parts has recombination rate > cutoff
    """

    def singleLinkageClustering(self, cutoff, bPrint=False, bPrintDetails=False):
        clusters = []
        in_cluster = [-1] * len(self.nodes)
        rank_max = []  # [0] * len(self.nodes)
        n_clusters = 0

        if bPrint:
            print(
                "clustering of net with nNodes=" + str(len(self.nodes)) + " and nEdges=" + str(len(self.edges)) + "...")

        for i in range(len(self.nodes)):
            if in_cluster[i] < 0:
                if bPrintDetails:
                    print("started from " + str(i) + " ...")

                n_clusters += 1
                iCluster = n_clusters - 1
                in_cluster[i] = iCluster
                rank_max.append(0)

                r = 0
                current_set = [i]
                sett = [i]
                while len(current_set) > 0:
                    next_set = []
                    for j in current_set:
                        node = self.nodes[j]
                        for edge in node.edges:
                            k = edge.get_end_node(node).id
                            if in_cluster[k] < 0:
                                if edge.recombination_rate <= cutoff:
                                    next_set.append(k)
                                    in_cluster[k] = iCluster
                                    sett.append(k)
                    if len(next_set) > 0:
                        r += 1
                        if bPrintDetails:
                            print("rank=" + str(r) + ", nAdd=" + str(len(next_set)))
                    current_set = next_set
                rank_max[iCluster] = r
                clusters.append(sett)
                if bPrintDetails:
                    print("started from " + str(i) + " ...Finished: n=" + str(len(sett)))
        if bPrint:
            print("clustering of net with nNodes=" + str(len(self.nodes)) + " and nEdges=" + str(
                len(self.edges)) + "...Finished")
            print("nClusters=" + str(len(clusters)))
            if bPrintDetails:
                print("Sizes:")
                for c in clusters:
                    print(" " + str(len(c)) + ": " + str(c))
        return clusters, in_cluster

    """
    retuns all nodes that these nodes doesn't have a prove with edges 5offot ?
    """

    def nodesIDUnprovenByParallelpaths(self, cutoff=0.15, cutoffParallel=0.25):
        ids = []
        print("nodesIDUnprovenByParallelpaths...")
        for node in self.nodes:
            n_nodes = []
            # For every edge in node, check if recombination_rate <= cutoff, if True, add edge end node to n_nodes
            for edge in node.edges:
                if edge.recombination_rate <= cutoff:
                    k = edge.get_end_node(node).id
                    if not (k in n_nodes):
                        n_nodes.append(k)
            net1 = self.subnet(n_nodes, cutoffParallel)
            clusters, inCluster = net1.singleLinkageClustering(cutoffParallel, False, False)
            if len(clusters) > 1:
                ids.append(node.id)
            if node.id % 200 == 1:
                print(str(node.id) + " of " + str(len(self.nodes)) + " nodes are processed")
        print("nodesIDUnprovenByParallelpaths...Finished")
        print(str(len(ids)) + " nodes to exclude:")
        for id in ids:
            print(str(id) + " " + self.nodes[id].caption)
        return ids  # list of IDs that should be removed from network

    """
    remove nodes from net according to nodes in the list(idsExclude)
    """

    def netWithoutNodesFromList(self, idsExclude, cutoff):  # Build new network without excluded nodes
        idsOk = []
        for i in range(len(self.nodes)):
            if not (i in idsExclude):
                idsOk.append(i)
        return self.subnet(idsOk, cutoff)

    def subnet(self, idsInclude, cutoff):
        """
        sub-network according to cutoff (r < cutoff) -> (default cutoff = 15%)
        :param ids: IDs of nodes to be included in the subnet
        :param cutoff:
        :return:
        """
        net = Network(nodes=[], edges=[], mst=None, skeleton=None, cutoff=cutoff)
        idnew = [-1] * len(self.nodes)
        idsPP = []
        idMy = []
        i = 0
        for node in self.nodes:
            if node.id in idsInclude:
                vpp = node.copy(i, edges=[])
                idnew[node.id] = i
                idsPP.append(i)
                idMy.append(node.id)
                i += 1
                net.addNode(vpp)
                # net.node.append(vpp)
                # net.nNodes += 1

        for i in idsPP:
            j = idMy[i]
            for edge in self.nodes[j].edges:
                # print(str(i)+" "+str(idnew[i])+" "+str(idnew[k])+" "+str(k))
                if edge.recombination_rate <= cutoff:
                    k = edge.get_end_node(self.nodes[j]).id
                    if idnew[k] >= 0:
                        # print(str(i)+" "+str(idnew[j])+" "+str(idnew[k])+" "+str(k))
                        if idnew[j] < idnew[k]:
                            startNode = net.nodes[idnew[j]]  # self.get_node(idnew[j])
                            endNode = net.nodes[idnew[k]]  # self.get_node(idnew[k])
                            epp = edge.copy(startNode, endNode)
                            startNode.add_edge(epp)
                            endNode.add_edge(epp)
                            net.addEdge(epp)
        return net

    def makeLinearContigClusters(self, bExcludeNodesCausingNonLinearClusters=False, cutoff=0.15, cutoffParallel = 0.25):
        # clusters, inCluster
        if bExcludeNodesCausingNonLinearClusters:  # BOOLEAN
            idsExclude = self.nodesIDUnprovenByParallelpaths(cutoff, cutoffParallel)
            linear_net = self.netWithoutNodesFromList(idsExclude, cutoffParallel)
            # Network.print_pajek_network(linear_net, sFileName="linear.net")
        return linear_net, idsExclude  # clusters, inCluster
