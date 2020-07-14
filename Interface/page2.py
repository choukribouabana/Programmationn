# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from random import randint, choice
from PyQt5 import QtCore, QtGui, QtWidgets
import page3
import page4

class Ui_Page2(object):

    def split(self):
        return [self.text[x:x + self.longMotif] for x in range(0, len(self.text), self.longMotif)]

    def importerTexte (self):
        with open("..\SARS-COV-2.txt", "r") as f:
            self.text = f.read()
            self.lineEdit.setText("SARS-COV-2.txt")
    def importerMotifs (self):
        self.motifs = list()
        self.nbMotifs = 4
        for j in range(self.nbMotifs):
             self.longMotif = randint(5, 10)
             motif = choice(self.split())
             self.motifs.append(motif)
        motifs = list(set(self.motifs))
        self.lineEdit_2.setText(";".join(motifs))

    def saisirMotifs(self):
        self.motifs = self.lineEdit_3.text().upper()
        if len(self.motifs) == 0:
            self.nbMotifs = 0
        elif len(self.motifs) == 1 :
            self.nbMotifs = 0
        else :
            self.motifs = self.motifs.split(";")
            self.nbMotifs = len(self.motifs)
            if self.motifs[-1] == "":
                self.nbMotifs -= 1
                self.motifs.pop()

    def openWindXbwt (self):
        if self.nbMotifs != 0:
            self.window = QtWidgets.QMainWindow()
            self.ui = page3.Ui_Page3(self.text, self.motifs, self.nbMotifs)
            self.ui.setupUi(self.window)
            self.window.show()

    def openWindTrie (self):
        if self.nbMotifs != 0:
            self.fenetre = QtWidgets.QMainWindow()
            self.uii = page4.Ui_Page4(self.text, self.motifs, self.nbMotifs)
            self.uii.setupUi(self.fenetre)
            self.fenetre.show()

    def setupUi(self, Page2):
        Page2.setObjectName("Page2")
        Page2.resize(628, 497)
        Page2.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Page2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 380, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 380, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("texte")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("Motifs")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 260, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("motifsInseres")
        #------------PushButtons---------------
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("importerTexte")
        self.pushButton_3.clicked.connect(self.importerTexte)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("importerMotifs")
        self.pushButton_4.clicked.connect(self.importerMotifs)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("saisirMotifs")
        self.pushButton_5.clicked.connect(self.saisirMotifs)

        Page2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Page2)
        self.statusbar.setObjectName("statusbar")
        Page2.setStatusBar(self.statusbar)

        self.retranslateUi(Page2)
        QtCore.QMetaObject.connectSlotsByName(Page2)

    def retranslateUi(self, Page2):
        _translate = QtCore.QCoreApplication.translate
        Page2.setWindowTitle(_translate("Page2", "MainWindow"))
        self.pushButton.setText(_translate("Page2", "Aho-Corasick"))
        self.pushButton.clicked.connect(self.openWindTrie)

        self.pushButton_2.setText(_translate("Page2", "XBWT"))
        self.pushButton_2.clicked.connect(self.openWindXbwt)

        self.label.setText(_translate("Page2", "Exécuter avec :"))
        self.label_2.setText(_translate("Page2", "Nom du fichier ADN : "))
        self.label_3.setText(_translate("Page2", "Les motifs importés :"))
        self.label_4.setText(_translate("Page2", "Saisir les motifs séparés par \";\" :"))
        self.pushButton_3.setText(_translate("Page2", "Importer texte"))
        self.pushButton_4.setText(_translate("Page2", "Importer motifs"))
        self.pushButton_5.setText(_translate("Page2", "Saisir motifs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Page2 = QtWidgets.QMainWindow()
    ui = Ui_Page2()
    ui.setupUi(Page2)
    Page2.show()
    sys.exit(app.exec_())


