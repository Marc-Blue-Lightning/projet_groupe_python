# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboar.ui'
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
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 432)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_backg = QFrame(self.centralwidget)
        self.frame_backg.setObjectName(u"frame_backg")
        self.frame_backg.setGeometry(QRect(9, 9, 811, 371))
        self.tabWidget = QTabWidget(self.frame_backg)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 561, 301))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.table_conge = QTableWidget(self.tab)
        if (self.table_conge.columnCount() < 5):
            self.table_conge.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_conge.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_conge.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_conge.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_conge.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_conge.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_conge.setObjectName(u"table_conge")
        self.table_conge.setGeometry(QRect(10, 10, 531, 251))
        self.table_conge.setColumnCount(5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.table_attente = QTableWidget(self.tab_2)
        if (self.table_attente.columnCount() < 5):
            self.table_attente.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_attente.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_attente.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_attente.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_attente.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_attente.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.table_attente.setObjectName(u"table_attente")
        self.table_attente.setGeometry(QRect(10, 10, 531, 251))
        self.table_attente.setColumnCount(5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.table_dispo = QTableWidget(self.tab_3)
        if (self.table_dispo.columnCount() < 5):
            self.table_dispo.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_dispo.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_dispo.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_dispo.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_dispo.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_dispo.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.table_dispo.setObjectName(u"table_dispo")
        self.table_dispo.setGeometry(QRect(10, 10, 531, 251))
        self.table_dispo.setColumnCount(5)
        self.tabWidget.addTab(self.tab_3, "")
        self.button_conger = QPushButton(self.frame_backg)
        self.button_conger.setObjectName(u"button_conger")
        self.button_conger.setGeometry(QRect(30, 332, 111, 31))
        self.button_orga = QPushButton(self.frame_backg)
        self.button_orga.setObjectName(u"button_orga")
        self.button_orga.setGeometry(QRect(310, 332, 111, 31))
        self.admin_mode = QPushButton(self.frame_backg)
        self.admin_mode.setObjectName(u"admin_mode")
        self.admin_mode.setGeometry(QRect(670, 332, 111, 31))
        self.frame_user = QFrame(self.frame_backg)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setGeometry(QRect(600, 10, 191, 191))
        self.frame_user.setFrameShape(QFrame.StyledPanel)
        self.frame_user.setFrameShadow(QFrame.Raised)

        self.bienv = QLabel(self.frame_user)
        self.bienv.setObjectName(u"bienv")
        self.bienv.setGeometry(QRect(56, 10, 71, 20))

        self.id_user_label = QLabel(self.frame_user)
        self.id_user_label.setObjectName(u"id_user_label")
        self.id_user_label.setGeometry(QRect(10, 50, 47, 13))

        self.label_nom = QLabel(self.frame_user)
        self.label_nom.setObjectName(u"label_nom")
        self.label_nom.setGeometry(QRect(10, 80, 47, 13))

        self.label_poste = QLabel(self.frame_user)
        self.label_poste.setObjectName(u"label_poste")
        self.label_poste.setGeometry(QRect(10, 110, 47, 13))

        self.label_role = QLabel(self.frame_user)
        self.label_role.setObjectName(u"label_role")
        self.label_role.setGeometry(QRect(10, 140, 47, 13))

        self.lineEdit_iduser = QLineEdit(self.frame_user)
        self.lineEdit_iduser.setObjectName(u"lineEdit_iduser")
        self.lineEdit_iduser.setGeometry(QRect(60, 50, 113, 20))

        self.lineEdit_nom = QLineEdit(self.frame_user)
        self.lineEdit_nom.setObjectName(u"lineEdit_nom")
        self.lineEdit_nom.setGeometry(QRect(60, 80, 113, 20))

        self.lineEdit_poste = QLineEdit(self.frame_user)
        self.lineEdit_poste.setObjectName(u"lineEdit_poste")
        self.lineEdit_poste.setGeometry(QRect(60, 110, 113, 20))

        self.lineEdit_role = QLineEdit(self.frame_user)
        self.lineEdit_role.setObjectName(u"lineEdit_role")
        self.lineEdit_role.setGeometry(QRect(60, 140, 113, 20))
        self.lineEdit_role.setToolTip("Role de l'utilisateur")


        self.label = QLabel(self.frame_backg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 230, 191, 81))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 832, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.table_conge.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID USER", None));
        ___qtablewidgetitem1 = self.table_conge.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.table_conge.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Poste", None));
        ___qtablewidgetitem3 = self.table_conge.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date de d\u00e9but", None));
        ___qtablewidgetitem4 = self.table_conge.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date de fin", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"En Cong\u00e9", None))
        ___qtablewidgetitem5 = self.table_attente.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID USER", None));
        ___qtablewidgetitem6 = self.table_attente.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem7 = self.table_attente.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Poste", None));
        ___qtablewidgetitem8 = self.table_attente.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date de d\u00e9but", None));
        ___qtablewidgetitem9 = self.table_attente.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Date de fin", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"En Attente", None))
        ___qtablewidgetitem10 = self.table_dispo.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID USER", None));
        ___qtablewidgetitem11 = self.table_dispo.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem12 = self.table_dispo.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Poste", None));
        ___qtablewidgetitem13 = self.table_dispo.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Date de d\u00e9but", None));
        ___qtablewidgetitem14 = self.table_dispo.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Date de fin", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Disponible", None))
        self.button_conger.setText(QCoreApplication.translate("MainWindow", u"Demande de Cong\u00e9", None))
        self.button_orga.setText(QCoreApplication.translate("MainWindow", u"organigramme", None))
        self.admin_mode.setText(QCoreApplication.translate("MainWindow", u"admin mode", None))
        self.bienv.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Bienvenu(e)</span></p></body></html>", None))
        self.id_user_label.setText(QCoreApplication.translate("MainWindow", u"ID User :", None))
        self.label_nom.setText(QCoreApplication.translate("MainWindow", u"Nom      :", None))
        self.label_poste.setText(QCoreApplication.translate("MainWindow", u"Poste    :", None))
        self.label_role.setText(QCoreApplication.translate("MainWindow", u"Role      :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Message iteractif", None))
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
