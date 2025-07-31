# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestionPoste.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(682, 459)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backG = QFrame(self.centralwidget)
        self.backG.setObjectName(u"backG")
        self.backG.setGeometry(QRect(10, 10, 661, 391))
        self.backG.setFrameShape(QFrame.StyledPanel)
        self.backG.setFrameShadow(QFrame.Raised)
        self.poste_tab = QTableWidget(self.backG)
        if (self.poste_tab.columnCount() < 4):
            self.poste_tab.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.poste_tab.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.poste_tab.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.poste_tab.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.poste_tab.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.poste_tab.setObjectName(u"poste_tab")
        self.poste_tab.setGeometry(QRect(10, 10, 401, 291))
        self.poste_frame = QFrame(self.backG)
        self.poste_frame.setObjectName(u"poste_frame")
        self.poste_frame.setGeometry(QRect(440, 10, 211, 291))
        self.poste_frame.setFrameShape(QFrame.StyledPanel)
        self.poste_frame.setFrameShadow(QFrame.Raised)
        self.lineEditId = QLineEdit(self.poste_frame)
        self.lineEditId.setObjectName(u"lineEditId")
        self.lineEditId.setGeometry(QRect(80, 20, 113, 20))
        self.lineEdit_Poste = QLineEdit(self.poste_frame)
        self.lineEdit_Poste.setObjectName(u"lineEdit_Poste")
        self.lineEdit_Poste.setGeometry(QRect(80, 90, 113, 20))
        self.textEditDescript = QTextEdit(self.poste_frame)
        self.textEditDescript.setObjectName(u"textEditDescript")
        self.textEditDescript.setGeometry(QRect(20, 160, 171, 91))
        self.descrip = QLabel(self.poste_frame)
        self.descrip.setObjectName(u"descrip")
        self.descrip.setGeometry(QRect(20, 130, 171, 20))
        self.idPoste = QLabel(self.poste_frame)
        self.idPoste.setObjectName(u"idPoste")
        self.idPoste.setGeometry(QRect(20, 20, 47, 21))
        self.nomPoste = QLabel(self.poste_frame)
        self.nomPoste.setObjectName(u"nomPoste")
        self.nomPoste.setGeometry(QRect(20, 90, 61, 21))
        self.modif = QPushButton(self.backG)
        self.modif.setObjectName(u"modif")
        self.modif.setGeometry(QRect(550, 330, 75, 23))
        self.ajout = QPushButton(self.backG)
        self.ajout.setObjectName(u"ajout")
        self.ajout.setGeometry(QRect(420, 330, 75, 23))
        self.retour = QPushButton(self.backG)
        self.retour.setObjectName(u"retour")
        self.retour.setGeometry(QRect(290, 330, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 682, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.poste_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id Poste", None));
        ___qtablewidgetitem1 = self.poste_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.poste_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem3 = self.poste_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nombre d'\u00e9l\u00e9ment", None));
        self.descrip.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Description</span></p></body></html>", None))
        self.idPoste.setText(QCoreApplication.translate("MainWindow", u"id poste", None))
        self.nomPoste.setText(QCoreApplication.translate("MainWindow", u"nom poste", None))
        self.modif.setText(QCoreApplication.translate("MainWindow", u"modiffier", None))
        self.ajout.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.retour.setText(QCoreApplication.translate("MainWindow", u"retour", None))
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
