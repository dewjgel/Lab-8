from product import Product

class OrderLine:

    def __init__(self, product: Product, quantity: int) -> None:

        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Quantity must be a whole number.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    def display_information(self) -> None:

        print(f"Product: {self.product.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Unit Price: ${self.product.price:.2f}")
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
