# Inventory Management System


inventory = {}

def add_item():
    """Add a new item to the inventory with quantity and price"""
    item_name = input("Enter item name: ").strip().lower()
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
                continue
            break
        except ValueError:
            print("Please enter a valid number for quantity!")
    
    while True:
        try:
            price = float(input("Enter price per unit: "))
            if price < 0:
                print("Price cannot be negative!")
                continue
            break
        except ValueError:
            print("Please enter a valid number for price!")
    
    if item_name in inventory:
        inventory[item_name]['quantity'] += quantity
        inventory[item_name]['price'] = price  # Update price if item exists
        print(f"Updated {item_name.title()} - Quantity: {inventory[item_name]['quantity']}, Price per unit: ${inventory[item_name]['price']:.2f}")
    else:
        inventory[item_name] = {'quantity': quantity, 'price': price}
        print(f"Added {item_name.title()} - Quantity: {quantity}, Price per unit: ${price:.2f}")

def display_inventory():
    """Display all items in the inventory with quantities and prices"""
    if not inventory:
        print("Inventory is empty!")
        return
    
    print("\nCurrent Inventory:")
    print("-----------------")
    for item, details in inventory.items():
        print(f"Item: {item.title()}, Quantity: {details['quantity']}, Price per unit: ${details['price']:.2f}")
    print()

def update_quantity():
    """Update quantity and price of an existing item"""
    item_name = input("Enter item name to update: ").strip().lower()
    if item_name not in inventory:
        print(f"{item_name.title()} not found in inventory!")
        return
    
    while True:
        try:
            quantity = int(input("Enter new quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
                continue
            break
        except ValueError:
            print("Please enter a valid number for quantity!")
    
    while True:
        try:
            price = float(input("Enter new price per unit: "))
            if price < 0:
                print("Price cannot be negative!")
                continue
            break
        except ValueError:
            print("Please enter a valid number for price!")
    
    inventory[item_name]['quantity'] = quantity
    inventory[item_name]['price'] = price
    print(f"Updated {item_name.title()} - Quantity: {quantity}, Price per unit: ${price:.2f}")

def remove_item():
    """Remove an item from the inventory"""
    item_name = input("Enter item name to remove: ").strip().lower()
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name.title()} removed from inventory")
    else:
        print(f"{item_name.title()} not found in inventory!")

def main():
    """Main function to run the inventory management system"""
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Update Quantity and Price")
        print("4. Remove Item")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_item()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            update_quantity()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting Inventory Management System")
            break
        else:
            print("Invalid choice! Please select 1-5")

# Run the program
if __name__ == "__main__":
    main()