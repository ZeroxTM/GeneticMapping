from collections import defaultdict

from PySide2 import QtCore
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtWidgets import QMessageBox

from classes.LinkageGroup import LinkageGroup
from classes.Marker import Marker
from controllers.GraphicalGenotypeController import GraphicalGenotypeController
from controllers.StatisticsController import StatisticsController


class MarkersTabController:
    ui = None
    markers = list()

    @staticmethod
    def fetch_markers(data, ddf):  # Fetch data into table view markersTable
        if MarkersTabController.ui is None:
            QMessageBox.information(MarkersTabController.ui, "Warning", "Something went wrong with the .txt file.")
        else:
            linkageGroupsDict = defaultdict(list)
            markers = list()
            # ~~~~~~~~~~~~~~ Read the markers from the file (Panda DataFrame) ~~~~~~~~~~~~~~#
            for index, row in data.iterrows():
                marker = Marker(row['im'], row['marker'],
                                (list(ddf.loc[ddf['marker_name'] == row['marker'], 'properties'])),
                                row['iLG'], row['chr'], 0, row['coorGenet'])
                markers.append(marker)
                linkageGroupsDict[marker.linkage_group].append(marker)

            LinkageGroup.create_linkages(linkageGroupsDict)  # Create all linkage groups
            Marker.markers = markers
            MarkersTabController.markers = markers
            MarkersTabController.ui.markersTable.verticalHeader().hide()
            # ~~~~~~~~~~~~~~ Display the markers in the table in gui ~~~~~~~~~~~~~~#
            for row, marker in enumerate(markers):
                MarkersTabController.ui.markersTable.insertRow(row)
                for column, variable in enumerate(vars(marker).items()):
                    item = QTableWidgetItem(str(variable[1])) if str(
                        variable[0]) != 'alleles' else QTableWidgetItem('N/A') if len(
                        variable[1]) == 0 else QTableWidgetItem(str(variable[1])[2:-2])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    MarkersTabController.ui.markersTable.setItem(row, column, item)

            # Display statistics
            StatisticsController.display_stat(markers, LinkageGroup.LinkageGroups)
            GraphicalGenotypeController.draw_graphical_genotype_map()
