from database.DB_connect import DBConnect
from database.retailer_dto import Retailer


class DAO():
    def __init__(self):
        pass

    def get_years(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Could not connect")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT YEAR(Date) FROM go_daily_sales"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['YEAR(Date)'])
        cursor.close()
        cnx.close()
        return result

    def get_brands(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Could not connect")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT Product_brand FROM go_products"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['Product_brand'])
        cursor.close()
        cnx.close()
        return result

    def get_retailers(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Could not connect")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM go_retailers"""
        cursor.execute(query)
        for row in cursor:
            ret_temp = Retailer(row['Retailer_code'],row['Retailer_name'],row['Type'],row['Country'])
            result.append(ret_temp)
        cursor.close()
        cnx.close()
        return result

    def get_filtered_sales(self,year,brand,ret_code):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Could not connect")
            return None

        cursor = cnx.cursor(dictionary = True)
        query = """ SELECT Retailer_code,Product_number,Date,Quantity*Unit_sale_price
                FROM """

if __name__ == '__main__':
    dao = DAO()
    anni = dao.get_years()
    brands = dao.get_brands()
    ret = dao.get_retailers()
    print(ret)


