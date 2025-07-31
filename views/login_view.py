from PySide6.QtWidgets import QMainWindow
from interface.login import Ui_MainWindow  # fichier compilé depuis login.ui
from views.dashboard_view import DashboardWindow  # Import de la fenêtre du dashboard
from controllers.auth_controller import login_utilisateur
from PySide6.QtGui import QIcon
from controllers.user_controleur import user # Import du gestionnaire de base de données

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("bonjour 😁😀😁")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connexion du bouton
        self.ui.boutonConnect.clicked.connect(self.handle_login)
        #self.ui.toolButton_aide.clicked.connect()
        self.ui.toolButton_aide.setToolTip("en cliquant sur ce bouton, vous aurez la possibilité de crée des utilisateur par défaut pour plus d'information sur leur id voir le manuelle")

    def handle_login(self,):
        # Récupération des informations de connexion
        self.email = self.ui.lineEdit_email.text()
        self.password = self.ui.lineEdit_passW.text()
        self.login = login_utilisateur(self.email, self.password)
        if self.login:
            # Ici tu mets ta logique d'authentification
            print("Connexion réussie !")
            self.dashboard = DashboardWindow()
            print("Connexion réussie dans le dashboard"+ str(self.login))
            self.dashboard.set_login_info(self.login)
            self.dashboard.show()
            self.close()  # ferme la fenêtre de login
              # Affiche les informations de l'utilisateur connecté
        else:
            print("Echec de la connexion")
    
    def addDefaultUsers(self):
        # Logique pour ajouter des utilisateurs par défaut pass
        #(nom, post_nom, prenom, email, mot_de_passe, poste_id, manager_id, roles)
        user.ajouter_utilisateur("Marc", "Mister", "Lightnin", "lightningMarc@gmail.com", "123456", 1, 1, "admin")
