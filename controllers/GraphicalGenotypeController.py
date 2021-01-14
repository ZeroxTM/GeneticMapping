"""
 @Time : 30/11/2020 15:47
 @Author : Alaa Grable, Adam Mahameed
 """
#TODO: add Restore button and Load current alleles
import copy
from itertools import tee

from PySide2 import QtCore, QtGui
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog, QApplication
from pandas import DataFrame, ExcelWriter

from Data import Data
from classes.Marker import Marker


class GraphicalGenotypeController:
    ui = None
    is_changed = False
    colors = {
        "1": QtGui.QColor(128, 0, 0, 180),
        "0": QtGui.QColor(0, 128, 0),
        "-": QtGui.QColor(134, 136, 138, 180),
        "No Data": QtGui.QColor(211, 211, 211, 180),
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
            alleles = marker.alleles[0] if len(marker.alleles) != 0 else 'No Data'
            orig_alleles_dict[row] = [marker.id, alleles]
            if alleles == 'No Data':
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
                    #item.setFlags(QtCore.Qt.ItemIsEnabled)
                    GraphicalGenotypeController.ui.genotypingTable.setItem(row, col_index, item)
        Data.orig_alleles_dict = orig_alleles_dict
        GraphicalGenotypeController.ui.genotypingTable.cellChanged.connect(GraphicalGenotypeController.cell_changed)

    @staticmethod
    def cell_changed(row, column):
        item = GraphicalGenotypeController.ui.genotypingTable.item(row, column)
        color = GraphicalGenotypeController.colors[str(item.text())]
        if str(item.text()) == '1':
            color.setAlpha(150)
        elif str(item.text()) == '0':
            color.setAlpha(220)
        else:
            color.setAlpha(150)
        item.setBackground(color)
        #item.setBackground(GraphicalGenotypeController.colors[str(item.text())])
        new_allele = ""
        for column in range(GraphicalGenotypeController.ui.genotypingTable.columnCount()):
            new_allele += str(GraphicalGenotypeController.ui.genotypingTable.item(row, column).text())
        Marker.markers[row].alleles = [new_allele]
        GraphicalGenotypeController.is_changed = True

    @staticmethod
    def update_graphical_genotype_map(updated_alleles_dict, swapped_rows):
        for index in swapped_rows:
            data = updated_alleles_dict[index]
            for i in range(len(data[1])):
                item = QTableWidgetItem(data[1][i])
                color = GraphicalGenotypeController.colors[data[1][i]]
                if data[1][i] == '1':
                    color.setAlpha(150)
                if data[1][i] == '0':
                    color.setAlpha(220)
                item.setBackground(color)
                #item.setFlags(QtCore.Qt.ItemIsEnabled)
                GraphicalGenotypeController.ui.genotypingTable.setItem(index, i, item)
        QMessageBox.information(GraphicalGenotypeController.ui, "Info",
                                str(len(updated_alleles_dict)) + " alleles were renamed successfully.")
        GraphicalGenotypeController.ui.rename_alleles_btn.setEnabled(False)

    @staticmethod
    def rename_alleles():
        # Filter out markers without alleles info
        alleles_dict = copy.deepcopy(Data.orig_alleles_dict)
        swapped_rows = list()
        for k in list(alleles_dict):
            if alleles_dict[k][1] == 'No Data':
                del alleles_dict[k]
        Data.mod_alleles_dict = alleles_dict
        # Time for the real work here
        tuples_list = list()
        for x, y in pairwise(list(alleles_dict)):
            tuples_list.append(tuple((int(x), int(y))))
        for tup in tuples_list:
            jumps = 0
            for i in range(0, min(len(alleles_dict[tup[0]][1]), len(alleles_dict[tup[1]][1]))):
                if alleles_dict[tup[0]][1][i] == '-' or alleles_dict[tup[1]][1][i] == '-':
                    pass
                elif int(alleles_dict[tup[0]][1][i]) != int(alleles_dict[tup[1]][1][i]):
                    jumps += 1
            print(str(tup) + ', Number of differences: ' + str(jumps))
            if jumps >= min(len(alleles_dict[tup[0]][1]),
                            len(alleles_dict[tup[1]][1])) - jumps:  # This condition may be wrong
                alleles_dict[tup[1]][1] = swap_gene(alleles_dict[tup[1]][1])
                swapped_rows.append(tup[1])
        Data.mod_alleles_dict = alleles_dict
        GraphicalGenotypeController.update_graphical_genotype_map(alleles_dict, swapped_rows)

    @staticmethod
    def export_alleles():
        msgBox = QMessageBox(QApplication.activeWindow())
        msgBox.setText("Data export")
        msgBox.setInformativeText("What would you like to export?")
        exp_orig = msgBox.addButton("Original Data", QMessageBox.ActionRole)
        exp_renamed = msgBox.addButton("Renamed Alleles Data", QMessageBox.ActionRole)
        if len(Data.mod_alleles_dict) == 0:
            msgBox.removeButton(msgBox.buttons()[1])
        msgBox.addButton(QMessageBox.Cancel)
        export = True
        msgBox.exec_()
        if msgBox.clickedButton() == exp_orig:
            data = Data.orig_alleles_dict
            print("Exporting renames alleles data...")
        elif msgBox.clickedButton() == exp_renamed:
            data = Data.mod_alleles_dict
            print("Exporting renamed alleles data...")
        else:
            export = False
            print("Cancel")
        if export:
            try:
                path, _ = QFileDialog().getSaveFileName(QApplication.activeWindow(), filter='*.xlsx')
                df = DataFrame.from_dict(data, orient='index', columns=['Marker ID', 'Allele'])
                with ExcelWriter(path) as writer:
                    df.to_excel(writer)
                QMessageBox.information(GraphicalGenotypeController.ui, "Info", "Export Success\nAlleles data was "
                                                                                "exported successfully to path")
            except():
                QMessageBox.information(GraphicalGenotypeController.ui, "Warning",
                                        "Export Failed\nAn error has occurred!")


def pairwise(iterable):
    """s -> (s0, s1), (s1, s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def swap_gene(allele2):
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
