from PySide6.QtWidgets import QMainWindow
from interface.gestionPoste import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from PySide6.QtGui import QIcon

class GestionPosteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Gestion des Postes 😎😎")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion des boutons
        self.ui.modif.clicked.connect(self.handle_modify)
        self.ui.ajout.clicked.connect(self.handle_add)
        self.ui.retour.clicked.connect(self.back_role)

    def handle_add(self):
        print("poste en cours d'ajout")

    def handle_modify(self):
        # Ici tu mets ta logique de soumission de demande de poste
        print("poste en cours de modifié")

    def back_role(self):
        from views.admMode import AdminModeWindow
        self.adm = AdminModeWindow()
        print("Retour au menu admin")
        self.adm.show()
        self.close()