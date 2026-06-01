inventory = {}
categories = set()


def add_product():
    pid = input("Enter Product ID: ")

    if pid in inventory:
        print("Product already exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    supplier = input("Enter Supplier: ")

    inventory[pid] = {
        "name": name,
        "category": category,
        "qty": qty,
        "price": price,
        "supplier": supplier
    }

    categories.add(category)
    print("Product Added Successfully!")


def update_inventory():
    pid = input("Enter Product ID: ")

    if pid not in inventory:
        print("Product not found!")
        return

    inventory[pid]["qty"] = int(input("New Quantity: "))
    inventory[pid]["price"] = float(input("New Price: "))

    print("Inventory Updated!")


def search_product():
    keyword = input("Enter Product ID or Name: ").lower()

    found = False

    for pid, product in inventory.items():
        if keyword == pid.lower() or keyword in product["name"].lower():
            print(pid, product)
            found = True

    if not found:
        print("No product found.")


def display_inventory():
    if not inventory:
        print("Inventory Empty!")
        return

    print("\n--- INVENTORY ---")
    print("ID\tName\tQty\tPrice\tCategory")

    for pid, p in inventory.items():
        print(f"{pid}\t{p['name']}\t{p['qty']}\t{p['price']}\t{p['category']}")


def low_stock_alert():
    threshold = int(input("Enter Threshold: "))

    print("\nLow Stock Products:")
    for pid, p in inventory.items():
        if p["qty"] < threshold:
            print(pid, p["name"], "Qty:", p["qty"])


def out_of_stock_alert():
    print("\nOut Of Stock Products:")

    for pid, p in inventory.items():
        if p["qty"] == 0:
            print(pid, p["name"])


def inventory_report():
    total_items = sum(p["qty"] for p in inventory.values())
    total_value = sum(p["qty"] * p["price"] for p in inventory.values())

    print("\n--- REPORT ---")
    print("Total Products:", len(inventory))
    print("Total Items:", total_items)
    print("Total Value:", total_value)
    print("Categories:", categories)


def delete_product():
    pid = input("Enter Product ID: ")

    if pid in inventory:
        del inventory[pid]
        print("Product Deleted!")
    else:
        print("Product Not Found!")


while True:
    print("\n===== SMART INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Update Inventory")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Low Stock Alert")
    print("6. Out Of Stock Alert")
    print("7. Category Management")
    print("8. Inventory Report")
    print("9. Delete Product")
    print("0. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        search_product()
    elif choice == "4":
        display_inventory()
    elif choice == "5":
        low_stock_alert()
    elif choice == "6":
        out_of_stock_alert()
    elif choice == "7":
        print("Categories:", categories)
    elif choice == "8":
        inventory_report()
    elif choice == "9":
        delete_product()
    elif choice == "0":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
