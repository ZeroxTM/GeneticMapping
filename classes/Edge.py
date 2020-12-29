class Edge:
    def __init__(self, node1, node2, recombinationRate=None):
        """
        Edge connected to 2 nodes
        :param node1: first end [Node]
        :param node2: second end [Node]
        :param recombinationRate: Recombination Rate between nodes (cM) [float]
        """
        self.node1 = node1  # idStart
        self.node2 = node2  # idEnd
        self.recombinationRate = recombinationRate
        self.val = 1
        self.sc = "black"
        self.w = 1
        self.sp = "Solid"
        self.sl = ""

    def check(self):
        print()

    def print(self):
        print()

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
