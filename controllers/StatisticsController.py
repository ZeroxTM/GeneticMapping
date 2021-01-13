class StatisticsController:
    ui = None

    @staticmethod
    def display_stat(markers, linkage_groups):
        StatisticsController.ui.map_markers.setText(str(len(markers)))
        StatisticsController.ui.map_genotypes.setText(str(StatisticsController.count_n01(markers)))
        StatisticsController.ui.map_linkages.setText(str(len(linkage_groups)))
        StatisticsController.ui.map_allele.setText(str(round(StatisticsController.calc_frequency(markers),3)))

    @staticmethod
    def count_n01(markers):
        total = 0
        for marker in markers:
            total += marker.n0 + marker.n1 + marker.n_missing

        return total

    @staticmethod
    def calc_frequency(markers):
        allele_frequency = 0
        for marker in markers:
            allele_frequency += marker.p1
        return allele_frequency / len(markers)
