# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'identification.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(397, 503)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backG = QFrame(self.centralwidget)
        self.backG.setObjectName(u"backG")
        self.backG.setGeometry(QRect(10, 0, 371, 461))
        self.backG.setFrameShape(QFrame.StyledPanel)
        self.backG.setFrameShadow(QFrame.Raised)
        self.titre = QFrame(self.backG)
        self.titre.setObjectName(u"titre")
        self.titre.setGeometry(QRect(29, 20, 311, 51))
        self.titre.setFrameShape(QFrame.StyledPanel)
        self.titre.setFrameShadow(QFrame.Raised)
        self.ident = QLabel(self.titre)
        self.ident.setObjectName(u"ident")
        self.ident.setGeometry(QRect(16, 12, 281, 31))
        self.user = QFrame(self.backG)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(30, 90, 311, 291))
        self.user.setFrameShape(QFrame.StyledPanel)
        self.user.setFrameShadow(QFrame.Raised)
        self.nom_line = QLineEdit(self.user)
        self.nom_line.setObjectName(u"nom_line")
        self.nom_line.setGeometry(QRect(120, 20, 171, 20))
        self.postN_line = QLineEdit(self.user)
        self.postN_line.setObjectName(u"postN_line")
        self.postN_line.setGeometry(QRect(120, 50, 171, 20))
        self.preN_line = QLineEdit(self.user)
        self.preN_line.setObjectName(u"preN_line")
        self.preN_line.setGeometry(QRect(120, 80, 171, 20))
        self.eMail_line = QLineEdit(self.user)
        self.eMail_line.setObjectName(u"eMail_line")
        self.eMail_line.setGeometry(QRect(120, 110, 171, 20))
        self.poste = QComboBox(self.user)
        self.poste.setObjectName(u"poste")
        self.poste.setGeometry(QRect(120, 140, 171, 22))
        self.comboBox_2 = QComboBox(self.user)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(120, 180, 171, 22))
        self.actif = QCheckBox(self.user)
        self.actif.setObjectName(u"actif")
        self.actif.setGeometry(QRect(120, 230, 70, 17))
        self.nom = QLabel(self.user)
        self.nom.setObjectName(u"nom")
        self.nom.setGeometry(QRect(20, 20, 81, 16))
        self.postN = QLabel(self.user)
        self.postN.setObjectName(u"postN")
        self.postN.setGeometry(QRect(20, 50, 81, 16))
        self.preN = QLabel(self.user)
        self.preN.setObjectName(u"preN")
        self.preN.setGeometry(QRect(20, 80, 81, 16))
        self.eMail = QLabel(self.user)
        self.eMail.setObjectName(u"eMail")
        self.eMail.setGeometry(QRect(20, 110, 81, 16))
        self.poste_label = QLabel(self.user)
        self.poste_label.setObjectName(u"poste_label")
        self.poste_label.setGeometry(QRect(20, 140, 81, 16))
        self.role = QLabel(self.user)
        self.role.setObjectName(u"role")
        self.role.setGeometry(QRect(20, 180, 81, 16))
        self.confirmer = QPushButton(self.backG)
        self.confirmer.setObjectName(u"confirmer")
        self.confirmer.setGeometry(QRect(270, 410, 75, 23))
        self.Annuler = QPushButton(self.backG)
        self.Annuler.setObjectName(u"Annuler")
        self.Annuler.setGeometry(QRect(150, 410, 75, 23))
        self.boutton = QPushButton(self.backG)
        self.boutton.setObjectName(u"boutton")
        self.boutton.setGeometry(QRect(30, 410, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 397, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ident.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">identification de l'utilisateur</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\"><br/></span></p></body></html>", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"employe", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"manager", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"admin", None))

        self.actif.setText(QCoreApplication.translate("MainWindow", u"Actif", None))
        self.nom.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.postN.setText(QCoreApplication.translate("MainWindow", u"Post Nom :", None))
        self.preN.setText(QCoreApplication.translate("MainWindow", u"Prenom :", None))
        self.eMail.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
        self.poste_label.setText(QCoreApplication.translate("MainWindow", u"Poste :", None))
        self.role.setText(QCoreApplication.translate("MainWindow", u"Role :", None))
        self.confirmer.setText(QCoreApplication.translate("MainWindow", u"confirmer", None))
        self.Annuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.boutton.setText(QCoreApplication.translate("MainWindow", u"humm...", None))
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
