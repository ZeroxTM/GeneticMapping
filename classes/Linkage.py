"""
 @Time : 20/11/2020 15:58
 @Author : Alaa Grable
 """
"""
Class of genetic linkage between two markers
"""
from Macros import calculate_recombination_rate


class Linkage:
    ui = None

    def __init__(self, linkage_id, marker_1_id, marker_1_name, marker_2_id, marker_2_name):
        self.linkage_id = linkage_id
        self.marker_1_id = marker_1_id
        self.marker_2_id = marker_2_id
        self.marker_1_name = marker_1_name
        self.marker_2_name = marker_2_name
        self.n00 = 0  # Needs redefinition
        self.n01 = 0  # Needs redefinition
        self.n10 = 0  # Needs redefinition
        self.n11 = 0  # Needs redefinition
        self.recombination_rate = calculate_recombination_rate(self.n00, self.n01, self.n10, self.n11)
        self.expected_distance_haldane = 0  # Needs redefinition
        self.expected_distance_kossambi = 0  # Needs redefinition
        self.observed_distance = 0   # Needs redefinition
        self.distance_on_map = 0   # Needs redefinition
        self.p_value = 0   # Needs redefinition
        self.p_min = 0  # Needs redefinition
        self.p_max = 0  # Needs redefinition
        self.min_distance_haldane = 0  # Needs redefinition
        self.max_distance_haldane = 0  # Needs redefinition
        self.topology_connection_index = 0  # Needs redefinition

