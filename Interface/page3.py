# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys
sys.path.append("../")
import XBWT.Main as Xbwt
from PyQt5 import QtCore, QtGui, QtWidgets
import ComparerFonctions as Comp

class Ui_Page3(object):
    def __init__(self, text, motifs, nbMotifs):
        self.text = text
        self.motiffs = motifs
        self.nbMotiffs = nbMotifs

    def afficher(self):
            self.res = Xbwt.methodeXbwt(self.motiffs, self.text)
            for elm in self.res:
                self.motifs.append(
                    "<span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">{}</span>".format(elm[0]))
                self.indice.append(
                    "<span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">{}</span>".format(elm[1]))
            self.motifs.setLineWrapMode(QtWidgets.QTextBrowser.NoWrap)
            self.motifs.horizontalScrollBar().setValue(0)
            self.indice.setLineWrapMode(QtWidgets.QTextBrowser.NoWrap)
            self.indice.horizontalScrollBar().setValue(0)
            self.nbMotifs.setText("{}".format(self.nbMotiffs))
            self.temps.setText("{}".format(Xbwt.temps))
            self.taille.setText("{}".format(Comp.getsize(Xbwt.ll) + Comp.getsize(Xbwt.chaineDesParentheses) + Comp.getsize(Xbwt.listeDesNoeuds)+Comp.getsize(Xbwt.f)))



    def setupUi(self, Page3):
        Page3.setObjectName("Page3")
        Page3.resize(628, 497)
        self.centralwidget = QtWidgets.QWidget(Page3)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 10, 181, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(220, 10, 81, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.motifs = QtWidgets.QTextBrowser(self.centralwidget)
        self.motifs.setGeometry(QtCore.QRect(40, 80, 181, 371))
        self.motifs.setObjectName("motifs")

        self.indice = QtWidgets.QTextBrowser(self.centralwidget)
        self.indice.setGeometry(QtCore.QRect(220, 80, 81, 371))
        self.indice.setObjectName("indice")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 190, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 310, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.temps = QtWidgets.QLabel(self.centralwidget)
        self.temps.setGeometry(QtCore.QRect(320, 240, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.temps.setFont(font)
        self.temps.setAutoFillBackground(True)
        self.temps.setText("")
        self.temps.setObjectName("temps")
        self.taille = QtWidgets.QLabel(self.centralwidget)
        self.taille.setGeometry(QtCore.QRect(320, 360, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.taille.setFont(font)
        self.taille.setAutoFillBackground(True)
        self.taille.setText("")
        self.taille.setObjectName("taille")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 80, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setObjectName("label_6")
        self.nbMotifs = QtWidgets.QLabel(self.centralwidget)
        self.nbMotifs.setGeometry(QtCore.QRect(320, 130, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nbMotifs.setFont(font)
        self.nbMotifs.setAutoFillBackground(True)
        self.nbMotifs.setText("")
        self.nbMotifs.setObjectName("nbMotifs")
        Page3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Page3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 21))
        self.menubar.setObjectName("menubar")
        Page3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Page3)
        self.statusbar.setObjectName("statusbar")
        Page3.setStatusBar(self.statusbar)

        self.retranslateUi(Page3)
        QtCore.QMetaObject.connectSlotsByName(Page3)

    def retranslateUi(self, Page3):
        _translate = QtCore.QCoreApplication.translate
        Page3.setWindowTitle(_translate("Page3", "MainWindow"))
        self.textBrowser.setHtml(_translate("Page3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">Motifs Recherchés</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Page3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">Indice</span></p></body></html>"))
        self.motifs.setHtml(_translate("Page3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.indice.setHtml(_translate("Page3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label.setText(_translate("Page3", "Temps d\'exécution :"))
        self.label_2.setText(_translate("Page3", "Taille de la XBWT :  "))
        self.label_5.setText(_translate("Page3", "Méthode XBWT"))
        self.label_6.setText(_translate("Page3", "Nombre de motifs :"))
        self.afficher()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Page3 = QtWidgets.QMainWindow()
    ui = Ui_Page3()
    ui.setupUi(Page3)
    Page3.show()
    sys.exit(app.exec_())
