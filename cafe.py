import sys
menu = {
    'Pizza':280,
    'Burger':200,
    'Pasta':180,
    'Sandwitch':120,
    'Coffee':90
}

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

# The first iterface for the RMS
def main():
    print("Welcome to Ool Jalool Cafe!!")

    while True:
        print("\n------------Main menu-----------")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Exit")

        Choice = input("Enter your choice (1-3): ")

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
            print("Thank you for visiting Ool Jalool Cafe! Goodbye.")
            sys.exit()

        else:
            print("Invalid choice! Please select from the available options. ")
             

if __name__ == "__main__":
  main()





























