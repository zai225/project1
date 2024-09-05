# Making a Resturant biling system with any interface 
# Making a dic for the menu
menu = {
    'pizza':200,
    'burger':150,
    'pasta':180,
    'fries':100,
    'coffee':80,
}
# Greating 
print("Welcome to Ool Jalool Cafe")
print("Pizza: Rs200\nBurger: Rs150\nPasta: Rs180\nFries: Rs100\nCoffee: Rs80")

order_total = 0
item_1 = input("What do you want to have today Sir/Ma'am: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your Item {item_1.capitalize()} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet")

another_order = input("Is there any thing else you want to add? (Yes/No): ").lower()
if another_order == "yes":
    item_2 = input("Enter the item you want to order: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2.capitalize()} has added in your order")

    else:
        print(f"Ordered Item {item_2} is not available yet")

print(f"The Total amount of your order to pay is {order_total}")
  
print("Thanks for ordering from Ool Jalool cafe\nYour order will be on your table in 10min")



