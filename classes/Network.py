"""
Genetic map network structure
"""
import copy
import itertools

from Macros import calculate_recombination_rate
from classes.Edge import Edge
from classes.Linkage import get_shared_alleles
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

    def calcRanksOfNodes(self, idNodeStart, bPrint):
        pass

    def checkConnection(self):
        print()

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)

    def initialize_network(self, linkage_groups):
        """
        :param indexes_of_linkages: list of linkage (linkageGroup)
        :return:
        """
        id = -1
        node_id = -1
        print("\nAdding Nodes to the network ..\n")
        for linkage_group in linkage_groups:
            print("\nAdding nodes to network from linkage: " + str(linkage_group.id) + "\n")
            for marker in linkage_group.markers:
                node_id += 1
                self.addNode(Node(id=node_id, index=marker.id, marker=marker, edges=[]))
        print("\nDone Adding Nodes to the network!")
        print("\nAdding edges to the network ..\n")
        for linkage_group in linkage_groups:
            print("\nAdding Edges to network from linkage group: " + str(linkage_group.id))
            combinations = itertools.combinations(linkage_group.markers, 2)
            for comb in combinations:
                ns = get_shared_alleles(comb[0].alleles, comb[1].alleles)
                if type(ns) != str:
                    recombination_rate = calculate_recombination_rate(ns[0], ns[1], ns[2], ns[3])
                    if recombination_rate <= 0.15:
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

    """
    write the network to pajek file (upper file before edges)
    """

    # def printToFilePajek__shapka(self, file, nodes_length):
    #     file.write("*Network" + '\n')
    #   file.write("*Vertices " + str(nodes_length) + '\n')

    # def printToFilePajek__shapkaEdges(self, file, nEdges=-1):
    #   s = ""
    #   if nEdges >= 0:
    #       s = ' ' + str(nEdges)
    #   file.write("*Edges" + s + '\n')

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
        rankInMST = [-1] * len(self.nodes)
        idEdgeShortestFromMST = [-1] * len(self.nodes)
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
            print("Minimal spanning tree (MST) for net with nNodes=" + str(len(self.nodes)) + " and nEdges=" + str(
                len(self.edges)) + f"...Finished \n\t#Nodes in MST: {len(mst_net.nodes)}\n\t#Edges in MST: {len(mst_net.edges)}")
            if bPrintDetails:
                idsNodeInMST.sort()
                print(str(idsNodeInMST))
                print(str(rankInMST))
        return mst_net

    """
    print the network to pajek file
    """

    def print_pajek_network(self, sFileName, bPrint=False, bPrintDetails=False):
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
        if bPrint:
            print("\nprint net to file " + sFileName + "...\n")

        with open(sFileName, 'w') as file:
            # Print Pajek file header
            file.write("*Network" + '\n')
            file.write("*Vertices " + str(len(self.nodes)) + '\n')

            # Print nodes data
            for node in self.nodes:
                file.write(node.get_node_data() + '\n')

            # Printing edges to pajek file
            # i = 0
            # for edge in self.edges:
            #   if (dMax < 0 or edge.recombination_rate <= dMax) and (edge.start_node < edge.end_node):
            #      i += 1

            file.write("*Edges " + str(len(self.edges)) + '\n')
            for i, edge in enumerate(self.edges):
                # if (dMax < 0 or edge.recombination_rate <= dMax) and (edge.start_node < edge.end_node):
                file.write(edge.get_edge_data())
                # edge.printToFilePajek(file, edge.start_node + 1, edge.end_node + 1)

                if bPrintDetails and len(self.edges) > 10000:
                    if i % 1000 == 1:
                        print(str(i) + " of " + str(len(self.edges)) + " edges are processed")

        if bPrint:
            print("print net to file " + sFileName + "...Finished")

    """
    write to pajek file not all networks, but a specific (selected) nodes
    """

    # def printToFilePajek__selectedNodesOnly(self, sFileName, dMax, listOfIndexesToSelect, bPrint=False,
    #                                         bPrintDetails=False):
    #     if bPrint:
    #         print("print net to file " + sFileName + "...")
    #     # file = open(sFileName, 'w')
    #     with open(sFileName, 'w') as file:
    #
    #         g = [-1] * len(self.nodes)
    #
    #         for a in listOfIndexesToSelect:
    #             if 0 <= a < len(self.nodes):
    #                 g[a] = 0
    #         n_Corrected = 0
    #         for i in range(len(self.nodes)):
    #             if g[i] >= 0:
    #                 g[i] = n_Corrected
    #                 n_Corrected += 1
    #
    #         file.write("*Network" + '\n')
    #         file.write("*Vertices " + str(n_Corrected) + '\n')
    #         for i in range(len(self.nodes)):
    #             if g[i] >= 0:
    #                 self.nodes[i].printToFilePajek(g[i] + 1, file)
    #
    #         '''
    #         self.printToFilePajek__shapkaEdges(file)
    #         i=0
    #         for e in self.edge:
    #             if (dMax<0 or e.val<=dMax)and(e.idStart<e.idEnd):
    #                 if g[e.idStart]>=0 and g[e.idEnd]>=0:
    #                     e.printToFilePajek(file,g[e.idStart]+1,g[e.idEnd]+1)
    #             i+=1
    #
    #             if bPrintDetails:
    #                 if i%100==1:
    #                     print(str(i)+" of "+str(self.nEdges)+" edges are processed")
    #         '''
    #         i = 0
    #         for edge in self.edges:
    #             if (dMax < 0 or edge.recombination_rate <= dMax) and (edge.start_node < edge.end_node):
    #                 if g[edge.start_node] >= 0 and g[edge.end_node] >= 0:
    #                     # e.printToFilePajek(file,g[e.idStart]+1,g[e.idEnd]+1)
    #                     i += 1
    #
    #             if bPrintDetails:
    #                 if i % 1000 == 1:
    #                     print(str(i) + " of " + str(len(self.edges)) + " edges are processed")
    #
    #         file.write("*Edges " + str(i) + '\n')
    #         i = 0
    #         for edge in self.edges:
    #             if (dMax < 0 or edge.recombination_rate <= dMax) and (edge.start_node < edge.end_node):
    #                 if g[edge.start_node] >= 0 and g[edge.end_node] >= 0:
    #                     edge.printToFilePajek(file, g[edge.start_node] + 1, g[edge.end_node] + 1)
    #             i += 1
    #             if bPrintDetails:
    #                 if i % 1000 == 1:
    #                     print(str(i) + " of " + str(len(self.edges)) + " edges are processed")
    #
    #     # file.close()
    #
    #     if bPrint:
    #         print("print net to file " + sFileName + "...Finished")

    """
    divide the whole network to parts that the edges between these parts has recombination rate > cutoff
    """

    ##NEED MORE EXPLAINATION
    def singleLinkageClustering(self, cutoff, bPrint=False, bPrintDetails=False):
        clusters = []
        in_cluster = [-1] * len(self.nodes)
        rank_max = [0] * len(self.nodes)
        n_clusters = 0

        if bPrint:
            print(
                "clustering of net with nNodes=" + str(len(self.nodes)) + " and nEdges=" + str(len(self.edges)) + "...")

        for i in range(len(self.nodes)):
            if in_cluster[i] < 0:
                if bPrintDetails:
                    print("started from " + str(i) + " ...")

                iCluster = n_clusters
                n_clusters += 1
                in_cluster[i] = iCluster

                r = 0
                current_set = [i]
                sett = [i]
                while len(current_set) > 0:
                    next_set = []
                    for j in current_set:
                        node = self.nodes[j]
                        for edge in node.edges:
                            k = edge.idNodeEnd(j)
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
    calculate the rank of nodes bya7as to another node that we chose (idNodeStart)
    """

    def calcRanksOfNodes(self, idNodeStart, bPrint):
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
                    k = edge.idNodeEnd(j)
                    if rank[k] < 0:
                        nextSet.append(k)
                        rank[k] = r + 1
                        set.append(k)
            if len(nextSet) > 0:
                r += 1
                bPrintDetails = False
                if bPrintDetails:
                    print("rank=" + str(r) + ", nAdd=" + str(len(nextSet)))
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
            print("rankMax: " + str(rankMax))
            print("calcRanksOfNodes=" + str(len(self.nodes)) + " and nEdges=" + str(len(self.edges)) + "...Finished")
        return rank, rankMax, withRank

    """
    Find which nodes are on the longest path of mst
    """

    def idNodesOnPathLongest(self, bPrint=False, bPrintDetails=False):
        if bPrint:
            print("idNodesOnPathLongest for net of " + str(len(self.nodes)) + " nodes...")
        netMST = self.MST(bPrint=False, bPrintDetails=False)
        rank, rankMax, withRank = netMST.calcRanksOfNodes(0, False)
        starts = withRank[rankMax]
        myList = []
        argMax = -1
        for start in starts:
            rank, rankMax, withRank = netMST.calcRanksOfNodes(start, False)
            if argMax < 1:
                argMax = 0
                myList = [rank, rankMax, withRank]
            else:
                if argMax > myList[1]:
                    myList = [rank, rankMax, withRank]
        if bPrintDetails:
            print("LenOfLongestPath=" + str(rankMax + 1)) + " nodes"

        idNode = withRank[rankMax][0]
        idNodes = [idNode]
        r = rankMax
        while r > 0:
            idNodeNext = -1
            for edge in netMST.nodes[idNode].edges:
                k = edge.idNodeEnd(idNode)
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
        if bPrint:
            print("idNodesOnPathLongest for net of " + str(len(self.nodes)) + " nodes...Finished")
        return idNodes

    """
    after clusterization, we can write that cluster(linkage group) to pajek file
    """

    def printToFilePajek_allCluster(self, dMax, sName, clusters, inCluster, sPath):
        sFileName = sPath + sName + "_in_" + str(len(clusters)) + "_Clusters.txt"
        # file = open(sFileName, 'w')
        with open(sFileName, 'w') as file:
            file.write("i\tmarker\tLG\tn\n")
            for i in range(len(self.nodes)):
                file.write(str(i) + '\t' + self.nodes[i].caption + '\t' + str(inCluster[i]) + '\t' + str(
                    len(clusters[inCluster[i]])) + '\n')
        # file.close()
        n = len(clusters)
        for i in range(n):
            sFileNamePajekPP = sPath + sName + "_cl" + str(i + 1) + "_" + str(len(clusters[i])) + ".net"
            self.printToFilePajek__selectedNodesOnly(sFileNamePajekPP, dMax, clusters[i], True, False)
        print("all clusters are printed")

    """
    retuns all nodes that these nodes doesn't have a prove with edges 5offot ?
    """

    def nodesIDUnprovenByParallelpaths(self, cutoff, cutoffParallel):
        ids = []
        print("nodesIDUnprovenByParallelpaths...")
        for node in self.nodes:
            n_nodes = []
            for edge in node.edges:
                if edge.recombination_rate <= cutoff:
                    k = edge.idNodeEnd(node.id)
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
        return ids

    """
    remove nodes from net according to nodes in the list(idsExclude)
    """

    def netWithoutNodesFromList(self, idsExclude, cutoff):
        idsOk = []
        for i in range(len(self.nodes)):
            if not (i in idsExclude):
                idsOk.append(i)
        return self.subnet(idsOk, cutoff)

    """
    sub-network according to cutoff (r < cutoff) -> (default cutoff = 15%)
    """

    def subnet(self, ids, cutoff):
        net = Network()
        idnew = [-1] * len(self.nodes)
        idsPP = []
        idMy = []
        i = 0
        for node in self.nodes:
            if node.id in ids:
                vpp = node.copy(i)
                idnew[node.id] = i
                idsPP.append(i)
                idMy.append(node.id)
                i += 1
                net.addNode(vpp)
                # net.node.append(vpp)
                # net.nNodes += 1
            # if i==1:
            #	print("nEdges0="+str(len(vpp.edges)))
        if False:
            print
            len(idMy)
            print
            len(ids)
            for i in ids:
                if not (i in idMy):
                    print(str(i))
            print
            ids
            print
            str(self.node[0].id)
            print
            str(self.node[1].id)
            print
            str(self.node[2].id)

        for i in idsPP:
            j = idMy[i]
            for edge in self.nodes[j].edges:
                # print(str(i)+" "+str(idnew[i])+" "+str(idnew[k])+" "+str(k))
                if edge.recombination_rate <= cutoff:
                    k = edge.idNodeEnd(j)
                    if idnew[k] >= 0:
                        # print(str(i)+" "+str(idnew[j])+" "+str(idnew[k])+" "+str(k))
                        if idnew[j] < idnew[k]:
                            epp = edge.copy(idnew[j], idnew[k])
                            net.addEdge(epp)
        return net
