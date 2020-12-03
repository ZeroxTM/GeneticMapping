"""
 @Time : 30/11/2020 15:47
 @Author : Alaa Grable
 """
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QTableWidgetItem


class GraphicalGenotypeController:
    ui = None
    colors = {
        "1": QtGui.QColor(0, 77, 153, 180),
        "0": QtGui.QColor(112, 128, 144, 180),
        "-": QtGui.QColor(134, 136, 138, 180),
        "empty": QtGui.QColor(211, 211, 211, 180)
    }

    @staticmethod
    def draw_graphical_genotype_map():
        GraphicalGenotypeController.ui.genotypingTable.setShowGrid(False)
        GraphicalGenotypeController.ui.genotypingTable.horizontalHeader().hide()
        GraphicalGenotypeController.ui.genotypingTable.verticalHeader().hide()
        from controllers.MarkersTabController import MarkersTabController
        gen_length = max(
            [len(marker.alleles[0]) if len(marker.alleles) != 0 else 0 for marker in MarkersTabController.markers])
        for i in range(gen_length):
            GraphicalGenotypeController.ui.genotypingTable.insertColumn(i)
            GraphicalGenotypeController.ui.genotypingTable.resizeColumnToContents(i)
        for row, marker in enumerate(MarkersTabController.markers):
            GraphicalGenotypeController.ui.genotypingTable.insertRow(row)
            alleles = marker.alleles[0] if len(marker.alleles) != 0 else 'empty'
            if alleles == 'empty':
                for col_index in range(gen_length):
                    item = QTableWidgetItem()
                    item.setBackground(GraphicalGenotypeController.colors[alleles])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    GraphicalGenotypeController.ui.genotypingTable.setItem(row, col_index, item)
            else:
                for col_index, char in enumerate(alleles):
                    item = QTableWidgetItem(char)
                    item.setBackground(GraphicalGenotypeController.colors[char])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    GraphicalGenotypeController.ui.genotypingTable.setItem(row, col_index, item)
