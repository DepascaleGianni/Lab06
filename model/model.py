import database.DAO as dao
from database.retailer_dto import Retailer

class Model:
    def __init__(self):
        self._d = dao.DAO()

    def get_years(self):
        return  self._d.get_years()
    def get_brands(self):
        return self._d.get_brands()

    def get_retailers(self):
        return self._d.get_retailers()

    def get_top_sales(self,year, brand, retailer : Retailer):
        self._d.get_filtered_sales(year,brand,retailer.retailer_code)


# if __name__ == '__main__':
#     m = Model()
#     print((m.get_brands()))
