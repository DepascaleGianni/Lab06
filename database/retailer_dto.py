from dataclasses import dataclass

@dataclass()
class Retailer:
    retailer_code : float
    retailer_name : str
    type : str
    country : str

    def __str__(self):
        return f"{self.retailer_code} - {self.retailer_name}"
    def __eq__(self, other):
        return self.retailer_code == other.retailer.retailer_code

    def __hash__(self):
        return hash(self.retailer_code)

