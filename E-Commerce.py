products = {
    101: {"name": "Laptop", "price": 55000.0},
    102: {"name": "Mouse", "price": 559.0},
    103: {"name": "Keyboard", "price": 999.0},
    104: {"name": "USB Cable", "price": 299.0},
    105: {"name": "Laptop", "price": 55000.0},
}

cart = {}

def show_product():
    print("*" * 40)
    print("\nAvailable products")
    print("{:<6}{:<20}{:>10}".format("ID", "Product", "Price(INR)"))
    for prod, item in products.items():
        print("{:<6}{:<20}{:>10.2f}".format(prod, item["name"], item["price"]))
    print()

def add_to_your_cart():
    show_product()
    if len(cart) != 0:
        view_cart()
    add_cart = int(input("Enter the product ID you want to add: "))
    if add_cart in products:
        quantity = int(input("Enter the quantity: "))
        if add_cart in cart:
            cart[add_cart]["quantity"] += quantity
        else:
            cart[add_cart] = {**products[add_cart], "quantity": quantity}
    else:
        print("Product unavailable")

def remove_from_cart():
    view_cart()
    remove_id = int(input("Enter the product ID you want to delete: "))
    quantity = int(input("Enter the quantity to remove: "))
    if remove_id not in cart:
        print("Item not in cart")
    else:
        if cart[remove_id]["quantity"] <= quantity:
            cart.pop(remove_id)
        else:
            cart[remove_id]["quantity"] -= quantity

def view_cart():
    if not cart:
        print("Cart is empty")
        return
    print("\nItems in your cart")
    print("{:<5} {:<10} {:<10} {:<13} {:<10}".format("ID", "Product", "Qty", "Price(INR)", "SubTotal"))
    print("-" * 50)
    total_all_items = 0
    for prod, item in cart.items():
        subtotal = item["price"] * item["quantity"]
        print("{:<5} {:<10} {:<10} {:<13.2f} {:<10.2f}".format(prod, item["name"], item["quantity"], item["price"], subtotal))
        total_all_items += subtotal
    print("-" * 50)
    print("Total amount: INR", total_all_items)
    print()

def check_out():
    if len(cart) != 0:
        print("----Bill---")
        view_cart()
        total_all_items = sum(j["price"] * j["quantity"] for j in cart.values())
        discount = (total_all_items * 5) / 100
        print("Sub total      : INR", total_all_items)
        print("Discount       : INR", discount)
        print("Amount Payable : INR", total_all_items - discount)
        payment = input("Proceed to payment simulation? (Y/y): ")
        if payment.lower() == "y":
            print("Payment successful.\nThank you for shopping with us!\nVisit again.")
        else:
            print("Payment failed, try again.")
    else:
        print("Cart is empty, nothing to checkout.")

def exit_shopping():
    print("Exiting E-commerce app. Goodbye!")

def print_menu():
    print("=" * 6 + " E-commerce Shopping Cart " + "=" * 19)
    print("1. Show Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Exit")
    print("=" * 50)

while True:
    print_menu()
    input_number = int(input("Enter your choice (1-6): "))
    if input_number == 1:
        show_product()
    elif input_number == 2:
        add_to_your_cart()
    elif input_number == 3:
        remove_from_cart()
    elif input_number == 4:
        view_cart()
    elif input_number == 5:
        check_out()
    elif input_number == 6:
        exit_shopping()
        break
    else:
        print("Invalid choice, try again.")
