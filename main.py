# This Python file uses the following encoding: utf-8
import os
import subprocess
import sys
import time

import pandas as pd
import pyautogui
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QFile, Slot, Qt
from PySide2.QtGui import QIcon, QPalette, QColor
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileDialog, QDialog, QMessageBox, \
    QTableWidgetItem
from pajek_tools import PajekWriter
import numpy as np
from Data import Data
from classes.CheckableComboBox import CheckableComboBox
from classes.LinkageGroup import LinkageGroup
from controllers.GeneticMapController import GeneticMapController
from controllers.NetworkTabController import NetworkTabController
from controllers.FileBrowserController import FileBrowserController
from controllers.GraphicalGenotypeController import GraphicalGenotypeController
from controllers.LinkagesController import LinkagesController
from controllers.MapComparisonController import MapComparisonController
from controllers.MarkersTabController import MarkersTabController
from controllers.StatisticsController import StatisticsController

class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.current_hover = [0, 0]
        self.current_hover2 = [0, 0]
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        ui_file = QFile(os.path.join(os.path.dirname(__file__), "form.ui"))
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()
        self.ui.show()


    def set_menu_functionality(self):
        NetworkTabController.linkages_comboBox = CheckableComboBox(self.ui.linkages_comboBox)
        NetworkTabController.linkages_comboBox.ComboBox.view().pressed.connect(self.handleItemPressed)
        self.ui.actionImport_Map_Data.triggered.connect(self.import_file)
        self.ui.actionQuit.triggered.connect(self.ui.close)
        self.ui.markersTable.setMouseTracking(True)
        self.ui.genotypingTable.setMouseTracking(True)
        self.ui.markersTable.cellEntered.connect(self.cellHover)
        self.ui.markersTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.markersTable.customContextMenuRequested.connect(self.on_right_click)
        self.ui.genotypingTable.cellEntered.connect(self.cellHover2)
        self.ui.import_btn.clicked.connect(self.import_map2)
        self.ui.mainTabs.currentChanged.connect(self.onChange)
        self.ui.mainTabs.blockSignals(False)
        self.ui.actionOpen_Graph_with_Pajek.triggered.connect(self.Network_structure)
        self.ui.actionInspect_Parallel_Linkage.triggered.connect(self.Network_structure)
        self.ui.actionTest_Cluster_Linear_Structure.triggered.connect(self.Network_structure)
        self.ui.actionSubdivide_Cluster_Into.triggered.connect(self.Network_structure)
        self.ui.actionCompare_Maps.triggered.connect(lambda _: self.ui.mainTabs.setCurrentIndex(5) if FileBrowserController.file_chosen else None)
        self.ui.actionEdit_Input_Map.triggered.connect(lambda _: self.ui.mainTabs.setCurrentIndex(4) if FileBrowserController.file_chosen else None)
        self.ui.actionAbout.triggered.connect(lambda _: QMessageBox().information(self.ui, "About..", "Copyright (c) 2020 Alaa Grable, Adam Mahamed."))

    def handleItemPressed(self, index):
        item = self.ui.linkages_comboBox.model().itemFromIndex(index)
        linkage_name = item.text().split()[1]
        linkages_markers = item.text().split()[6]
        if index.row() != 0:
            if item.checkState() == QtCore.Qt.Checked:
                if linkage_name in NetworkTabController.linkages_selected:
                    NetworkTabController.linkages_selected.remove(linkage_name)
                if linkages_markers in NetworkTabController.linkages_markers:
                    NetworkTabController.linkages_markers.remove(linkages_markers)
                self.display_linkages()
                item.setCheckState(QtCore.Qt.Unchecked)
                if len(NetworkTabController.linkages_comboBox.get_selected()) == 0:
                    self.ui.draw_network_btn.setEnabled(False)
                self.ui.calc_mst_btn.setEnabled(False)
                self.ui.draw_pajek_btn.setEnabled(False)
                self.ui.subdivide_btn.setEnabled(False)
            else:
                if linkage_name not in NetworkTabController.linkages_selected:
                    NetworkTabController.linkages_selected.append(linkage_name)
                if linkages_markers not in NetworkTabController.linkages_markers:
                    NetworkTabController.linkages_markers.append(linkages_markers)
                self.display_linkages()
                item.setCheckState(QtCore.Qt.Checked)
                self.ui.draw_network_btn.setEnabled(True)

    def display_linkages(self):
        self.ui.selected_linkages_textEdit.setText(', '.join(NetworkTabController.linkages_selected))
        markers = 0
        for length in NetworkTabController.linkages_markers:
            markers += int(length)
        self.ui.total_markers_textEdit.setText(str(markers))

    # @pyqtSlot()
    def onChange(self, i):
        if i == 3:
            self.ui.rename_alleles_btn.show()
            self.ui.export_alleles_btn.show()
            self.ui.export_alleles_btn.setText("Export Alleles Genotyping")
            self.ui.groupBox_2.setVisible(True)
            self.ui.groupBox_3.setVisible(True)
        elif i == 2:
            self.ui.groupBox_2.setVisible(False)
            self.ui.groupBox_3.setVisible(False)
            self.ui.export_alleles_btn.setText("Export Alleles Genotyping")
            self.ui.rename_alleles_btn.hide()
            self.ui.export_alleles_btn.hide()
        elif i == 4:
            self.ui.export_alleles_btn.show()
            self.ui.export_alleles_btn.setText("Save")
            self.ui.rename_alleles_btn.hide()
        elif i == 5:
            self.ui.groupBox_2.setVisible(False)
            self.ui.groupBox_3.setVisible(False)
            self.ui.export_alleles_btn.hide()
        else:
            self.ui.export_alleles_btn.setText("Export Alleles Genotyping")
            self.ui.rename_alleles_btn.hide()
            self.ui.export_alleles_btn.hide()
            self.ui.groupBox_2.setVisible(True)
            self.ui.groupBox_3.setVisible(True)

    def import_map2(self):
        path, _ = QFileDialog().getOpenFileName(QApplication.activeWindow(), "Select a file to open", filter="Map data (*.txt *.csv)")
        MapComparisonController.compare_maps(path) if path else print("a")

    def on_right_click(self, pos):
        it = self.ui.markersTable.itemAt(pos)
        if it is None: return
        marker = it.row()
        item_range = QtWidgets.QTableWidgetSelectionRange(0, marker, self.ui.markersTable.rowCount() - 1, marker)
        self.ui.markersTable.setRangeSelected(item_range, True)
        menu = QtWidgets.QMenu()
        view_linkages = menu.addAction("View Linkages")
        action = menu.exec_(self.ui.markersTable.viewport().mapToGlobal(pos))
        if action == view_linkages:
            self.ui.mainTabs.setTabEnabled(1, True)
            LinkagesController.display_linkages_of(marker)

    def cellHover2(self, row, column):
        """
        Edits statistics tab on hover over the table of graphical genotyping
        """
        item = self.ui.genotypingTable.item(row, column)
        if self.current_hover2 != [row, column] and item is not None:
            marker = MarkersTabController.markers[row]
            self.ui.marker_id.setText(str(marker.id))
            self.ui.marker_name.setText(str(marker.name))
            self.ui.marker_genotype.setText(
                str(marker.alleles) if len(MarkersTabController.markers[row].alleles) != 0 else 'N/A')
            self.ui.marker_genotype_ns.setText(
                "n0: " + str(marker.n0) + " | n1: " + str(marker.n1) + " | n-Miss: " + str(marker.n_missing))
            self.ui.marker_skeleton_ind.setText(str(marker.skeleton_index))
            self.ui.marker_gencords.setText(str(marker.coordinateGenet))
            self.ui.lg_id.setText(str(marker.linkage_id))
            self.ui.lg_name.setText(str(marker.linkage_group))
            self.ui.lg_markers.setText(str(len(LinkageGroup.LinkageGroups[marker.linkage_group].markers)))
        self.current_hover2 = [row, column]

    def cellHover(self, row, column):
        """
        Edits statistics tab on hover over the table
        """
        item = self.ui.markersTable.item(row, column)
        if self.current_hover != [row, column] and item is not None:
            self.ui.marker_id.setText(self.ui.markersTable.item(row, 0).text())
            self.ui.marker_name.setText(self.ui.markersTable.item(row, 1).text())
            self.ui.marker_genotype.setText(self.ui.markersTable.item(row, 2).text())
            self.ui.marker_genotype_ns.setText(
                "n0: " + self.ui.markersTable.item(row, 3).text() + " | n1: " + self.ui.markersTable.item(row, 4).text()
                + " | n-Miss: " + self.ui.markersTable.item(row, 5).text())
            self.ui.marker_skeleton_ind.setText(self.ui.markersTable.item(row, 14).text())
            self.ui.marker_gencords.setText(self.ui.markersTable.item(row, 15).text())
            self.ui.lg_id.setText(self.ui.markersTable.item(row, 11).text())
            self.ui.lg_name.setText(self.ui.markersTable.item(row, 12).text())
            self.ui.lg_markers.setText(
                str(len(LinkageGroup.LinkageGroups[self.ui.markersTable.item(row, 12).text()].markers)))
        if Data.network is not None:
            if Data.skeleton_nodes is not None:
                if self.ui.markersTable.item(row, 1).text() in [node.marker.name for node in Data.skeleton_nodes]:
                    self.ui.lg_skeleton.setChecked(True)
                else:
                    self.ui.lg_skeleton.setChecked(False)
        self.current_hover = [row, column]

    def init_file_system_tree(self):
        model = QFileSystemModel(nameFilterDisables=False)
        model.setRootPath("Desktop")
        model.setNameFilters(["*.txt", "*.csv"])
        self.ui.browserTreeView.setModel(model)
        self.ui.browserTreeView.setRootIndex(model.index("Desktop"))
        self.ui.browserTreeView.hideColumn(1)
        self.ui.browserTreeView.hideColumn(2)
        self.ui.browserTreeView.hideColumn(3)
        self.ui.browserTreeView.doubleClicked.connect(self.onClicked)

    def onClicked(self, index):
        path = self.sender().model().filePath(index)
        if path is not None:
            FileBrowserController.load_file(path)
        else:
            QMessageBox().warning(self.ui, "Warning", "No File Has Been Chosen!")

    def import_file(self):
        path, _ = QFileDialog().getOpenFileName(QApplication.activeWindow(), "Select a file to open", filter="Map data (*.txt *.csv)")
        if path is not None:
            FileBrowserController.load_file(path)
        else:
            QMessageBox().warning(self.ui, "Warning", "No File Has Been Chosen!")

    def set_controllers_ui_ref(self):
        FileBrowserController.ui = self.ui
        MarkersTabController.ui = self.ui
        StatisticsController.ui = self.ui
        GraphicalGenotypeController.ui = self.ui
        LinkagesController.ui = self.ui
        MapComparisonController.ui = self.ui
        NetworkTabController.ui = self.ui
        GeneticMapController.ui = self.ui
        self.ui.mainTabs.setCurrentIndex(0)

    @Slot()
    def Network_structure(self):
        self.ui.mainTabs.setCurrentIndex(2) if FileBrowserController.file_chosen else None

    def initialize_clicks(self):
        self.ui.rename_alleles_btn.clicked.connect(GraphicalGenotypeController.rename_alleles)
        self.ui.export_alleles_btn.clicked.connect(self.export_alleles_btn_clicked)
        self.ui.rename_alleles_btn.hide()
        self.ui.export_alleles_btn.hide()
        self.ui.draw_network_btn.clicked.connect(NetworkTabController.build_network)
        self.ui.calc_mst_btn.clicked.connect(NetworkTabController.calculate_mst)
        self.ui.subdivide_btn.clicked.connect(NetworkTabController.subdivide_network)
        self.ui.draw_pajek_btn.clicked.connect(NetworkTabController.draw_pajek)
        self.ui.draw_network_btn.setEnabled(False)
        self.ui.calc_mst_btn.setEnabled(False)
        self.ui.draw_pajek_btn.setEnabled(False)
        self.ui.subdivide_btn.setEnabled(False)
        self.ui.lg_skeleton.toggled.connect(
            lambda checked: self.ui.lg_skeleton.setChecked(False) if checked else self.ui.lg_skeleton.setChecked(True))



    def export_alleles_btn_clicked(self):
        if self.ui.mainTabs.currentIndex() == 3:
            GraphicalGenotypeController.export_alleles()
        else:
            GeneticMapController.save_file()



    def disable_tabs(self):
        for i in range(1, 6):
            self.ui.mainTabs.setTabEnabled(i, False)
        self.ui.label_recomb.setHidden(True)
        self.ui.map_recombination.setHidden(True)


if __name__ == "__main__":

    try:
        from PySide2.QtWinExtras import QtWin
        myappid = 'mycompany.myproduct.subproduct.version'
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("images/DNA.png"))
    widget = main()
    widget.init_file_system_tree()
    widget.set_menu_functionality()
    widget.set_controllers_ui_ref()
    widget.initialize_clicks()
    widget.disable_tabs()
    # widget.show()
    sys.exit(app.exec_())