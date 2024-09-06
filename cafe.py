import sys
menu = {
    'Pizza':280,
    'Burger':200,
    'Pasta':180,
    'Sandwitch':120,
    'Coffee':90
}

# Admin Password for admin access panel
admin_password = "admin123"

# Display menu Funtion
def display_menu():
    print("\n--------Menu--------")
    for item, price in menu.items():
        print(f"{item}: Rs {price}")
    print("------------------------\n")

# Taking order
def take_order():
    order = {}
    while True:
        display_menu()
        item = input("What would you like to order(or type Done to finish): ").capitalize()
        if item == "Done":
            break
        elif item in menu:
            quantity = int(input(f"How many {item}(s) you would like to order? "))
            order[item] = order.get(item, 0) + quantity
            print(f"{quantity} {item}(s) added to your order")
        else:
            print(f"Sorry, the {item} you ask for is not available.\nPlease order something form the menu")

    return order

# Making the bill
def calculate_bill(order):
    total_amount = 0
    print("\n---------Your Bill----------")
    for item, quantity in order.items():
        cost = menu[item] * quantity
        total_amount += cost
        print(f"{item}: {quantity} x Rs {menu[item]} = {cost}Rs")
        print(f"--------------------------\nTotal Amount To Pay: Rs {total_amount}")
        print("-------------------------\n")

    return total_amount

# Receipt For the Customer
def customer_recepit(order, total_amount):
    print("\n----------Recepit-----------")
    for item, quantiy in order.items():
        print(f"{item}: {quantiy} x Rs {menu[item]} = Rs {menu[item] * quantiy} ")
    print(f"Total Amount: Rs {total_amount}")
    print("Thank for Ordering from Ool Jalool Cafe!!\n----------------------")

# Admin Panel (Admin can modify menu add and remove update item )
def admin_panel():
    print("\n----------Welcome to the admin panel-------")
    pasword = input("Enter the admin password: ")
    if pasword == admin_password:
        while True:
            print("\nAdmin Panel Options: ")
            print("1. Add new item to the menu")
            print("2. Remove Item from the menu")
            print("3. Update an item from the menu")
            print("4. View menu")
            print("5. Exit")

            choice = input("Enter Your Choice (1-5): ")

            if choice == "1":
                item = input("Enter the name of the new item: ").capitalize()
                if item in menu:
                    print(f"{item} already exists in the menu.")
                else:
                    price = int(input(f"Enter the price for {item}: Rs "))
                    menu[item] = price
                    print(f"{item} has been added to the menu with a price of Rs {price}.")

            elif choice == '2':
                item = input("Enter the name of the item to remove: ").capitalize()
                if item in menu:
                    del menu[item]
                    print(f"{item} has been removed from the menu.")
                else:
                    print(f"{item} is not in the menu.")

            elif choice == '3':
                item = input("Enter the name of the item to update: ").capitalize()
                if item in menu:
                    price = int(input(f"Enter the new price for {item}: Rs "))
                    menu[item] = price
                    print(f"The price of {item} has been updated to Rs {price}.")
                else:
                    print(f"{item} is not in the menu.")

            elif choice == '4':
                display_menu()

            elif choice == '5':
                print("Exiting Admin Panel...")
                break

            else:
                print("Invalid choice! Please select from the available options.")
    else:
        print("Invalid password! Access Denied.")       

# The first iterface for the RMS
def main():
    print("Welcome to Ool Jalool Cafe!!")

    while True:
        print("\n------------Main menu-----------")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Admin panel")
        print("4. Exit")

        Choice = input("Enter your choice (1-4): ")

        if Choice == "1":
           display_menu()
        elif Choice == "2":
            order = take_order()
            if order:
                total_amount = calculate_bill(order)
                customer_recepit(order, total_amount)
            else:
                print("You haven't order anything yet.")

        elif Choice == "3":
            admin_panel()

        elif Choice == "4":
            print("Thank you for visiting Ool Jalool Cafe! Goodbye.")
            sys.exit()

        else:
            print("Invalid choice! Please select from the available options. ")
             
if __name__ == "__main__":
  main()












