from PySide6.QtWidgets import QMainWindow
from interface.gestionCong import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from PySide6.QtGui import QIcon

class GestionCongWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Gestion des Congés 😎😎")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion des boutons
        self.ui.accepter.clicked.connect(self.handle_request)
        self.ui.rejetter.clicked.connect(self.handle_cancel)
        self.ui.recher.clicked.connect(self.handle_search)
        self.ui.retour.clicked.connect(self.back_role)

    def handle_search(self):
        # Ici tu mets ta logique de recherche de demande de congé
        print("Recherche de demande de congé effectuée")

    def handle_cancel(self):

        print("Demande de congé rejetée")
        

    def handle_request(self):
        # Ici tu mets ta logique de soumission de demande de congé
        print("Demande de congé accepter")

    def back_role(self):
        from views.admMode import AdminModeWindow
        self.adm = AdminModeWindow()
        print("Demande de congé annulée")
        self.adm.show()
        self.close()