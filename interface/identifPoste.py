# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'identifPoste.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(359, 419)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backG = QFrame(self.centralwidget)
        self.backG.setObjectName(u"backG")
        self.backG.setGeometry(QRect(9, 9, 341, 361))
        self.backG.setFrameShape(QFrame.StyledPanel)
        self.backG.setFrameShadow(QFrame.Raised)
        self.titre = QFrame(self.backG)
        self.titre.setObjectName(u"titre")
        self.titre.setGeometry(QRect(29, 10, 281, 51))
        self.titre.setFrameShape(QFrame.StyledPanel)
        self.titre.setFrameShadow(QFrame.Raised)
        self.poste = QLabel(self.titre)
        self.poste.setObjectName(u"poste")
        self.poste.setGeometry(QRect(20, 13, 241, 20))
        self.framePoste = QFrame(self.backG)
        self.framePoste.setObjectName(u"framePoste")
        self.framePoste.setGeometry(QRect(30, 70, 281, 211))
        self.framePoste.setFrameShape(QFrame.StyledPanel)
        self.framePoste.setFrameShadow(QFrame.Raised)
        self.lineEditPoste = QLineEdit(self.framePoste)
        self.lineEditPoste.setObjectName(u"lineEditPoste")
        self.lineEditPoste.setGeometry(QRect(132, 20, 131, 20))
        self.textEditDescript = QTextEdit(self.framePoste)
        self.textEditDescript.setObjectName(u"textEditDescript")
        self.textEditDescript.setGeometry(QRect(23, 90, 241, 71))
        self.label_Nom = QLabel(self.framePoste)
        self.label_Nom.setObjectName(u"label_Nom")
        self.label_Nom.setGeometry(QRect(20, 20, 101, 21))
        self.label_Description = QLabel(self.framePoste)
        self.label_Description.setObjectName(u"label_Description")
        self.label_Description.setGeometry(QRect(46, 60, 191, 20))
        self.confi = QPushButton(self.backG)
        self.confi.setObjectName(u"confi")
        self.confi.setGeometry(QRect(240, 310, 75, 23))
        self.confi.setMouseTracking(False)
        self.confi.setAutoDefault(False)
        self.retour = QPushButton(self.backG)
        self.retour.setObjectName(u"retour")
        self.retour.setGeometry(QRect(130, 310, 75, 23))
        self.easterEgg = QPushButton(self.backG)
        self.easterEgg.setObjectName(u"easterEgg")
        self.easterEgg.setGeometry(QRect(30, 310, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 359, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.confi.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.poste.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Poste</span></p></body></html>", None))
        self.label_Nom.setText(QCoreApplication.translate("MainWindow", u"Nom Poste :", None))
        self.label_Description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Description</p></body></html>", None))
        self.confi.setText(QCoreApplication.translate("MainWindow", u"confirmer", None))
        self.retour.setText(QCoreApplication.translate("MainWindow", u"retour", None))
        self.easterEgg.setText(QCoreApplication.translate("MainWindow", u"hum...", None))
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
