from classes.Node import Node


class Edge:
    def __init__(self, id=-1, start_node=-1, end_node=-1, recombination_rate=1.0, width=1, shape="Solid",
                 description=""):
        """
        Edge connected to 2 nodes
        :param node1: first end [Node]
        :param node2: second end [Node]
        :param recombinationRate: Recombination Rate between nodes (cM) [float]
        """
        self.id = id  # should be static and incremented with each new edge , arbitrary number [IDs are sequenced]
        self.start_node = start_node  # idStart #NODE
        self.end_node = end_node  # idEnd #NODE
        self.recombination_rate = recombination_rate  # self.val
        # self.color = color  # self.cs
        self.color = self.colorGet(self.recombination_rate)
        self.width = width
        self.shape = shape
        self.description = description

    def copy(self, start_node, end_node):
        return Edge(self.id, start_node, end_node, self.recombination_rate, self.width, self.shape, self.description)

    def colorGet(self, r):
        if r <= 0.01:
            return "black"
        if r <= 0.03:
            return "blue"
        if r <= 0.05:
            return "red"
        if r <= 0.1:
            return "LightGreen"
        if r <= 0.15:
            return "yellow"
        return "white"  # "LightGray"

    def get_edge_data(self):
        """
        write a line in pajek file about this edge
        :param file: the file to write the edge to (pajek file)
        :param start_node: start node of the edge
        :param end_node: end node of the edge
        :return:
        """
        sc = " c " + self.color
        # Get the color of the edge according to the recombination rate between
        # these two nodes
        sc = " c " + self.colorGet(self.recombination_rate)
        sv = " " + '{:1.2f}'.format(self.recombination_rate)
        sw = ""
        # Validate the width of the edge
        if self.width > 0:
            sw = " w " + str(self.width)
        s = str(self.start_node) + ' ' + str(self.end_node)
        bSimple = False
        if bSimple:
            # 2 3 1 c black
            s = s + sv + sc + sw + '\n'
        else:
            # Create the pattern for pajek
            # for LTC
            # 19 182 0.15 w 1 c yellow p Solid l ""
            sv = " 1"
            sp = " p " + self.shape  # "Solid"
            sl = " l \"" + '{:1.2f}'.format(self.recombination_rate) + "\""
            s = s + sv + sw + sc + sp + sl + '\n'
        return s

    def update_edge(self, start_node=-1, end_node=-1, recombination_rate=1.0, color="black", width=1, shape="Solid",
                    description=""):

        self.start_node = start_node  # idStart
        self.end_node = end_node  # idEnd
        self.recombination_rate = recombination_rate  # self.val
        self.color = color  # self.cs
        self.width = width
        self.shape = shape
        self.description = description

    def getFromS(self, line):
        """
        read a line from pajek file about this edge
        :param s:
        :return:
        """
        # already without \n
        # 2 3 1 c black w 1
        # 19 182 0.15 w 1 c yellow p Solid l ""
        split_line = line.split(' ')

        color = "black"
        width = 1
        shape = "Solid"
        description = ""
        for i, char in enumerate(split_line):
            if char == "c":
                color = split_line[i + 1]
            if char == "w":
                width = int(split_line[i + 1])
            if char == "p":
                shape = split_line[i + 1]
            if char == "l":
                k = len(split_line[i + 1]) - 1
                if k > 0:
                    description = split_line[i + 1][1:k]
        value = float(split_line[2])
        if value == 1 and len(description) > 0:
            value = float(description)
        self.update_edge(start_node=int(split_line[0]) - 1, end_node=int(split_line[1]) - 1, recombination_rate=value,
                         color=color, width=width, shape="Solid", description=description)

    def get_end_node(self, start_node=Node()):
        """
        if gotten where this edge starts, returns where it ends
        :param
        :return:
        """
        if self.start_node == start_node:
            return self.end_node
        elif self.end_node == start_node:
            return self.start_node
        else:
            return 0

    # undirected edge
    def __eq__(self, other):
        return self.id == other.id or (self.start_node == other.start_node and self.end_node == other.end_node) or \
               (self.start_node == other.end_node and self.end_node == other.start_node)

    @staticmethod
    def sort2(node1, node2):
        return (node1, node2) if node1.id <= node2.id else (node2, node1)

    def check(self):
        print()

    def print(self):
        print()
