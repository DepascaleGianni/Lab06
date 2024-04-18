import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddYear = None
        self._ddBrand = None
        self._ddRetailer = None
        self._btnTopSales = None
        self._btnAnalyse = None
        self.lst_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Sales Analyse", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self._ddYear = ft.Dropdown(label='anno',width=200, hint_text="select the year", on_change=self._controller.read_year,
                                   options=[ft.dropdown.Option(key="",text="No selection")])
        self._controller.fillDdYear()
        self._ddBrand = ft.Dropdown(label='brand',width=200, hint_text="select the brand", on_change=self._controller.read_brand,
                                    options=[ft.dropdown.Option(key="",text="No selection")])
        self._controller.fillDdBrand()
        self._ddRetailer = ft.Dropdown(label='retailer', width=200, hint_text="select the retailer",
                                       options=[ft.dropdown.Option(key="",text="No selection", data=None)])
        self._controller.fillDdRetailer()

        row1 = ft.Row([self._ddYear, self._ddBrand,self._ddRetailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #Row 2

        self._btnTopSales = ft.ElevatedButton(text="Top sales",
                                              on_click=self._controller.handle_top_sales,
                                              tooltip="select the 5 best sales for the selected filters")
        self._btnAnalyse = ft.ElevatedButton(text="Analyse",
                                             on_click=self._controller.handle_analyse,
                                             tooltip="analizza")

        row2 = ft.Row(controls=[self._btnTopSales,self._btnAnalyse],
        alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)


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
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
