# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection

from model.studente import Studente


class StudenteDAO:
    @classmethod
    def getAllStudenti(cls):
        studenti = []
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select  matricola, cognome, nome, cds from studente"""
        cursor.execute(query)
        for matricola, cognome, nome, cds in cursor:
            studenti.append(Studente(matricola, cognome, nome, cds))
        cursor.close()
        cnx.close()
        return studenti

    def cerca_studente(matricola) -> Studente | None:
        """
            Funzione che data una matricola ricerca nel database lo studente corrispondente (se presente)
            :param matricola: la matricola dello studente da ricercare
            :return: uno studente, se presente
            """
        cnx = get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM studente WHERE matricola = %s", (matricola,))
            row = cursor.fetchone()
            if row is not None:
                result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            else:
                result = None
            cursor.close()
            cnx.close()
            return result
        else:
            print("Could not connect")
            return None