class Map:
    def __init__(self, network=None, linkage_groups=[], length=0, numOfMarkers=0):
        """

        :param network: network
        :param linkageGroup: list of linkageGroups [LinkageGroup[]]
        :param length: [float]
        :param numOfMarkers: [int]
        """
        self.network = network
        self.linkage_groups = linkage_groups
        self.numOfMarkers = numOfMarkers
