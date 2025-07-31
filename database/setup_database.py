import mysql.connector
import os
import sys

# 🔧 Ajouter le dossier parent au chemin Python pour accéder à config/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Importer la config de connexion
from config.db_config import DB_HOST, DB_USER, DB_PASSWORD

def execute_sql_script(file_path):
    try:
        # Connexion MySQL (sans base de données pour créer la DB)
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # 🔁 Lecture du fichier SQL
        with open(file_path, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # ✂️ Séparer les instructions et les exécuter une par une
        for statement in sql_script.split(";"):
            if statement.strip():
                cursor.execute(statement)

        conn.commit()
        print("✅ Base de données initialisée avec succès.")
    except mysql.connector.Error as err:
        print(f"Message MySQL : {err}")
    except Exception as e:
        print(f"Message : {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # 🔍 Calcul du chemin absolu vers init.sql
    current_dir = os.path.dirname(__file__)
    sql_path = os.path.join(current_dir, "init.sql")

    execute_sql_script(sql_path)
