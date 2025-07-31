import database.dataBase as dataBase

class user:
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
    
    def recuperer_utilisateur(self, id_utilisateur):
        query = "SELECT * FROM utilisateurs WHERE id = %s"
        self.cursor.execute(query, (id_utilisateur,))
        return self.cursor.fetchone()
    
    def modifier_utilisateur(self, id_utilisateur, nom=None, post_nom=None, prenom=None, email=None, mot_de_passe=None, poste_id=None, manager_id=None, role=None):
        query = "UPDATE utilisateurs SET "
        values = []
        if nom:
            query += "nom = %s, "
            values.append(nom)
        if post_nom:
            query += "post_nom = %s, "
            values.append(post_nom)
        if prenom:
            query += "prenom = %s, "
            values.append(prenom)
        if email:
            query += "email = %s, "
            values.append(email)
        if mot_de_passe:
            query += "mot_de_passe = %s, "
            values.append(mot_de_passe)
        if poste_id is not None:
            query += "poste_id = %s, "
            values.append(poste_id)
        if manager_id is not None:
            query += "manager_id = %s, "
            values.append(manager_id)
        if role:
            query += "roles = %s "
            values.append(role)
        
        query += "WHERE id = %s"
        values.append(id_utilisateur)

        self.cursor.execute(query, tuple(values))
        self.conn.commit()