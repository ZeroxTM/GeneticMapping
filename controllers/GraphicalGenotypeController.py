"""
 @Time : 30/11/2020 15:47
 @Author : Alaa Grable
 """
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QTableWidgetItem

class GraphicalGenotypeController:
    ui = None
    used_indexes = dict()

    colors = {
        "1": QtGui.QColor(102, 0, 0, 180),  # Dark Red
        "0": QtGui.QColor(0, 77, 153, 180),  # Dark Blue
        "-": QtGui.QColor(134, 136, 138, 180)  # Dark Grey
    }

    @staticmethod
    def draw_graphical_genotype_map():
        GraphicalGenotypeController.ui.genotypingTable.setShowGrid(False)
        GraphicalGenotypeController.ui.genotypingTable.horizontalHeader().hide()
        GraphicalGenotypeController.ui.genotypingTable.verticalHeader().hide()
        row = 0
        from controllers.MarkersTabController import MarkersTabController
        for index, marker in enumerate(MarkersTabController.markers):
            GraphicalGenotypeController.ui.genotypingTable.insertRow(index)
            if len(marker.alleles) != 0:
                GraphicalGenotypeController.used_indexes[index] = marker
                GraphicalGenotypeController.ui.genotypingTable.setColumnCount(len(marker.alleles[0]))
                for col_index, char in enumerate(marker.alleles[0]):
                    item = QTableWidgetItem(char)
                    item.setBackground(GraphicalGenotypeController.colors[char])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    GraphicalGenotypeController.ui.genotypingTable.setItem(row, col_index, item)
                row += 1
