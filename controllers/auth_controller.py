import mysql.connector
import database.dataBase as dataBase

def login_utilisateur(email, mot_de_passe):
    try:
        conn = dataBase.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            utilisateurs.*, 
            postes.nom AS nom_poste
        FROM utilisateurs
        LEFT JOIN postes ON utilisateurs.poste_id = postes.id
        WHERE utilisateurs.email = %s AND utilisateurs.mot_de_passe = %s
        """
        cursor.execute(query, (email, mot_de_passe))
        utilisateur = cursor.fetchone()

        if utilisateur:
            print("Connexion réussie ✅")
            return utilisateur
        else:
            print("Email ou mot de passe incorrect ❌")
            return None

    except mysql.connector.Error as err:
        print(f"Erreur de connexion : {err}")
        return None
    finally:
        cursor.close()
        conn.close()
