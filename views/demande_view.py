
from PySide6.QtWidgets import QMainWindow
from interface.demande import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from views.congeForme_view import CongeFormeWindow
from PySide6.QtGui import QIcon

class DemandeConge(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Demande de Congé 😎😎")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion des boutons
        self.ui.demande.clicked.connect(self.handle_request)
        self.ui.retour.clicked.connect(self.handle_cancel)

    def handle_request(self):
        
        print("Demande de congé soumise")
        self.dashboard = CongeFormeWindow()
        self.dashboard.show()
        self.close()

    def handle_cancel(self):
        from views.dashboard_view import DashboardWindow
        print("Demande de congé annulée")
        self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.close()