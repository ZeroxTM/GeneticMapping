from collections import defaultdict

from PySide2 import QtCore
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtWidgets import QMessageBox

from classes.LinkageGroup import LinkageGroup
from classes.Marker import Marker
from controllers.GraphicalGenotypeController import GraphicalGenotypeController


class MarkersTabController:
    ui = None
    markers = list()

    @staticmethod
    def fetch_markers(data, ddf):  # Fetch data into table view markersTable
        if MarkersTabController.ui is None:
            QMessageBox.information(MarkersTabController.ui, "Warning", "Something went wrong with the .txt file.")
        else:
            '''
            # ~~~~~~~~~~~~~~ Read the markers from the file (Normal .txt file) ~~~~~~~~~~~~~~#
            with open('geneticMap.txt') as fp:
                fp.readline()  # ignore the first line in the file
                for line in fp:
                    temp_line = line.split()
                    MarkersTabController.markers.append(Marker(temp_line[0], temp_line[1], temp_line[3]
                                                               , temp_line[4], 0, temp_line[5]))
            '''
            linkageGroupsDict = defaultdict(list)
            markers = MarkersTabController.markers
            # ~~~~~~~~~~~~~~ Read the markers from the file (Panda DataFrame) ~~~~~~~~~~~~~~#
            for index, row in data.iterrows():
                marker = Marker(index, row['marker'], (list(ddf.loc[ddf['marker_name'] == row['marker'], 'properties'])),
                                row['iLG'], row['chr'], 0, row['coorGenet'])
                markers.append(marker)
                linkageGroupsDict[marker.linkage_group].append(marker)

            LinkageGroup.create_linkages(linkageGroupsDict)  # Create all linkage groups

            # ~~~~~~~~~~~~~~ Display the markers in the table in gui ~~~~~~~~~~~~~~#
            for row, marker in enumerate(markers):
                MarkersTabController.ui.markersTable.insertRow(row)
                for column, variable in enumerate(vars(marker).items()):
                    item = QTableWidgetItem(str(variable[1]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    MarkersTabController.ui.markersTable.setItem(row, column, item)

            # Display statistics
            MarkersTabController.ui.map_markers.setText(str(len(MarkersTabController.markers)))
            GraphicalGenotypeController.draw_graphical_genotype_map()
