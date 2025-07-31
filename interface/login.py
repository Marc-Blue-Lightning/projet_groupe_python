# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 412)
        self.actionfist_user_default = QAction(MainWindow)
        self.actionfist_user_default.setObjectName(u"actionfist_user_default")
        self.actioninitialisation = QAction(MainWindow)
        self.actioninitialisation.setObjectName(u"actioninitialisation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.BackG = QFrame(self.centralwidget)
        self.BackG.setObjectName(u"BackG")
        self.BackG.setGeometry(QRect(0, 0, 351, 381))
        self.frame_deco = QFrame(self.BackG)
        self.frame_deco.setObjectName(u"frame_deco")
        self.frame_deco.setGeometry(QRect(40, 10, 271, 51))
        self.frame_deco.setFrameShape(QFrame.StyledPanel)
        self.frame_deco.setFrameShadow(QFrame.Raised)
        self.connexion = QLabel(self.frame_deco)
        self.connexion.setObjectName(u"connexion")
        self.connexion.setGeometry(QRect(3, 2, 271, 51))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setBold(True)
        self.connexion.setFont(font)
        self.toolButton_aide = QToolButton(self.BackG)
        self.toolButton_aide.setObjectName(u"toolButton_aide")
        self.toolButton_aide.setGeometry(QRect(10, 340, 25, 19))
        self.editFrame = QFrame(self.BackG)
        self.editFrame.setObjectName(u"editFrame")
        self.editFrame.setGeometry(QRect(20, 70, 311, 251))
        self.editFrame.setFrameShape(QFrame.StyledPanel)
        self.editFrame.setFrameShadow(QFrame.Raised)
        self.label_email = QLabel(self.editFrame)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(30, 40, 47, 13))
        self.verticalFrame_edit = QFrame(self.editFrame)
        self.verticalFrame_edit.setObjectName(u"verticalFrame_edit")
        self.verticalFrame_edit.setGeometry(QRect(110, 10, 160, 171))
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame_edit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_email = QLineEdit(self.verticalFrame_edit)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.verticalLayout_3.addWidget(self.lineEdit_email)

        self.lineEdit_passW = QLineEdit(self.verticalFrame_edit)
        self.lineEdit_passW.setObjectName(u"lineEdit_passW")
        self.lineEdit_passW.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.lineEdit_passW)

        self.boutonConnect = QPushButton(self.verticalFrame_edit)
        self.boutonConnect.setObjectName(u"boutonConnect")

        self.verticalLayout_3.addWidget(self.boutonConnect)

        self.label_pw = QLabel(self.editFrame)
        self.label_pw.setObjectName(u"label_pw")
        self.label_pw.setGeometry(QRect(30, 90, 64, 13))
        self.message = QLabel(self.editFrame)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(20, 190, 271, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 21))
        self.menuaide = QMenu(self.menubar)
        self.menuaide.setObjectName(u"menuaide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuaide.menuAction())
        self.menuaide.addSeparator()
        self.menuaide.addAction(self.actioninitialisation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionfist_user_default.setText(QCoreApplication.translate("MainWindow", u"fist user default", None))
        self.actioninitialisation.setText(QCoreApplication.translate("MainWindow", u"initialisation", None))
        self.connexion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">CONNEXION</span></p></body></html>", None))
        self.toolButton_aide.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.boutonConnect.setText(QCoreApplication.translate("MainWindow", u"Se Connecter", None))
        self.label_pw.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.message.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.menuaide.setTitle(QCoreApplication.translate("MainWindow", u"aide", None))
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
