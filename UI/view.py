import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._cognome = None
        self._nome = None
        self._matr = None
        self._btnIscrivi = None
        self._btnCorso = None
        self._searchBtn = None
        self._btnStud = None
        self._dd = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW CERCA ISCRITTI PER CORSO
        self._dd = ft.Dropdown(label="corso", hint_text="Seleziona Corso", width=600)
        self._searchBtn = ft.ElevatedButton(text="Cerca iscritti", width=100, on_click=self._controller.handleIscritti)
        self._controller.popolaDD()

        row = ft.Row([self._dd, self._searchBtn], alignment=ft.MainAxisAlignment.CENTER)

        # MATRICOLA NOME COGNOME
        self._matr = ft.TextField(hint_text="Inserire matricola")
        self._nome = ft.TextField(label= "nome",hint_text="nome",read_only=True)
        self._cognome = ft.TextField(label="cognome",hint_text="cognome",read_only=True)
        row1 = ft.Row([self._matr, self._nome, self._cognome], alignment=ft.MainAxisAlignment.CENTER)

        # BUTTONI
        self._btnStud = ft.ElevatedButton(text="Matricola", width=150, color="lightblue", on_click=self._controller.handleMatricola)
        self._btnCorso = ft.ElevatedButton(text="Corso", width=150, on_click=self._controller.handleCorso)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi", width=150, on_click=self._controller.handleIscrivi)
        row2 = ft.Row([self._btnStud, self._btnCorso, self._btnIscrivi], alignment=ft.MainAxisAlignment.CENTER)




        self._page.add(row, row1, row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
