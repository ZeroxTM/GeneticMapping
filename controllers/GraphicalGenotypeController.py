"""
 @Time : 30/11/2020 15:47
 @Author : Alaa Grable
 """
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QTableWidgetItem

from classes.Marker import Marker
from Data import Data


class GraphicalGenotypeController:
    ui = None
    colors = {
        "1": QtGui.QColor(0, 77, 153, 180),
        "0": QtGui.QColor(112, 128, 144),
        "-": QtGui.QColor(134, 136, 138, 180),
        "Empty": QtGui.QColor(211, 211, 211, 180)
    }

    @staticmethod
    def draw_graphical_genotype_map():
        count = 0
        orig_alleles_dict = dict()
        GraphicalGenotypeController.ui.genotypingTable.setShowGrid(False)
        GraphicalGenotypeController.ui.genotypingTable.horizontalHeader().hide()
        # GraphicalGenotypeController.ui.genotypingTable.verticalHeader().hide()
        from controllers.MarkersTabController import MarkersTabController
        gen_length = max(
            [len(marker.alleles[0]) if len(marker.alleles) != 0 else 0 for marker in MarkersTabController.markers])
        for i in range(gen_length):
            GraphicalGenotypeController.ui.genotypingTable.insertColumn(i)
            GraphicalGenotypeController.ui.genotypingTable.setColumnWidth(i, 10)
            # GraphicalGenotypeController.ui.genotypingTable.resizeColumnToContents(i)
        for row, marker in enumerate(MarkersTabController.markers):
            GraphicalGenotypeController.ui.genotypingTable.insertRow(row)
            alleles = marker.alleles[0] if len(marker.alleles) != 0 else 'Empty'
            orig_alleles_dict[marker.id] = alleles
            if alleles == 'Empty':
                for col_index in range(gen_length):
                    item = QTableWidgetItem()
                    item.setBackground(GraphicalGenotypeController.colors[alleles])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    GraphicalGenotypeController.ui.genotypingTable.setItem(row, col_index, item)
                GraphicalGenotypeController.ui.genotypingTable.setRowHidden(row, True)  # Hide empty row
            else:
                for col_index, char in enumerate(alleles):
                    item = QTableWidgetItem(char)
                    item.setBackground(GraphicalGenotypeController.colors[char])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    GraphicalGenotypeController.ui.genotypingTable.setItem(row, col_index, item)
        Data.orig_alleles_dict = orig_alleles_dict
        GraphicalGenotypeController.filter_fix(orig_alleles_dict)


    @staticmethod
    def filter_fix(alleles_dict):
        # Filter out markers without alleles info
        alleles_dict = alleles_dict.copy()
        for k in list(alleles_dict):
            if alleles_dict[k] == 'Empty':
                del alleles_dict[k]
        Data.mod_alleles_dict = alleles_dict
        # Time for the real work here
        for i in alleles_dict:
            None
