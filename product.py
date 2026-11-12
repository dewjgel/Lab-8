from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):

    def __init__(self, product_id: str, name:str, price: float, stock: int, supplier: Supplier)-> None:
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)
        self.supplier: Supplier = supplier

        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative.")

    def update_stock(self, quantity: int) -> None:
        if not isinstance(quantity, int) or isinstance(quantity,bool):
            raise ValueError("Stock must be a whole number.")

        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self.stock = quantity

    def display_information(self) -> None:
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")

    def display_supplier_information(self) -> None:
        self.supplier.display_information()

    @abstractmethod
    def get_fufillment_method(self):
        pass