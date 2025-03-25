# Add whatever it is needed to interface with the DB Table corso


import mysql.connector

from model.corso import Corso
from database.DB_connect import get_connection
from model.studente import Studente


class CorsoDAO:

    @classmethod
    def getAllCorsi(cls):
        corsi = []
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select codins, crediti, nome, pd from corso"""
        cursor.execute(query)
        for (codins, crediti, nome, pd) in cursor:
            corsi.append(Corso(codins, crediti, nome, pd))

        cursor.close()
        cnx.close()
        return corsi

    def get_iscritti_corso(codins) -> list[Studente] | None:
        """
        Funzione che recupera una lista con tutti gl istudenti iscritti al corso selezionato
        :param corso: il corso di cui recuperare gli iscritti
        :return: una lista con tutti gli studenti iscritti
        """
        cnx = get_connection()
        result = []
        query = """SELECT studente.* 
                    FROM iscrizione, studente 
                    WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s"""

        if cnx is not None:
            cursor = cnx.cursor()

            cursor.execute(query, (codins,))
            for codins1, crediti, nome, pd in cursor:
                result.append(Studente(codins1, crediti, nome, pd))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Could not connect")
            return None


    def getCorsiByStudente(matr):
        cnx = get_connection()
        result = []
        query = """ SELECT corso.* 
            FROM corso, iscrizione 
            WHERE iscrizione.codins=corso.codins AND iscrizione.matricola = %s
            """
        if cnx is not None:
            cursor = cnx.cursor()
            cursor.execute(query, (matr,))
            for codins, crediti, nome, pd in cursor:
                result.append(Corso(codins, crediti, nome, pd))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Could not connect")
            return result

    def iscrivi_corso(matricola, codins) -> bool:
        """
        Funzione che aggiunge uno studente agli iscritti di un corso
        :param matricola: la matricola dello studente
        :param codins: il codice del corso
        :return: True se l-operazione va a buon fine, False altrimenti
        """
        cnx = get_connection()
        result = []
        query = """INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
        (`matricola`, `codins`) 
        VALUES(%s,%s)
        """
        if cnx is not None:
            cursor = cnx.cursor()
            cursor.execute(query, (matricola, codins,))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        else:
            print("Could not connect")
            return False