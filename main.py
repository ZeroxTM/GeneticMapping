# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtGui import QPalette, QColor
from PySide2.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileDialog
from PySide2.QtCore import QFile, Qt, QDir
from PySide2.QtUiTools import QUiLoader

from classes.LinkageGroup import LinkageGroup
# from controllers.StatisticsController import StatisticsController
from controllers.GraphicalGenotypeController import GraphicalGenotypeController
from controllers.LinkagesController import LinkagesController
from controllers.MarkersTabController import MarkersTabController
from controllers.FileBrowserController import FileBrowserController
from controllers.StatisticsController import StatisticsController


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.current_hover = [0, 0]
        self.current_hover2 = [0, 0]
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        self.ui.show()
        ui_file.close()

    def set_menu_functionality(self):
        self.ui.actionImport_Map_Data.triggered.connect(self.import_file)
        self.ui.actionQuit.triggered.connect(self.ui.close)
        self.ui.markersTable.setMouseTracking(True)
        self.ui.genotypingTable.setMouseTracking(True)
        self.ui.markersTable.cellEntered.connect(self.cellHover)
        self.ui.markersTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.markersTable.customContextMenuRequested.connect(self.on_right_click)
        self.ui.genotypingTable.cellEntered.connect(self.cellHover2)

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
        self.current_hover = [row, column]

    def init_file_system_tree(self):
        model = QFileSystemModel(nameFilterDisables=False)
        model.setRootPath("Desktop")
        model.setNameFilters(["*.txt"])
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

    def import_file(self):
        path, _ = QFileDialog().getOpenFileName(QApplication.activeWindow(), "Select a file to open", filter="*.txt")
        print(path) if path else print("No path")

    def set_controllers_ui_ref(self):
        FileBrowserController.ui = self.ui
        MarkersTabController.ui = self.ui
        StatisticsController.ui = self.ui
        GraphicalGenotypeController.ui = self.ui
        LinkagesController.ui = self.ui
        self.ui.mainTabs.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    widget.init_file_system_tree()
    widget.set_menu_functionality()
    widget.set_controllers_ui_ref()
    # widget.show()
    sys.exit(app.exec_())
