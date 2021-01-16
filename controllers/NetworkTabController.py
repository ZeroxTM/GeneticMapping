import copy
import os
import subprocess
import time

import pyautogui
from PySide2 import QtCore
import numpy as np
from PySide2.QtWidgets import QFileDialog, QApplication, QMessageBox, QInputDialog, QTableWidgetItem
from PySide2 import QtGui

from Data import Data
from classes.CheckableComboBox import CheckableComboBox
from classes.Network import Network


class NetworkTabController:
    ui = None
    linkages_comboBox = None
    linkages_selected = list()
    linkages_markers = list()

    @staticmethod
    def initialize_combobox(linkage_groups):
        # NetworkTabController.linkages_comboBox = CheckableComboBox(NetworkTabController.ui.linkages_comboBox)
        NetworkTabController.linkages_comboBox.addItem("Select linkages for drawing", checkable=False)
        for key in list(linkage_groups.keys()):
            NetworkTabController.linkages_comboBox.addItem(
                "LinkageGroup: " + str(key) + " - Number of markers: " + str(len(linkage_groups[key].markers)))

    @staticmethod
    def build_network():
        QMessageBox.information(NetworkTabController.ui, "Notice",
                                "Please note, markers with no alleles data will not be included in the network.")
        net = Network(nodes=[], edges=[], mst=None, skeleton=None,
                      cutoff=float(NetworkTabController.ui.cutoff_textfield.toPlainText()))
        selected_linkages_ids = NetworkTabController.linkages_comboBox.get_selected()
        NetworkTabController.ui.log_plainTextEdit.clear()
        NetworkTabController.ui.log_plainTextEdit.insertPlainText("Building network of selected linkages...")
        NetworkTabController.ui.log_plainTextEdit.appendPlainText(
            "Selected linkages IDs: " + str(selected_linkages_ids))
        selected_linkages = list()
        print("Selected linkage groups:" + str(selected_linkages_ids))
        print(Data.linkage_groups.values())
        print(Data.linkage_groups.keys())
        for i in range(0, len(list(Data.linkage_groups)) + 1):
            if i in selected_linkages_ids:
                selected_linkages.append(list(Data.linkage_groups.values())[i - 1])
        print(selected_linkages)
        net.initialize_network(selected_linkages, filterate=NetworkTabController.ui.filterate_checkBox.isChecked())
        Data.network = net
        NetworkTabController.ui.calc_mst_btn.setEnabled(True)
        NetworkTabController.ui.draw_pajek_btn.setEnabled(True)
        NetworkTabController.ui.subdivide_btn.setEnabled(True)
        total = 0
        [total := len(m.markers) + total for m in selected_linkages]
        NetworkTabController.ui.log_plainTextEdit.appendPlainText(
            f"Network was built successfully!"
            f"\n\t{Network.no_data_markers} out of {total} nodes were found without edges and were removed."
            f"\n\t{Network.low_quality_markers} low quality markers were found and filtered out (p missing > 20% / allele segregation > 3.84)"
            f"\n\t#Nodes: {len(net.nodes)}"
            f"\n\t#Edges: {len(net.edges)}\n")
        Network.low_quality_markers = 0

    @staticmethod
    def calculate_mst():
        net = Data.network
        NetworkTabController.ui.log_plainTextEdit.appendPlainText(
            f"Calculating minimal spanning tree of {len(net.nodes)} nodes and {len(net.edges)} edges")
        net.mst = net.calc_MST_net(bPrint=True, bPrintDetails=False)
        # net.mst = net.calc_max_MST()
        NetworkTabController.ui.log_plainTextEdit.appendPlainText(f"Network was built successfully!"
                                                                  f"\n\t#Nodes: {len(net.mst.nodes)}"
                                                                  f"\n\t#Edges: {len(net.mst.edges)}\n")
        NetworkTabController.color_skeleton()
        print(net.mst.idNodesOnPathLongest())

    @staticmethod
    def color_skeleton():
        color = list(np.ceil(np.random.random(size=3) * 256))
        if color in Data.skeleton_colors:
            while color not in Data.skeleton_colors:
                color = list(np.ceil(np.random.random(size=3) * 256))
        Data.skeleton_colors.append(color)
        mst_markers = Data.network.mst.nodes
        for node in mst_markers:
            for row in range(NetworkTabController.ui.markersTable.rowCount()):
                item = NetworkTabController.ui.markersTable.item(row, 1)
                if item.text() == node.marker.name:
                    node.marker.skeleton_index = node.id
                    NetworkTabController.ui.markersTable.setItem(row, 14, QTableWidgetItem(str(node.id)))
                    for column in range(NetworkTabController.ui.markersTable.columnCount()):
                        NetworkTabController.ui.markersTable.item(row, column).setBackground(QtGui.QColor(color[0], color[1],
                                                                                          color[2], 70))

    @staticmethod
    def subdivide_network():
        val, ok = QInputDialog.getDouble(QApplication.activeWindow(), "Parallel cutoff",
                                         "Input cutoff value for unproven parallel linkages", 0.25, 0.0, 1.0, decimals=3, step=0.01)
        if ok:
            NetworkTabController.ui.log_plainTextEdit.appendPlainText(f"Testing network for linear structure...")

            linear_net, excluded = Data.network.makeLinearContigClusters(bExcludeNodesCausingNonLinearClusters=True, cutoff=float(
                NetworkTabController.ui.cutoff_textfield.toPlainText()), cutoffParallel=float(val))

            NetworkTabController.ui.log_plainTextEdit.appendPlainText(
                f"{len(Data.network.nodes) - len(linear_net.nodes)} nodes were removed:")

            excluded = [str(str(id) + "\t" + Data.network.nodes[id].caption) for id in excluded]
            for ex in excluded:
                NetworkTabController.ui.log_plainTextEdit.appendPlainText(ex)

            pajek_path = os.getcwd() + '\Pajek64\Pajek.exe'
            try:
                path, _ = QFileDialog().getSaveFileName(QApplication.activeWindow(), filter='*.net')
                Network.print_pajek_network(plot_net=linear_net, sFileName=path)
                QMessageBox.information(NetworkTabController.ui, "Info", "Save Success\nMap "
                                                                         "was successfully saved to path")
            except():
                QMessageBox.information(NetworkTabController.ui, "Warning",
                                        "Save Failed\nAn error has occurred!")
            NetworkTabController.ui.log_plainTextEdit.appendPlainText(
                f"Linear structure network was built successfully!"
                f"\n\t#Nodes: {len(linear_net.nodes)}"
                f"\n\t#Edges: {len(linear_net.edges)}\n")
            subprocess.Popen([pajek_path, path])

    @staticmethod
    def draw_pajek():
        msgBox = QMessageBox(QApplication.activeWindow())
        msgBox.setText("Plot network with Pajek")
        msgBox.setInformativeText("Which network would you like to plot?")
        net_plot = msgBox.addButton("Network", QMessageBox.ActionRole)
        mst_plot = msgBox.addButton("MST of Network", QMessageBox.ActionRole)
        plot = True
        if Data.network.mst == None:
            msgBox.removeButton(msgBox.buttons()[1])
        msgBox.addButton(QMessageBox.Cancel)
        msgBox.exec_()
        if msgBox.clickedButton() == net_plot:
            to_plot = Data.network
            print("Plotting network with Pajek...")
        elif msgBox.clickedButton() == mst_plot:
            to_plot = Data.network.mst
            print("Plotting MST with Pajek...")
        else:
            plot = False
            print("Cancel")

        if plot:
            pajek_path = os.getcwd() + '\Pajek64\Pajek.exe'
            try:
                path, _ = QFileDialog().getSaveFileName(QApplication.activeWindow(), filter='*.net')
                Network.print_pajek_network(plot_net=to_plot, sFileName=path)
                QMessageBox.information(NetworkTabController.ui, "Info", "Save Success\nMap "
                                                                         "was successfully saved to path")
            except():
                QMessageBox.information(NetworkTabController.ui, "Warning",
                                        "Save Failed\nAn error has occurred!")

            NetworkTabController.ui.log_plainTextEdit.appendPlainText(
                f"Network was exported to Pajek format successfully"
                f"\n\t#Nodes: {len(to_plot.nodes)}"
                f"\n\t#Edges: {len(to_plot.edges)}"
                f"\n\tNetwork save path: {path}\n")

            subprocess.Popen([pajek_path, path])
            # time.sleep(5)
            # (x, y) = pyautogui.position()
            # pyautogui.click(pyautogui.locateCenterOnScreen('icon.png'))
            # pyautogui.moveTo(x, y)
