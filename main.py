# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2 import QtWidgets
from PySide2.QtGui import QPalette, QColor
from PySide2.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileDialog
from PySide2.QtCore import QFile, Qt
from PySide2.QtUiTools import QUiLoader

from classes.LinkageGroup import LinkageGroup
#from controllers.StatisticsController import StatisticsController
from controllers.GraphicalGenotypeController import GraphicalGenotypeController
from controllers.MarkersTabController import MarkersTabController
from controllers.FileBrowserController import FileBrowserController


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.current_hover = [0, 0]
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
        self.ui.actionImport_Map_Data.triggered.connect(self.file_open)
        self.ui.actionQuit.triggered.connect(self.ui.close)
        self.ui.markersTable.setMouseTracking(True)
        self.ui.markersTable.cellEntered.connect(self.cellHover)

    # Override
    def cellHover(self, row, column):
        """
        Edits statistics tab on hover over the GUI
        """
        item = self.ui.markersTable.item(row, column)
        # old_item = self.ui.markersTable.item(self.current_hover[0], self.current_hover[1])
        if self.current_hover != [row, column] and item is not None:
            self.ui.marker_id.setText(self.ui.markersTable.item(row, 0).text())
            self.ui.marker_name.setText(self.ui.markersTable.item(row, 1).text())
            self.ui.marker_genotype.setText(self.ui.markersTable.item(row, 2).text())
            self.ui.marker_skeleton_ind.setText(self.ui.markersTable.item(row, 14).text())
            self.ui.marker_gencords.setText(self.ui.markersTable.item(row, 15).text())
            self.ui.lg_id.setText(self.ui.markersTable.item(row, 11).text())
            self.ui.lg_name.setText(self.ui.markersTable.item(row, 12).text())
            self.ui.lg_markers.setText(str(len(LinkageGroup.LinkageGroups[self.ui.markersTable.item(row, 12).text()].markers)))
        self.current_hover = [row, column]

    def init_file_system_tree(self):
        model = QFileSystemModel()
        model.setRootPath("Desktop")
        self.ui.browserTreeView.setModel(model)
        self.ui.browserTreeView.setRootIndex(model.index("Desktop"))
        self.ui.browserTreeView.hideColumn(1)
        self.ui.browserTreeView.hideColumn(2)
        self.ui.browserTreeView.hideColumn(3)
        self.ui.browserTreeView.doubleClicked.connect(self.onClicked)

    def onClicked(self, index):
        path = self.sender().model().filePath(index)
        FileBrowserController.load_file(path)

    def file_open(self):
        name = QFileDialog.getOpenFileName(self, "Import")

    def set_controllers_ui_ref(self):
        FileBrowserController.ui = self.ui
        MarkersTabController.ui = self.ui
        #StatisticsController.ui = self.ui
        GraphicalGenotypeController.ui = self.ui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Way to get screen size #1
    """screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))

    # Way to get screen size #2
    sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
    print(sizeObject.width())"""

    widget = main()
    widget.init_file_system_tree()
    widget.set_menu_functionality()
    widget.set_controllers_ui_ref()
    # widget.show()
    sys.exit(app.exec_())
