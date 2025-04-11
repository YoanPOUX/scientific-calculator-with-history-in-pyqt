from PyQt6.uic import load_ui
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from historique import History
from math import sqrt

class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()

        self.sqrt = False
        self.result_showing = False
        self.calcul = ""
        self.res = ""
        self.history = []

        self.ui = load_ui.loadUi(f"calcScientv3.ui", self)
        self.btnHistory.setIcon(QIcon("history_icon.png"))
        self.btnHistory.setIconSize(QSize(60,60))
        
        # Connect buttons to their actions
        self.btn0.clicked.connect(lambda: self.addToQline("0"))
        self.btn1.clicked.connect(lambda: self.addToQline("1"))
        self.btn2.clicked.connect(lambda: self.addToQline("2"))
        self.btn3.clicked.connect(lambda: self.addToQline("3"))
        self.btn4.clicked.connect(lambda: self.addToQline("4"))
        self.btn5.clicked.connect(lambda: self.addToQline("5"))
        self.btn6.clicked.connect(lambda: self.addToQline("6"))
        self.btn7.clicked.connect(lambda: self.addToQline("7"))
        self.btn8.clicked.connect(lambda: self.addToQline("8"))
        self.btn9.clicked.connect(lambda: self.addToQline("9"))
        self.btnCarre.clicked.connect(lambda: self.addToQline("²"))
        self.btnDiv.clicked.connect(lambda: self.addToQline("÷"))
        self.btnEgal.clicked.connect(lambda: self.addToQline("="))
        self.btnFois.clicked.connect(lambda: self.addToQline("X"))
        self.btnMoins.clicked.connect(lambda: self.addToQline("-"))
        self.btnParFermante.clicked.connect(lambda: self.addToQline(")"))
        self.btnParOuvrante.clicked.connect(lambda: self.addToQline("("))
        self.btnPlus.clicked.connect(lambda: self.addToQline("+"))
        self.btnRacine.clicked.connect(lambda: self.addToQline("√"))
        self.btnVirgule.clicked.connect(lambda: self.addToQline(","))

        self.btnHistory.clicked.connect(lambda : self.showHistory())

        self.show()

    def calculer(self):
        try:
            self.calcul = self.calcul.replace("X", "*").replace("÷", "/").replace(",", ".").replace("√", "sqrt").replace("²", "**2")

            self.res = str(eval(self.calcul))
        except Exception as e:
            print(f"Error in calculation: {e}")
            self.res = "Erreur"
        self.history.append([self.calcul, self.res])

    def addToQline(self, lbl):
        if lbl=="√":
            if self.result_showing:
                self.result_showing = False
                self.calcul+= "√("
                self.lineEdit.setText(self.calcul)
                self.sqrt = True
            else:
                self.calcul += "√("
                self.lineEdit.setText(self.calcul)
                self.sqrt = True

        elif lbl == "=":
            if self.sqrt:
                self.calcul += ")"
                self.sqrt = False

            self.calculer()
            if self.res != "Erreur":
                if '.' in self.res:
                    self.res = str(round(float(self.res), 2))
                    if float(self.res).is_integer():
                        self.res = str(int(float(self.res)))
                else:
                    self.res = str(int(self.res))
            self.lineEdit.setText(self.res)
            self.calcul = "" 
            self.result_showing = True

        else:
            if self.result_showing:
                if self.res != "Erreur" :
                    if lbl in ["+", "-","X", "÷"]:
                        self.result_showing = False
                        self.calcul = str(self.res + lbl)
                        self.lineEdit.setText(self.calcul)
                    else :
                        self.result_showing = False
                        self.calcul = str(lbl)
                        self.lineEdit.setText(self.calcul) 
                else :
                    self.result_showing = False
                    self.calcul = str(lbl)
                    self.lineEdit.setText(self.calcul)
            else:
                if self.sqrt:
                    self.calcul += lbl + ")"
                    self.sqrt = False
                else :
                    self.calcul += lbl
                self.lineEdit.setText(self.calcul)

    def showHistory(self):
        self.historyWindow = History(self.history, self)

    def afficherCalculRecuperer(self, calculRecup):
        calcul = calculRecup[0].text()[9:]
        index = 0
        for i in range (len(calcul)):
            if calcul[i] == "|":
                index = i -1
        calcul = calcul[0:index]
        self.lineEdit.setText(calcul)
        self.res = calcul
        self.calcul = calcul
        self.result_showing = True

calc = QApplication([])
window = Main_Window()
calc.exec()