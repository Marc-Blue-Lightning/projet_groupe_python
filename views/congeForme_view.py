from PySide6.QtWidgets import QMainWindow
from interface.congeForme import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from PySide6.QtGui import QIcon

class CongeFormeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Demande de Congé 😎😎")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion des boutons
        self.ui.envoyer.clicked.connect(self.handle_request)
        self.ui.Retour.clicked.connect(self.handle_cancel)

    def handle_request(self):
        # Ici tu mets ta logique de soumission de demande de congé
        from views.dashboard_view import DashboardWindow
        self.dashboard = DashboardWindow()
        print("Demande de congé soumise")
        self.dashboard.show()
        self.close()  # ferme la fenêtre de demande de congé

        

    def handle_cancel(self):
        from views.demande_view import DemandeConge
        self.dashboard = DemandeConge()
        print("Demande de congé annulée")
        self.dashboard.show()
        self.close()
