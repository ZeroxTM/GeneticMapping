import os
import re

import pandas as pd
from PySide2.QtWidgets import QMessageBox, QFileDialog

from controllers.GeneticMapController import GeneticMapController
from controllers.MarkersTabController import MarkersTabController as mtc


class FileBrowserController:
    ui = None  # Static UI reference variable
    file_chosen = False

    @staticmethod
    def load_file(path):
        dff = None
        if path[-4:] == '.txt':
            try:
                df = FileBrowserController.read_map_file(path)
                if os.path.exists(path[:-4] + '-data.txt'):
                    ddf = pd.read_csv(path[:-4] + '-data.txt', sep="\t", header=None)
                    print("found!")
                else:
                    QMessageBox.information(FileBrowserController.ui, "Warning",
                                            "Map data was not found.\n Please locate map data file.")
                    path2, _ = QFileDialog().getOpenFileName(FileBrowserController.ui, "Import", filter="*.txt")
                    if not path2: return
                    FileBrowserController.file_chosen = not FileBrowserController.file_chosen
                    ddf = pd.read_csv(path2, sep="\t", header=None)
                    ddf.columns = ['marker_name', 'properties']
                    FileBrowserController.validate_map_data(ddf)
                mtc.fetch_markers(df, ddf)
                GeneticMapController.load_file(path)
                FileBrowserController.enable_tabs()
                FileBrowserController.ui.importStatus.setText("Imported map: " + path + "\nData: " + path2)
                FileBrowserController.ui.importStatus.setFixedWidth(900)
                FileBrowserController.ui.importStatus.setFixedHeight(30)
            except ValueError:
                QMessageBox.information(FileBrowserController.ui, "Warning",
                                        "Invalid data format\n Please locate a valid map data file.")
        else:
            print("Invalid file type")
            QMessageBox.information(FileBrowserController.ui, "Warning", "Invalid file format, please choose .txt file")

    @staticmethod
    def read_map_file(path):
        df = pd.read_csv(path, sep="\t", header=None)
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])
        df = df.drop(['indexOnPath'], axis=1)
        QMessageBox.information(FileBrowserController.ui, "Info", "File was loaded successfully.")
        df = df.drop_duplicates(subset=['marker'], keep='first')  # Filtrate duplicate markers
        return df

    @staticmethod
    def enable_tabs():
        for i in range(1, 6):
            FileBrowserController.ui.mainTabs.setTabEnabled(i, True) if i != 1 else None

    @staticmethod
    def validate_map_data(ddf):
        for allele in ddf['properties']:
            if not FileBrowserController.allele_match(allele):
                raise ValueError

    """
            Regex that checks if every allele string contains 1,0,- only
        """

    @staticmethod
    def allele_match(strg, search=re.compile(r'[^0-1\-]').search):
        return not bool(search(strg))
