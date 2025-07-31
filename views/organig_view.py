from PySide6.QtWidgets import QMainWindow
from interface.organig import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from PySide6.QtGui import QIcon

class OrganigrammeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Organigramme de l'organisation 😎😋")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retour.clicked.connect(self.back_dashboard)
    def back_dashboard(self):
        from views.dashboard_view import DashboardWindow
        self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.close()