from PySide6.QtWidgets import QMainWindow
from interface.identifPoste import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from PySide6.QtGui import QIcon

class IdentifPosteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Identification de l'utilisateur 😎😎")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion des boutons
        self.ui.confirmer.clicked.connect(self.handle_confirm)
        self.ui.retour.clicked.connect(self.handle_cancel)
        self.ui.retour.setToolTip("Retour au menu précédent")
        self.ui.easterEgg.setToolTip("C'est un easter egg !🚗🚓🚕")

    def handle_confirm(self):
        print("Identification du nouveau poste confirmer")
        # Logique pour confirmer l'identification, par exemple, vérifier les informations saisies

    def handle_cancel(self):
        from views.gestionPoste_view import GestionPosteWindow
        self.gestion_poste = GestionPosteWindow()
        self.gestion_poste.show()
        print("Identification annulée, retour à la gestion des postes")
        self.close()