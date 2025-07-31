import mysql.connector
import database.dataBase as dataBase

class dashboard_Controll:
    def charger_conges(self, statut=None):
        """
        Charge les congés dans la table correspondante selon le statut :
        - statut=None : tous les congés (table_conge)
        - statut='en_attente' : congés en attente (table_attente)
        - statut='valide' : congés validés (table_dispo)
        """
        conn = dataBase.get_connection()
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

        table.setRowCount(0)

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
        self.charger_conges()                # Tous les congés
        self.charger_conges('en_attente')   # Congés en attente
        self.charger_conges('valide')        # Congés validés (disponibles)
