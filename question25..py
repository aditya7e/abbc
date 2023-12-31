def display_menu(inventory):
    print("Menu:")
    print("1. Buy Item")
    print("2. Exit")
    print("3. View Stock")

def purchase_item(inventory, item):
    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
        print(f"Purchase successful! {item} deducted from the stock.")
    else:
        print(f"Sorry, {item} is currently unavailable.")

def view_stock(inventory):
    print("Current Stock:")
    for item, count in inventory.items():
        print(f"{item}: {count} available")

# Initial inventory
inventory = {"Item A": 50, "Item B": 50, "Item C": 50}

while True:
    display_menu(inventory)
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        item_choice = input("Enter the item you want to buy: ")
        purchase_item(inventory, item_choice)
    elif choice == '2':
        print("Exiting the program. Thank you!")
        break
    elif choice == '3':
        view_stock(inventory)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
