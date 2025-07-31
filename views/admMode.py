
from PySide6.QtWidgets import QMainWindow
from interface.admMode import Ui_MainWindow  # fichier compilé depuis dashboard.ui
from PySide6.QtGui import QIcon

class AdminModeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("Mode Administrateur 😑😑😎😎")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion des boutons
        self.ui.pushButton.clicked.connect(self.handle_user)
        self.ui.pushButton_2.clicked.connect(self.handle_conger)
        self.ui.pushButton_3.clicked.connect(self.handle_poste)
        self.ui.retour.clicked.connect(self.back_role)

    def back_role(self):
        from views.dashboard_view import DashboardWindow
        print("Retour au mode utilisateur")
        self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.close()


    def handle_user(self):
        from views.gestionUser_view import GestionUserWindow
        self.gestion_user = GestionUserWindow()
        self.gestion_user.show()
        self.close()  # ferme la fenêtre d'administration
        print("gestion des utilisateurs")


    def handle_poste(self):
        from views.gestionPoste_view import GestionPosteWindow
        self.gestion_poste = GestionPosteWindow()
        self.gestion_poste.show()
        self.close()  # ferme la fenêtre d'administration
        print("gestion des postes")


    def handle_conger(self):
        from views.gestionCong_view import GestionCongWindow
        self.gestion_conge = GestionCongWindow()
        self.gestion_conge.show()
        self.close()  # ferme la fenêtre d'administration
        print("gestion des congés")
