from product import Product

class Inventory:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to the inventory.")

        if self.search_product(product.product_id) is not None:
            raise ValueError("Product ID already exists in the inventory.")
            

        self.products.append(product)
        print("Product added successfully.")
        return True

    def remove_product(self, product_id: str) -> bool:

        product = self.search_product(product_id)

        if product is None:
            return False

        self.products.remove(product)
        print("Product removed successfully.")
        return True
     
    def search_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id.lower() == product_id.lower():
                return product
            
        return None

    def display_inventory(self) -> None:
        print("Current Inventory")
        print("-----------------------------------------------")

        if not self.products:
            print("Inventory is empty.")

        else:
            for product in self.products:

                product.display_information()

                print(
                    "Fulfilment:",
                    product.get_fufillment_method()
                )

                print("Supplier:")
                product.display_supplier_information()

                print()

        print("-----------------------------------------------")

    def get_products(self) -> list[Product]:
        return self.products.copy()
