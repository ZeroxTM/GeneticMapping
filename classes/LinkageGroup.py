"""
Class of Linkage Groups
"""


class LinkageGroup:
    LinkageGroups = dict()

    def __init__(self, id=None, name=None, markers=[], skeletonMarker=[], markerOrd=[], network=None):
        """
        Linkage group
        :param id: Linkage Group ID
        :param name: Linkage group name
        :param markers: list of markers that belong to this group
        :param skeletonMarker: list of skeleton markers
        :param markerOrd: list of markers
        :param network: network that linkage group belongs to
        """
        self.id = id
        self.name = name
        self.markers = markers
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

    @staticmethod
    def create_linkages(linkageGroupsDict=dict()):
        for key in linkageGroupsDict:
            LinkageGroup.LinkageGroups[key] = LinkageGroup(linkageGroupsDict[key][0].id, key, linkageGroupsDict[key],[],[], None)
