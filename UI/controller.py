import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.corso_selezionato = None

    def popolaDD(self):
        for corso in self._model.getAllCorsi():
            self._view._dd.options.append(ft.dropdown.Option(corso.__str__()))
            self._view.update_page()

    def handleIscritti(self,e):
        if self._view._dd.value is not None:
            testo = self._view._dd.value
            inizio = testo.find("(") + 1
            fine = testo.find(")")
            codice = testo[inizio:fine]
            self.corso_selezionato = codice
        if self.corso_selezionato is None:
            self._view.create_alert("Scegliere un corso!")
            self._view.update_page()
            return
        iscritti = self._model.getStudentsByCorso(self.corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione!")
            return
        self._view.txt_result.controls.clear()
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti al corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))
                self._view.update_page()




        self._view.txt_result.value = ""

    def handleMatricola(self,e):
        studenti = self._model.getAllStudenti()
        if self._view._matr.value == "":
            self._view.create_alert("Inserire matricola!")
            self._view.update_page()
            return
        for s in studenti:
            if s.matricola == int(self._view._matr.value):
                self._view._nome.value = s.nome
                self._view._cognome.value = s.cognome
                self._view.update_page()
                return
        self._view.create_alert("Matricola non presente!")
        self._view.update_page()

    def handleCorso(self,e):
        matricola=self._view._matr.value
        if matricola == "":
            self._view.create_alert("inserire una matricola")
            return
        corsi = self._model.getCorsoByStudenti(int(matricola))
        if len(corsi) == 0:
            self._view.create_alert("La matricola indicata non risulta iscritta ad alcun corso")
        else:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
            for corso in corsi:
                self._view.txt_result.controls.append(ft.Text(f"{corso}"))
            self._view.update_page()

    def handleIscrivi(self, e):
        matricola = self._view._matr.value
        if matricola == "":
            self._view.create_alert("inserire una matricola")
            return
        studente = self._model.cercaStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        codice_corso = self._view._dd.value
        if codice_corso is None:
            self._view.create_alert("Selezionare un corso!")
            return
        corsi = self._model.getCorsoByStudenti(int(matricola))
        presente = False
        for i in corsi:
            if i.codins == codice_corso:
                presente = True
        if not presente:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
            self._view.update_page()
            return
        inizio = codice_corso.find("(") + 1
        fine = codice_corso.find(")")
        codice = codice_corso[inizio:fine]
        result = self._model.iscrivi_corso(matricola, codice)
        self._view.txt_result.controls.clear()
        if result:
            self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()
