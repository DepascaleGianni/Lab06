import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.selected_year = None
        self.selected_brand = None
        self.selected_retailer_object = None

    def fillDdYear(self):
        years = self._model.get_years()
        for el in years:
            self._view._ddYear.options.append(ft.dropdown.Option(key=el, text=el.__str__()))


    def fillDdBrand(self):
        brands = self._model.get_brands()
        for el in brands:
            self._view._ddBrand.options.append(ft.dropdown.Option(key=el, text=el.__str__()))

    def fillDdRetailer(self):
        ret = self._model.get_retailers()
        for el in ret:
            self._view._ddRetailer.options.append(ft.dropdown.Option(key=el.retailer_code, text=el.retailer_name,data=el,on_click=self.read_retailer))

    def read_year(self,e):
        self.selected_year = self._view._ddYear.value

    def read_brand(self,e):
        self.selected_brand = self._view._ddBrand.value

    def read_retailer(self,e):
        self.selected_retailer = e.control.data

    def handle_top_sales(self,e):
        self._model.get_top_sales(self.selected_year,self.selected_brand,self.selected_retailer)

    def handle_analyse(self,e):
        pass
