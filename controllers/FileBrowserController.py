import os

import pandas as pd
from PySide2.QtWidgets import QMessageBox, QFileDialog

from controllers.MarkersTabController import MarkersTabController as mtc


class FileBrowserController:
    ui = None  # Static UI reference variable

    @staticmethod
    def load_file(path):
        dff = None
        print(path)
        if (path[-4:] == '.txt'):
            df = pd.read_csv(path, sep="\t", header=None)
            df.columns = df.iloc[0]
            df = df.drop(df.index[0])
            df = df.drop(['im', 'indexOnPath'], axis=1)
            QMessageBox.information(FileBrowserController.ui, "Info", "File was loaded successfully.")
            #mtc.fetch_markers(df)

            if (os.path.exists(path[:-4] + '-data.txt')):
                ddf = pd.read_csv(path[:-4] + '-data.txt', sep="\t", header=None)
                print("found!")
            else:
                QMessageBox.information(FileBrowserController.ui, "Warning",
                                        "Map data was not found.\n Please locate map data file.")
                path = QFileDialog.getOpenFileName(FileBrowserController.ui, "Import")
                ddf = pd.read_csv(path[0], sep="\t", header=None)
                ddf.columns = ['marker_name', 'properties']
            mtc.fetch_markers(df, ddf)


        else:
            print("Invalid file type")
            QMessageBox.information(FileBrowserController.ui, "Warning", "Invalid file format, please choose .txt file")
