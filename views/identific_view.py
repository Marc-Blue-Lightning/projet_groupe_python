from PySide6.QtWidgets import QMainWindow
from interface.identific import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from PySide6.QtGui import QIcon

class IdentificationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Identification de l'utilisateur 😎😎")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion des boutons
        self.ui.confirmer.clicked.connect(self.handle_confirm)
        self.ui.Annuler.clicked.connect(self.handle_cancel)

    def handle_confirm(self):
        print("Identification de l'utilisateur en confirmer")

    def handle_cancel(self):
        from views.gestionUser_view import GestionUserWindow
        self.gestion_user = GestionUserWindow()
        self.gestion_user.show()
        print("Connexion annulée")
        self.close()  # ferme la fenêtre d'identification