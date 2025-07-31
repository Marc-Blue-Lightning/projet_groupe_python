# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaireConger.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(276, 326)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backG = QFrame(self.centralwidget)
        self.backG.setObjectName(u"backG")
        self.backG.setGeometry(QRect(10, 10, 251, 261))
        self.backG.setFrameShape(QFrame.StyledPanel)
        self.backG.setFrameShadow(QFrame.Raised)
        self.dateEditDebut = QDateEdit(self.backG)
        self.dateEditDebut.setObjectName(u"dateEditDebut")
        self.dateEditDebut.setGeometry(QRect(120, 20, 110, 22))
        self.dateEdit_Fin = QDateEdit(self.backG)
        self.dateEdit_Fin.setObjectName(u"dateEdit_Fin")
        self.dateEdit_Fin.setGeometry(QRect(120, 50, 110, 22))
        self.textEditMotif = QTextEdit(self.backG)
        self.textEditMotif.setObjectName(u"textEditMotif")
        self.textEditMotif.setGeometry(QRect(20, 120, 211, 81))
        self.motif = QLabel(self.backG)
        self.motif.setObjectName(u"motif")
        self.motif.setGeometry(QRect(100, 90, 47, 13))
        self.dateDebut = QLabel(self.backG)
        self.dateDebut.setObjectName(u"dateDebut")
        self.dateDebut.setGeometry(QRect(20, 30, 81, 16))
        self.dateFin = QLabel(self.backG)
        self.dateFin.setObjectName(u"dateFin")
        self.dateFin.setGeometry(QRect(20, 55, 71, 21))
        self.envoyer = QPushButton(self.backG)
        self.envoyer.setObjectName(u"envoyer")
        self.envoyer.setGeometry(QRect(150, 220, 75, 23))
        self.Retour = QPushButton(self.backG)
        self.Retour.setObjectName(u"Retour")
        self.Retour.setGeometry(QRect(30, 220, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 276, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.motif.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Motif</span></p></body></html>", None))
        self.dateDebut.setText(QCoreApplication.translate("MainWindow", u"Date de debut", None))
        self.dateFin.setText(QCoreApplication.translate("MainWindow", u"Date de fin", None))
        self.envoyer.setText(QCoreApplication.translate("MainWindow", u"Envoyer", None))
        self.Retour.setText(QCoreApplication.translate("MainWindow", u"Retour", None))
    # retranslateUi

class MainApp(QMainWindow):
    def __init__(self) : 
        super().__init__()
        
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("bonjour 😁😀😁")
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
