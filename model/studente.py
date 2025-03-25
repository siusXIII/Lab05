from dataclasses import dataclass


@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    cds: str
    def __init__(self, matricola, nome, cognome, cds):
        self._matricola = matricola
        self._cognome = cognome
        self._nome = nome
        self._cds = cds

    @property
    def matricola(self):
        return self._matricola

    @property
    def nome(self):
        return self._nome

    @property
    def cognome(self):
        return self._cognome

    @property
    def cds(self):
        return self._cds

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"
