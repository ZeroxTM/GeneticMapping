import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QComboBox, QApplication, QLabel, QMainWindow, QWidget


# subclass
# class CheckableComboBox(QComboBox):
#     # once there is a checkState set, it is rendered
#     # here we assume default Unchecked
#     def addItem(self, item, checkable=True):
#         super(CheckableComboBox, self).addItem(item)
#         item = self.model().item(self.count() - 1, 0)
#         if checkable:
#             item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
#             item.setCheckState(Qt.Unchecked)
#         else:
#             item.setFlags(Qt.ItemIsEnabled)
#
#     def itemChecked(self, index):
#         item = self.model().item(index, 0)
#         return item.checkState() == Qt.Checked

# subclass
class CheckableComboBox:
    # once there is a checkState set, it is rendered
    # here we assume default Unchecked
    def __init__(self, ComboBox):
        self.ComboBox = ComboBox

    def addItem(self, item, checkable=True):
        self.ComboBox.addItem(item)
        item = self.ComboBox.model().item(self.ComboBox.count() - 1, 0)
        if checkable:
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
        else:
            item.setFlags(Qt.ItemIsEnabled)

    def itemChecked(self, index):
        item = self.ComboBox.model().item(index, 0)
        return item.checkState() == Qt.Checked

    def get_selected(self):
        checked = []
        for i in range(1, self.ComboBox.count()):
            item = self.ComboBox.model().item(i, 0)
            if item.checkState() == Qt.Checked:
                checked.append(i)
        return checked



# # the basic main()
# app = QApplication(sys.argv)
# dialog = QMainWindow()
# mainWidget = QWidget()
# dialog.setCentralWidget(mainWidget)
# ComboBox = CheckableComboBox(mainWidget)
# ComboBox.addItem("Combobox Item ", checkable=False)
# for i in range(6):
#     ComboBox.addItem("Combobox Item " + str(i))
#
# dialog.show()
# sys.exit(app.exec_())

