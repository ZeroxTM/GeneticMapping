"""
 @Time : 30/11/2020 15:47
 @Author : Alaa Grable
 """
from itertools import tee
from operator import xor

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
        GraphicalGenotypeController.ui.genotypingTable.verticalHeader().hide()
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
            orig_alleles_dict[row] = [marker.id, alleles]
            if alleles == 'Empty':
                pass
                # for col_index in range(gen_length):
                #     item = QTableWidgetItem()
                #     item.setBackground(GraphicalGenotypeController.colors[alleles])
                #     item.setFlags(QtCore.Qt.ItemIsEnabled)
                #     GraphicalGenotypeController.ui.genotypingTable.setItem(row, col_index, item)
                GraphicalGenotypeController.ui.genotypingTable.setRowHidden(row, True)  # Hide empty row
            else:
                for col_index, char in enumerate(alleles):
                    item = QTableWidgetItem(char)
                    item.setBackground(GraphicalGenotypeController.colors[char])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    GraphicalGenotypeController.ui.genotypingTable.setItem(row, col_index, item)
        Data.orig_alleles_dict = orig_alleles_dict
        GraphicalGenotypeController.rename_alleles(orig_alleles_dict)

    @staticmethod
    def rename_alleles(alleles_dict):
        # Filter out markers without alleles info
        alleles_dict = alleles_dict.copy()
        for k in list(alleles_dict):
            if alleles_dict[k][1] == 'Empty':
                del alleles_dict[k]
        Data.mod_alleles_dict = alleles_dict
        # Time for the real work here
        tuples_list = list()
        for x, y in GraphicalGenotypeController.pairwise(list(alleles_dict)):
            tuples_list.append(tuple((int(x), int(y))))
        for tup in tuples_list:
            jumps = 0
            for i in range(0, min(len(alleles_dict[tup[0]][1]), len(alleles_dict[tup[1]][1]))):
                if alleles_dict[tup[0]][1][i] == '-' or alleles_dict[tup[1]][1][i] == '-':
                    pass
                elif int(alleles_dict[tup[0]][1][i]) != int(alleles_dict[tup[1]][1][i]):
                    jumps += 1
            print(str(tup) + ', Number of differences: ' + str(jumps))
            if jumps >= min(len(alleles_dict[tup[0]][1]), len(alleles_dict[tup[1]][1])) - jumps:#This condition may be wrong
                # print(alleles_dict[tup[1]])
                alleles_dict[tup[1]][1] = GraphicalGenotypeController.swap_gene(alleles_dict[tup[1]][1])
                # print(alleles_dict[tup[1]])

    @staticmethod
    def pairwise(iterable):
        """s -> (s0, s1), (s2, s3), (s4, s5), ..."""
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    @staticmethod
    def swap_gene(allele2):
        print(allele2)
        allele2 = list(allele2)
        for i in range(0, len(allele2)):
            if allele2[i] != '-':
                if allele2[i] == '1':
                    allele2[i] = '0'
                else:
                    allele2[i] = '1'
        allele2 = ''.join(allele2)
        print('swapped: ' + allele2)
        return allele2
