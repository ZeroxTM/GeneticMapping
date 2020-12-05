"""
 @Time : 03/12/2020 20:22
 @Author : Alaa Grable
 """
from PySide2 import QtCore
from PySide2.QtWidgets import QTableWidgetItem
from classes.Linkage import Linkage
from classes.LinkageGroup import LinkageGroup
from controllers.MarkersTabController import MarkersTabController


class LinkagesController:
    ui = None
    # a dictionary to store each linkage group id and it's linkages
    # where the key is the linkage group id
    # and the value is a list of objects of Linkage (between 2 markers)
    markers_linkages = dict()

    @staticmethod
    def display_linkages_of(row):
        """
        A method that takes the row of the selected marker from the markers list,
        and then displays it's linkages with the other markers from the same
        linkage group on the table in the linkages tab.
        :param row:
        :return:
        """
        # Gets the Corresponding marker from the selected row(marker)
        marker = MarkersTabController.markers[row]
        # Change the view to the linkages tab
        LinkagesController.ui.mainTabs.setCurrentIndex(1)
        # ListOfKeys = [key for (key, value) in LinkageGroup.LinkageGroups.items() if value == marker]
        # Get the values of the linkage groups dictionary
        list_of_values = LinkageGroup.LinkageGroups.items()
        # find the key where this chosen marker is value at
        marker_key = next((value[0] for value in list_of_values if marker in value[1].markers), None)
        # Get the linkage group of that marker
        linkage_group = LinkageGroup.LinkageGroups[marker_key]
        # Get all the markers in the same linkage group as the chosen marker
        linkage_group_markers = linkage_group.markers.copy()
        # Remove the chosen marker from the list to iterate over the rest of the marker
        linkage_group_markers.remove(marker)
        # Iterate over the rest of the markers in the list (after removing the chosen marker)
        # and for each of these combinations, create a linkage object, and store it in
        # the markers_linkages dictionary with the key being the the linkage group id
        for row_index, markr in enumerate(linkage_group_markers):
            LinkagesController.ui.linkageTable.insertRow(row_index)
            linkage = Linkage(linkage_group.id, marker, markr)
            available = LinkagesController.markers_linkages.get(linkage_group.id, None)
            if available is None:
                LinkagesController.markers_linkages[linkage_group.id] = list()
                LinkagesController.markers_linkages[linkage_group.id].append(linkage)
            elif linkage not in available:
                LinkagesController.markers_linkages[linkage_group.id].append(linkage)
            else:
                linkage = next((lnkage for lnkage in available if lnkage == linkage), None)
            for column, variable in enumerate(vars(linkage).items()):
                item = QTableWidgetItem(str(variable[1]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                LinkagesController.ui.linkageTable.setItem(row_index, column, item)
