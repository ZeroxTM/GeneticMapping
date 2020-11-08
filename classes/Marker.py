"""
Class of genetic markers
"""

class Marker:
    def __init__(self, id, name, genotype, linkageGroup, skeletonIndex, coordinateGenet):
        """
        Marker initilization
        :param id: Marker ID int
        :param name: Marker Name string
        :param genotype: {0,1,-1}
        :param linkageGroup: LinkageGroup
        :param skeletonIndex: int
        :param coordinateGenet: float
        """
        self.id = id
        self.name = name
        self.genotype = genotype
        self.linkageGroup = linkageGroup
        self.skeletonIndex = skeletonIndex
        self.coordinateGenet = coordinateGenet

    def calcStatistics(self):
        """
        statistics are calculated here
        :return:
        """
        print("Stats")
