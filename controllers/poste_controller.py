import database.dataBase as dataBase

class poste:
    def __init__(self):
        self.conn = dataBase.get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def add_poste(self, nom, descrip, superieur_id):
        query = """
        INSERT INTO postes (nom, descrip, superieur_id)
        VALUES (%s, %s, %s)
        """
        values = (nom, descrip, superieur_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.conn.commit()
    
    def get_postes(self):
        query = "SELECT * FROM postes"
        self.cursor.execute(query)
        return self.cursor.fetchall()
   