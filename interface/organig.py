# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'organigramme.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(642, 430)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backG = QFrame(self.centralwidget)
        self.backG.setObjectName(u"backG")
        self.backG.setGeometry(QRect(10, 10, 621, 361))
        self.backG.setFrameShape(QFrame.StyledPanel)
        self.backG.setFrameShadow(QFrame.Raised)
        self.organigrame = QTableWidget(self.backG)
        if (self.organigrame.columnCount() < 6):
            self.organigrame.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.organigrame.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.organigrame.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.organigrame.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.organigrame.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.organigrame.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.organigrame.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.organigrame.setObjectName(u"organigrame")
        self.organigrame.setGeometry(QRect(10, 10, 601, 281))
        self.retour = QPushButton(self.backG)
        self.retour.setObjectName(u"retour")
        self.retour.setGeometry(QRect(100, 310, 381, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 642, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.organigrame.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id_user", None));
        ___qtablewidgetitem1 = self.organigrame.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.organigrame.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Post_nom", None));
        ___qtablewidgetitem3 = self.organigrame.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Pre_nom", None));
        ___qtablewidgetitem4 = self.organigrame.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Poste", None));
        ___qtablewidgetitem5 = self.organigrame.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"id_Sup\u00e9rieur", None));
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
