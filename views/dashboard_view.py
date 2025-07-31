from PySide6.QtWidgets import QMainWindow
from interface.dashboards import Ui_MainWindow, QPushButton
from views.admMode import AdminModeWindow  # Import de la fenêtre d'administration
from views.organig_view import OrganigrammeWindow  # Import de la fenêtre d'organigramme
from views.demande_view import DemandeConge  # Import de la fenêtre de demande de congé 
from controllers.auth_controller import login_utilisateur  # Import du contrôleur d'authentification
from PySide6.QtGui import QIcon
from database import dataBase as database

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("image/MK4_LOGO.png"))
        self.setToolTip("bonjour 😁😀😁")
        self.ui = Ui_MainWindow() # Connexion du bouton de gestion des utilisateurs
        
        self.ui.setupUi(self)

        self.ui.admin_mode.clicked.connect(self.open_user_management)#pour le mode adminnistrateur de notre application
        self.ui.button_orga.clicked.connect(self.open_orga)#l'organigramme de notre application
        self.ui.button_conger.clicked.connect(self.open_conger)#pour la demande de congé

        self.charger_toutes_les_tables()

    def set_login_info(self, login):
        self.ui.lineEdit_role.setText(login['roles'])  # Affiche le rôle de l'utilisateur connecté
        self.ui.lineEdit_poste.setText(login['nom_poste'])  # Affiche l'email de l'utilisateur connecté
        self.ui.lineEdit_nom.setText(login['nom'])  # Affiche le nom de l'utilisateur connecté
        self.ui.lineEdit_iduser.setText(str(login['id']))  # Affiche l'ID de l'utilisateur connecté
        
        
    def open_user_management(self):
        # Logique pour ouvrir la gestion des utilisateurs
        print("Ouverture de la gestion des utilisateurs")
        # Ici, tu peux ajouter le code pour ouvrir une nouvelle fenêtre ou afficher un dialogue
        # par exemple, en instanciant une nouvelle classe de gestion des utilisateurs
        # user_management_window = UserManagementWindow()
        # user_management_window.show()# Ici tu mets ta logique d'authentification
        self.admin = AdminModeWindow()
        self.admin.show()
        print("Connexion réussie ! dans la gestion des utilisateur")#histoire de savoir si on est bien connecté
        self.close()  # ferme la fenêtre de login
    
    def open_orga(self):
        # Logique pour ouvrir l'organigramme
        print("Ouverture de l'organigramme")
        # Ici, tu peux ajouter le code pour ouvrir une nouvelle fenêtre ou afficher un dialogue
        # par exemple, en instanciant une nouvelle classe de l'organigramme
        # orga_window = OrgaWindow()
        # orga_window.show()# Ici tu mets ta logique d'authentification
        self.orga = OrganigrammeWindow()
        self.orga.show()
        print("Connexion réussie ! dans l'organigramme")#histoire de savoir si on est bien connecté
        self.close()  # ferme la fenêtre de login

    def open_conger(self):
        # Logique pour ouvrir la demande de congé
        print("Ouverture de la demande de congé")
        # Ici, tu peux ajouter le code pour ouvrir une nouvelle fenêtre ou afficher un dialogue
        # par exemple, en instanciant une nouvelle classe de la demande de congé
        # conger_window = CongerWindow()
        # conger_window.show()# Ici tu mets ta logique d'authentification
        self.conger = DemandeConge()
        self.conger.show()
        print("Connexion réussie dans le formulaire de demande de congé")#histoire de savoir si on est bien connecté
        self.close()  # ferme la fenêtre de login

        

    def charger_conges(self, statut=None):
        # Connexion à la base de données (modifie selon ton config)
        conn = database.get_connection()
        # Connexion à la base de données
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT u.id as id_user, u.nom, p.nom as nom_poste, c.date_debut, c.date_fin
            FROM conges c
            JOIN utilisateurs u ON c.utilisateur_id = u.id
            LEFT JOIN postes p ON u.poste_id = p.id
        """
        if statut:
            query += " WHERE c.statut = %s"
            cursor.execute(query, (statut,))
        else:
            cursor.execute(query)

        resultats = cursor.fetchall()

        # Choix de la table à remplir selon le statut
        if statut == 'en_attente':
            table = self.ui.table_attente
        elif statut == 'valide':
            table = self.ui.table_dispo
        else:
            table = self.ui.table_conge

        table.setRowCount(0)  # Vide la table avant insertion

        for row_data in resultats:
            row_index = table.rowCount()
            table.insertRow(row_index)
            table.setItem(row_index, 0, QTableWidgetItem(str(row_data['id_user'])))
            table.setItem(row_index, 1, QTableWidgetItem(row_data['nom']))
            table.setItem(row_index, 2, QTableWidgetItem(row_data['nom_poste'] or "Non défini"))
            table.setItem(row_index, 3, QTableWidgetItem(str(row_data['date_debut'])))
            table.setItem(row_index, 4, QTableWidgetItem(str(row_data['date_fin'])))

        cursor.close()
        conn.close()

    def charger_toutes_les_tables(self):
        self.charger_conges()              # Tous les congés
        self.charger_conges('en_attente') # Congés en attente
        self.charger_conges('valide')     # Congés validés (disponibles)
