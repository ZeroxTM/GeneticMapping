"""
 @Time : 09/01/2021 0:27
 @Author : Alaa Grable
 """
from PySide2.QtWidgets import QMessageBox


class GeneticMapController:
    ui = None

    @staticmethod
    def load_file(path):
        GeneticMapController.ui.alaa_plainTextEdit.setPlainText(open(path).read())

    @staticmethod
    def save_file():
        with open('new_genetic_map.txt', 'w') as file:
            file.write(str(GeneticMapController.ui.alaa_plainTextEdit.toPlainText()))
        QMessageBox().information(GeneticMapController.ui, "Done", "Alleles has been saved successfully!!")
