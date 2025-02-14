# Restaurant Menu
menu = {
    'Pizza': 90,
    'Pasta': 70,
    'Burger': 87,
    'Salad': 88,
    'Coffee': 100,
}

# Greeting
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs90\nPasta: Rs70\nBurger: Rs87\nSalad: Rs88\nCoffee: Rs100")

# Order Processing
order_total = 0

item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to the order.")
    else:
        print(f"Ordered item {item_2} is not available!")

# Display total
print(f"The total amount to pay is Rs{order_total}.")
