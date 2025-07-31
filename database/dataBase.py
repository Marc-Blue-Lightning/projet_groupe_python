# db.py
import os
import sys
import mysql.connector

# 🔧 Ajouter le dossier parent au chemin Python pour accéder à config/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Importer la config de connexion
from config.db_config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
