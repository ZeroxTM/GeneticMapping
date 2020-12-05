"""
 @Time : 20/11/2020 15:58
 @Author : Alaa Grable
 """
"""
Class of genetic linkage between two markers
"""
from Macros import calculate_recombination_rate, calculate_haldane_distance, calculate_kossambi_distance


def get_shared_alleles(marker1_alleles, marker2_alleles):
    n00, n01, n10, n11 = 0, 0, 0, 0
    if len(marker1_alleles) != 0:
        marker1_alleles = marker1_alleles[0]
    else:
        return 'N/A'
    if len(marker2_alleles) != 0:
        marker2_alleles = marker2_alleles[0]
    else:
        return 'N/A'

    for i in range(0, len(marker1_alleles)):
        if marker1_alleles[i] == '0' and marker2_alleles[i] == '0':
            n00 += 1
        elif marker1_alleles[i] == '1' and marker2_alleles[i] == '1':
            n11 += 1
        elif marker1_alleles[i] == '0' and marker2_alleles[i] == '1':
            n01 += 1
        elif marker1_alleles[i] == '1' and marker2_alleles[i] == '0':
            n10 += 1
    return [n00, n01, n10, n11]


class Linkage:
    ui = None

    def __init__(self, linkage_id, marker1, marker2):
        self.linkage_id = linkage_id
        self.marker_1_id = marker1.id
        self.marker_2_id = marker2.id
        self.marker_1_name = marker1.name
        self.marker_2_name = marker2.name
        self.ns = get_shared_alleles(marker1.alleles, marker2.alleles)

        if type(self.ns) != str:
            self.recombination_rate = calculate_recombination_rate(self.ns[0], self.ns[1], self.ns[2], self.ns[3])
            self.expected_distance_haldane = calculate_haldane_distance(self.recombination_rate)
            self.expected_distance_kossambi = calculate_kossambi_distance(self.recombination_rate)
        else:
            self.recombination_rate = 'N/A'
            self.expected_distance_haldane = 'N/A'
            self.expected_distance_kossambi = 'N/A'
        self.observed_distance = round(abs(float(marker1.coordinateGenet) - float(marker2.coordinateGenet)), 2)
        self.distance_on_map = 0  # Needs redefinition
        self.p_value = 0  # Needs redefinition
        self.p_min = 0  # Needs redefinition
        self.p_max = 0  # Needs redefinition
        self.min_distance_haldane = 0  # Needs redefinition
        self.max_distance_haldane = 0  # Needs redefinition
        self.topology_connection_index = 0  # Needs redefinition

    def __eq__(self, other):
        return self.linkage_id == other.linkage_id and self.marker_1_id == other.marker_1_id \
               and self.marker_2_id == other.marker_2_id
