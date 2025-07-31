# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestionUser.ui'
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
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(729, 495)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backG = QFrame(self.centralwidget)
        self.backG.setObjectName(u"backG")
        self.backG.setGeometry(QRect(10, 10, 711, 431))
        self.backG.setFrameShape(QFrame.StyledPanel)
        self.backG.setFrameShadow(QFrame.Raised)
        self.frame_infoUser = QFrame(self.backG)
        self.frame_infoUser.setObjectName(u"frame_infoUser")
        self.frame_infoUser.setGeometry(QRect(470, 9, 231, 291))
        self.frame_infoUser.setFrameShape(QFrame.StyledPanel)
        self.frame_infoUser.setFrameShadow(QFrame.Raised)
        self.id_label = QLabel(self.frame_infoUser)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(20, 20, 47, 13))
        self.idUser = QLineEdit(self.frame_infoUser)
        self.idUser.setObjectName(u"idUser")
        self.idUser.setGeometry(QRect(80, 20, 131, 20))
        self.recherche = QPushButton(self.frame_infoUser)
        self.recherche.setObjectName(u"recherche")
        self.recherche.setGeometry(QRect(110, 50, 75, 23))
        self.label_nom = QLabel(self.frame_infoUser)
        self.label_nom.setObjectName(u"label_nom")
        self.label_nom.setGeometry(QRect(20, 90, 47, 13))
        self.label_postN = QLabel(self.frame_infoUser)
        self.label_postN.setObjectName(u"label_postN")
        self.label_postN.setGeometry(QRect(20, 120, 61, 16))
        self.lineEdit_nom = QLineEdit(self.frame_infoUser)
        self.lineEdit_nom.setObjectName(u"lineEdit_nom")
        self.lineEdit_nom.setGeometry(QRect(90, 90, 113, 20))
        self.lineEdit_PostN = QLineEdit(self.frame_infoUser)
        self.lineEdit_PostN.setObjectName(u"lineEdit_PostN")
        self.lineEdit_PostN.setGeometry(QRect(90, 120, 113, 20))
        self.lineEdit_PreN = QLineEdit(self.frame_infoUser)
        self.lineEdit_PreN.setObjectName(u"lineEdit_PreN")
        self.lineEdit_PreN.setGeometry(QRect(90, 150, 113, 20))
        self.lineEdit_Email = QLineEdit(self.frame_infoUser)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setGeometry(QRect(90, 180, 113, 20))
        self.lineEdit_poste = QLineEdit(self.frame_infoUser)
        self.lineEdit_poste.setObjectName(u"lineEdit_poste")
        self.lineEdit_poste.setGeometry(QRect(90, 210, 113, 20))
        self.lineEdit_role = QLineEdit(self.frame_infoUser)
        self.lineEdit_role.setObjectName(u"lineEdit_role")
        self.lineEdit_role.setGeometry(QRect(90, 240, 113, 20))
        self.label_preN = QLabel(self.frame_infoUser)
        self.label_preN.setObjectName(u"label_preN")
        self.label_preN.setGeometry(QRect(20, 150, 47, 13))
        self.label_Email = QLabel(self.frame_infoUser)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(20, 180, 47, 13))
        self.label_poste = QLabel(self.frame_infoUser)
        self.label_poste.setObjectName(u"label_poste")
        self.label_poste.setGeometry(QRect(20, 210, 47, 13))
        self.label_role = QLabel(self.frame_infoUser)
        self.label_role.setObjectName(u"label_role")
        self.label_role.setGeometry(QRect(20, 240, 47, 13))
        self.tableWidget = QTableWidget(self.backG)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 441, 361))
        self.message = QLabel(self.backG)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(470, 310, 231, 61))
        self.modifUser = QPushButton(self.backG)
        self.modifUser.setObjectName(u"modifUser")
        self.modifUser.setGeometry(QRect(610, 390, 75, 23))
        self.addUser = QPushButton(self.backG)
        self.addUser.setObjectName(u"addUser")
        self.addUser.setGeometry(QRect(370, 390, 75, 23))
        self.cancel = QPushButton(self.backG)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(40, 390, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 729, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"Id User :", None))
        self.recherche.setText(QCoreApplication.translate("MainWindow", u"rechercher", None))
        self.label_nom.setText(QCoreApplication.translate("MainWindow", u"nom :", None))
        self.label_postN.setText(QCoreApplication.translate("MainWindow", u"Post Nom :", None))
        self.label_preN.setText(QCoreApplication.translate("MainWindow", u"Prenom :", None))
        self.label_Email.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
        self.label_poste.setText(QCoreApplication.translate("MainWindow", u"Post :", None))
        self.label_role.setText(QCoreApplication.translate("MainWindow", u"R\u00f4le :", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id User", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Post Nom", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Prenom", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"R\u00f4le", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Poste", None));
        self.message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.modifUser.setText(QCoreApplication.translate("MainWindow", u"Modif User", None))
        self.addUser.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
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
