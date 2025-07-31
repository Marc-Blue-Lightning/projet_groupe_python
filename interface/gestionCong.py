# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestionConger.ui'
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
        MainWindow.resize(659, 411)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backG = QFrame(self.centralwidget)
        self.backG.setObjectName(u"backG")
        self.backG.setGeometry(QRect(10, 10, 631, 341))
        self.backG.setFrameShape(QFrame.StyledPanel)
        self.backG.setFrameShadow(QFrame.Raised)
        self.congerTab = QTableWidget(self.backG)
        if (self.congerTab.columnCount() < 4):
            self.congerTab.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.congerTab.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.congerTab.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.congerTab.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.congerTab.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.congerTab.setObjectName(u"congerTab")
        self.congerTab.setGeometry(QRect(10, 10, 401, 281))
        self.conger = QFrame(self.backG)
        self.conger.setObjectName(u"conger")
        self.conger.setGeometry(QRect(430, 10, 181, 231))
        self.conger.setFrameShape(QFrame.StyledPanel)
        self.conger.setFrameShadow(QFrame.Raised)
        self.accepter = QPushButton(self.conger)
        self.accepter.setObjectName(u"accepter")
        self.accepter.setGeometry(QRect(100, 190, 75, 23))
        self.rejetter = QPushButton(self.conger)
        self.rejetter.setObjectName(u"rejetter")
        self.rejetter.setGeometry(QRect(10, 190, 75, 23))
        self.recher = QPushButton(self.conger)
        self.recher.setObjectName(u"recher")
        self.recher.setGeometry(QRect(44, 40, 101, 23))
        self.idCLine = QLineEdit(self.conger)
        self.idCLine.setObjectName(u"idCLine")
        self.idCLine.setGeometry(QRect(50, 10, 113, 20))
        self.idC = QLabel(self.conger)
        self.idC.setObjectName(u"idC")
        self.idC.setGeometry(QRect(10, 10, 31, 21))
        self.idULine = QLineEdit(self.conger)
        self.idULine.setObjectName(u"idULine")
        self.idULine.setGeometry(QRect(70, 90, 91, 20))
        self.lineEdit_dateD = QLineEdit(self.conger)
        self.lineEdit_dateD.setObjectName(u"lineEdit_dateD")
        self.lineEdit_dateD.setGeometry(QRect(70, 120, 91, 20))
        self.lineEdit_dateF = QLineEdit(self.conger)
        self.lineEdit_dateF.setObjectName(u"lineEdit_dateF")
        self.lineEdit_dateF.setGeometry(QRect(70, 150, 91, 20))
        self.idU = QLabel(self.conger)
        self.idU.setObjectName(u"idU")
        self.idU.setGeometry(QRect(10, 90, 47, 21))
        self.datF = QLabel(self.conger)
        self.datF.setObjectName(u"datF")
        self.datF.setGeometry(QRect(10, 150, 47, 21))
        self.dateD = QLabel(self.conger)
        self.dateD.setObjectName(u"dateD")
        self.dateD.setGeometry(QRect(10, 120, 61, 21))
        self.retour = QPushButton(self.backG)
        self.retour.setObjectName(u"retour")
        self.retour.setGeometry(QRect(250, 310, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 659, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.congerTab.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id conger", None));
        ___qtablewidgetitem1 = self.congerTab.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Id User", None));
        ___qtablewidgetitem2 = self.congerTab.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date debut", None));
        ___qtablewidgetitem3 = self.congerTab.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date fin", None));
        self.accepter.setText(QCoreApplication.translate("MainWindow", u"Accepter", None))
        self.rejetter.setText(QCoreApplication.translate("MainWindow", u"Rejetter", None))
        self.recher.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.idC.setText(QCoreApplication.translate("MainWindow", u"ID C", None))
        self.idU.setText(QCoreApplication.translate("MainWindow", u"ID User", None))
        self.datF.setText(QCoreApplication.translate("MainWindow", u"Date fin", None))
        self.dateD.setText(QCoreApplication.translate("MainWindow", u"Date debut", None))
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
