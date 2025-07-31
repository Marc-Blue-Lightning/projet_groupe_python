import database.dataBase as dataBase

class DBManager:
    def __init__(self):
        self.conn = dataBase.get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def ajouter_utilisateur(self, nom, post_nom, prenom, email, mot_de_passe, poste_id=None, manager_id=None, role='employe'):
        query = """
        INSERT INTO utilisateurs (nom, post_nom, prenom, email, mot_de_passe, poste_id, manager_id, roles)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (nom, post_nom, prenom, email, mot_de_passe, poste_id, manager_id, role)
        self.cursor.execute(query, values)
        self.conn.commit()

    def recuperer_utilisateurs_avec_conges(self):
        query = """
        SELECT u.id, u.nom, u.prenom, u.email, p.nom AS poste, c.date_debut, c.date_fin, c.statut
        FROM utilisateurs u
        LEFT JOIN postes p ON u.poste_id = p.id
        LEFT JOIN conges c ON u.id = c.utilisateur_id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
