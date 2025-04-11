from PyQt6.QtWidgets import QDialog
from PyQt6.uic import load_ui
from PyQt6.QtWidgets import QDialogButtonBox

class History (QDialog):
    def __init__(self, history, mainWindow):
        QDialog.__init__(self)
        self.ui = load_ui.loadUi(f"historique.ui", self)
        self.mainWin = mainWindow
        self.history = []
        for item in history:
            self.history.append("Calcul : " + item[0] + " | Resultat : " + item[1])
        self.historique.addItems(self.history)
        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.recupererCalcul)
        self.show()

    def recupererCalcul(self):
        self.mainWin.afficherCalculRecuperer(self.historique.selectedItems())