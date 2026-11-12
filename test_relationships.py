from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


def test_relationships():

    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "tech@example.com"
    )

    # Create products independently
    laptop = PhysicalProduct(
        "P001", "Laptop", 1200, 15, 2.5, supplier
    )

    antivirus = DigitalProduct(
        "D001", "Antivirus", 45, 25, 500, supplier
    )

    # Test association
    print("\nTEST ASSOCIATION")

    laptop.display_supplier_information()
    antivirus.display_supplier_information()

    print(laptop.supplier is supplier)
    print(antivirus.supplier is supplier)

    # Test aggregation
    print("\nTEST AGGREGATION")

    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(laptop)

    inventory_a.remove_product("P001")

    print("Product still exists:", laptop.name)

    inventory_b.add_product(laptop)

    print("Product in Inventory B:",
          inventory_b.search_product("P001") is laptop)

    # Test polymorphism
    print("\nTEST POLYMORPHISM")

    inventory_b.add_product(antivirus)

    for product in inventory_b.get_products():

        product.display_information()

        print("Fulfilment:",
              product.get_fufillment_method())

    # Test composition
    print("\nTEST COMPOSITION")

    order_a = Order("O001")
    order_b = Order("O002")

    order_a.add_order_line(laptop, 2)
    order_a.add_order_line(antivirus, 1)

    order_b.add_order_line(laptop, 3)

    order_a.display_order()
    order_b.display_order()

    print(
        "Same Product object:",
        order_a.order_lines[0].product
        is order_b.order_lines[0].product
    )

    print(
        "Different OrderLine objects:",
        order_a.order_lines[0]
        is not order_b.order_lines[0]
    )


if __name__ == "__main__":
    test_relationships()
