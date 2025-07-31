from PySide6.QtWidgets import QMainWindow
from interface.gestionUser import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from PySide6.QtGui import QIcon

class GestionUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Gestion des Utilisateurs 😎😎")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion des boutons
        self.ui.modifUser.clicked.connect(self.handle_modify)
        self.ui.recherche.clicked.connect(self.handle_rech)
        self.ui.addUser.clicked.connect(self.handle_add)
        self.ui.cancel.clicked.connect(self.back_role)

    def handle_rech(self):
        print("Recherche d'utilisateur effectuée")
    def handle_add(self):
        print("ajout de l'utilisateur en cours")

    def handle_modify(self):
        # Ici tu mets ta logique de soumission de demande d'utilisateur
        print("modification d'utilisateur en cours")

    def back_role(self):
        from views.admMode import AdminModeWindow
        self.adm = AdminModeWindow()
        print("Retour au menu admin")
        self.adm.show()
        self.close()