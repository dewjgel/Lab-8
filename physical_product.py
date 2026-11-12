from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.weight: float = float(weight)

        if self.weight < 0:
            raise ValueError("Weight cannot be negative.")

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight:.2f} kg")

    def get_fufillment_method(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        shipping_rate: float = 5.00
        return self.weight * shipping_rate

CanBeShipped.register(PhysicalProduct)