from database import corso_DAO, studente_DAO


class Model:
    def __init__(self):
        self._corsi = []
        self._studenti = []

    def getAllCorsi(self):
        self._corsi = corso_DAO.CorsoDAO.getAllCorsi()
        return self._corsi

    def getAllStudenti(self):
        self._studenti= studente_DAO.StudenteDAO.getAllStudenti()
        return self._studenti

    def cercaStudente(self, m):
        s = studente_DAO.StudenteDAO.cerca_studente(m)
        return s

    def getStudentsByCorso(self, corso):
        self._studenti = corso_DAO.CorsoDAO.get_iscritti_corso(corso)
        return self._studenti

    def getCorsoByStudenti(self, matr):
        self._corsi = corso_DAO.CorsoDAO.getCorsiByStudente(matr)
        return self._corsi

    def iscrivi_corso(self, matricola, codin):
        return corso_DAO.CorsoDAO.iscrivi_corso(matricola, codin)
