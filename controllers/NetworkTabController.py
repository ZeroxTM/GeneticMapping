import copy
import os
import subprocess
import time

import pyautogui
from PySide2 import QtCore
from PySide2.QtWidgets import QFileDialog, QApplication, QMessageBox

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
        net.initialize_network(selected_linkages)
        Data.network = net
        NetworkTabController.ui.calc_mst_btn.setEnabled(True)
        NetworkTabController.ui.draw_pajek_btn.setEnabled(True)
        NetworkTabController.ui.subdivide_btn.setEnabled(True)
        total = 0
        [total := len(m.markers) + total for m in selected_linkages]
        NetworkTabController.ui.log_plainTextEdit.appendPlainText(
            f"Network was built successfully!"
            f"\n\t{total - len(net.nodes)} out of {total} nodes were found without edges and were removed."
            f"\n\t#Nodes: {len(net.nodes)}"
            f"\n\t#Edges: {len(net.edges)}")

    @staticmethod
    def calculate_mst():
        net = Data.network
        net.mst = net.calc_MST_net(bPrint=True, bPrintDetails=False)
        # net.mst = net.calc_max_MST()
        print(net.mst.idNodesOnPathLongest())

    @staticmethod
    def subdivide_network():
        linear_net = Data.network.makeLinearContigClusters(bExcludeNodesCausingNonLinearClusters=True)
        pajek_path = os.getcwd() + '\Pajek64\Pajek.exe'

        try:
            path, _ = QFileDialog().getSaveFileName(QApplication.activeWindow(), filter='*.net')
            Network.print_pajek_network(plot_net=linear_net, sFileName=path)
            QMessageBox.information(NetworkTabController.ui, "Info", "Save Success\nMap "
                                                                     "was successfully saved to path")
        except():
            QMessageBox.information(NetworkTabController.ui, "Warning",
                                    "Save Failed\nAn error has occurred!")

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

            subprocess.Popen([pajek_path, path])
            # time.sleep(5)
            # (x, y) = pyautogui.position()
            # pyautogui.click(pyautogui.locateCenterOnScreen('icon.png'))
            # pyautogui.moveTo(x, y)
