"""
Class of genetic markers
"""
from Macros import calculate_p0, calculate_p1, calculate_p_missing, calculate_segregation


class Marker:
    markers = list()

    def __init__(self, id, name, alleles, linkage_id, linkage_group, skeleton_index, coordinate_genet):
        """
        Marker initilization
        :param id: Marker ID int
        :param name: Marker Name string
        :param alleles: {0,1,-1}
        :param n0: int
        :param n1: int
        :param n_missing: int
        :param p0: float
        :param p1: float
        :param twins: int
        :param topology_connection_index: int
        :param linkage_id: int
        :param linkage_group: LinkageGroup
        :param skeleton_index: int
        :param coordinate_genet: float
        """
        self.id = id
        self.name = name
        self.alleles = alleles
        self.n0, self.n1, self.n_missing = self.calculate_n01()

        self.p0 = calculate_p0(self.n0, self.n1)
        self.p1 = calculate_p1(self.n0, self.n1)
        self.p_missing = calculate_p_missing(self.n_missing, (self.n0 + self.n1 + self.n_missing))
        self.segregation = calculate_segregation(self.n0, self.n1, self.p0, self.p1)

        self.twins = 0  # Needs redefinition
        self.linkage_id = linkage_id
        self.linkage_group = linkage_group
        self.topology_connection_index = 0  # Needs redefinition
        self.skeleton_index = skeleton_index
        self.coordinateGenet = coordinate_genet

    def calculate_n01(self):
        if len(self.alleles) != 0:
            return str(self.alleles[0]).count('0'), str(self.alleles[0]).count('1'), str(self.alleles[0]).count('-')
        else:
            return 0, 0, 0

    def calcStatistics(self):
        """
        statistics are calculated here
        :return:
        """
        print("Stats")
