"""
Class of Linkage Groups
"""


class LinkageGroup:
    def __init__(self, id=None, name=None, marker=[], skeletonMarker=[], markerOrd=[], network=None):
        """
        Linkage group
        :param id: Linkage Group ID
        :param name: Linkage group name
        :param marker: list of markers that belong to this group
        :param skeletonMarker: list of skeleton markers
        :param markerOrd: list of markers
        :param network: network that linkage group belongs to
        """
        self.id = id
        self.name = name
        self.marker = marker
        self.skeletonMarker = skeletonMarker
        self.markerOrd = markerOrd
        self.network = network

    def calcRec(self):
        print("")

    def buildNetwork(self):
        print()

    def selectSkeleton(self):
        print()

    def calcCoordinates(self):
        print()

    def filtration(self):
        print()

    def grouping(self):
        print()