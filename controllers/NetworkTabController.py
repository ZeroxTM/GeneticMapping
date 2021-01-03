import copy

from Data import Data
from classes.CheckableComboBox import CheckableComboBox
from classes.Network import Network


class NetworkTabController:
    ui = None
    linkages_comboBox = None

    @staticmethod
    def initialize_combobox(linkage_groups):
        NetworkTabController.linkages_comboBox = CheckableComboBox(NetworkTabController.ui.linkages_comboBox)
        NetworkTabController.linkages_comboBox.addItem("Select linkages for drawing", checkable=False)
        for key in list(linkage_groups.keys()):
            NetworkTabController.linkages_comboBox.addItem(
                "LinkageGroup: " + str(key) + " - Number of markers: " + str(len(linkage_groups[key].markers)))

    @staticmethod
    def build_network():
        net = Network(nodes=[], edges=[], mst=None, skeleton=None, cutoff=0.5)
        selected_linkages_ids = NetworkTabController.linkages_comboBox.get_selected()
        selected_linkages = list()
        print("Selected linakge groups:" + str(selected_linkages_ids))
        print(Data.linkage_groups.values())
        print(Data.linkage_groups.keys())
        if len(selected_linkages_ids) > 0:
            for i in range(0, len(list(Data.linkage_groups))+1):
                if i in selected_linkages_ids:
                    selected_linkages.append(list(Data.linkage_groups.values())[i-1])
            print(selected_linkages)
            net.initialize_network(selected_linkages)
            Data.network = net
            NetworkTabController.ui.calc_mst_btn.setEnabled(True)
            NetworkTabController.ui.draw_pajek_btn.setEnabled(True)
            NetworkTabController.ui.subdivide_btn.setEnabled(True)
        else:
            print("No linkages were selected")
            NetworkTabController.ui.calc_mst_btn.setEnabled(False)
            NetworkTabController.ui.draw_pajek_btn.setEnabled(False)
            NetworkTabController.ui.subdivide_btn.setEnabled(False)

    @staticmethod
    def calculate_mst():
        Data.network.mst = Data.network.calc_MST_net(bPrint=True,bPrintDetails=True)

