from dataclasses import dataclass
from database.retailer_dto import Retailer
from database.product_dto import Product
from datetime import date

@dataclass()
class Sale:
    retailer : str
    product : str
    date : date
    ricavo : float

    #lazy
    #lazy
