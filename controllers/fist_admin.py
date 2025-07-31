import mysql.connector
import os
import database.dataBase as dataBase

def create_admin_user():
    
    # Connexion à la base de données
    conn = dataBase.get_connection()

    cursor = conn.cursor()

    # Script SQL à exécuter
    sql = """
    INSERT INTO utilisateurs (nom, post_nom, prenom, email, mot_de_passe, poste_id, manager_id, roles)
    SELECT * FROM (
        SELECT 
            'Marc' AS nom,
            'Lightning' AS post_nom,
            'Root' AS prenom,
            'lightningmarc@example.com' AS email,
            'lightningRoot' AS mot_de_passe,
            NULL AS poste_id,
            NULL AS manager_id,
            'admin' AS roles
    ) AS tmp
    WHERE NOT EXISTS (
        SELECT 1 FROM utilisateurs WHERE email = 'admin@example.com'
    ) LIMIT 1;
    """

    try:
        cursor.execute(sql)
        conn.commit()
        print("Insertion terminée (ou déjà existante).")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        cursor.close()
        conn.close()
