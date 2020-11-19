from PySide2.QtWidgets import QTableWidgetItem


class MarkersTabController:
    ui = None

    @staticmethod
    def fetch_markers(data):  # Fetch data into table view markersTable
        markersTable = MarkersTabController.ui.markersTable
        markersTable.setItem(0, 0, QTableWidgetItem("text1"))