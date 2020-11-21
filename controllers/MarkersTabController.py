from PySide2 import QtCore
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtWidgets import QMessageBox

from classes.Marker import Marker


class MarkersTabController:
    ui = None
    markers = list()

    @staticmethod
    def fetch_markers(data):  # Fetch data into table view markersTable
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
            # ~~~~~~~~~~~~~~ Read the markers from the file (Panda DataFrame) ~~~~~~~~~~~~~~#
            for index, row in data.iterrows():
                MarkersTabController.markers.append(Marker(index, row['marker'], row['iLG']
                                                           , row['chr'], 0, row['coorGenet']))
            # ~~~~~~~~~~~~~~ Display the markers in the table in gui ~~~~~~~~~~~~~~#
            for row, marker in enumerate(MarkersTabController.markers):
                MarkersTabController.ui.markersTable.insertRow(row)
                for column, variable in enumerate(vars(marker).items()):
                    item = QTableWidgetItem(str(variable[1]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    MarkersTabController.ui.markersTable.setItem(row, column, item)

