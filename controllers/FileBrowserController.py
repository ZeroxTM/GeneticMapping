import pandas as pd
from PySide2.QtWidgets import QMessageBox

from controllers.MarkersTabController import MarkersTabController as mtc

class FileBrowserController:
    ui = None #Static UI reference variable
    @staticmethod
    def load_file(path):
        print(path)
        if (path[-4:] == '.txt'):
            df = pd.read_csv(path, sep="\t", header=None)
            df.columns = df.iloc[0]
            df = df.drop(df.index[0])
            df = df.drop(['im', 'indexOnPath'], axis=1)
            print(df)
            QMessageBox.information(FileBrowserController.ui, "Info", "File was loaded successfully.")
            mtc.fetch_markers(df)

        else:
            print("Invalid file type")
            QMessageBox.information(FileBrowserController.ui, "Warning", "Invalid file format, please choose .txt file")
