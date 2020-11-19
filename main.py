# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileDialog
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from controllers.MarkersTabController import MarkersTabController
from controllers.FileBrowserController import FileBrowserController


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
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
        print(name)

    def set_controllers_ui_ref(self):
        FileBrowserController.ui = self.ui
        MarkersTabController.ui = self.ui

if __name__ == "__main__":
    app = QApplication([])
    widget = main()
    widget.init_file_system_tree()
    widget.set_menu_functionality()
    widget.set_controllers_ui_ref()
   # widget.show()
    sys.exit(app.exec_())
