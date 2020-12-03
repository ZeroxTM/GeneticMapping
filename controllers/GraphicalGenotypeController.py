"""
 @Time : 30/11/2020 15:47
 @Author : Alaa Grable
 """
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QTableWidgetItem

class GraphicalGenotypeController:
    ui = None
    colors = {
        "1": QtGui.QColor(102, 0, 0, 180),  # Dark Red
        "0": QtGui.QColor(0, 77, 153, 180),  # Dark Blue
        "-": QtGui.QColor(134, 136, 138, 180)  # Dark Grey
    }

    @staticmethod
    def draw_graphical_genotype_map():
        GraphicalGenotypeController.ui.tableWidget.setShowGrid(False)
        GraphicalGenotypeController.ui.tableWidget.horizontalHeader().hide()
        GraphicalGenotypeController.ui.tableWidget.verticalHeader().hide()
        row = 0
        from controllers.MarkersTabController import MarkersTabController
        for marker in MarkersTabController.markers:
            if len(marker.alleles) != 0:
                GraphicalGenotypeController.ui.tableWidget.setColumnCount(len(marker.alleles[0]))
                GraphicalGenotypeController.ui.tableWidget.insertRow(row)
                for col_index, char in enumerate(marker.alleles[0]):
                    item = QTableWidgetItem(char)
                    item.setBackground(GraphicalGenotypeController.colors[char])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    GraphicalGenotypeController.ui.tableWidget.setItem(row, col_index, item)
                row += 1
