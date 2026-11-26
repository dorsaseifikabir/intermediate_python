from product import Product
from inventory import Inventory
import sys

my_inventory = Inventory()

action_list = {}


def add_item():
    my_inventory.add_to_inventory(Product.add_item())


def calculate_item_value():
    chosen_item = my_inventory.search_product()
    if chosen_item:
        item_value = chosen_item.calculate_product_value()
        print(f"the value of the chosen product is {item_value}$")


def update_item():
    chosen_item = my_inventory.search_product()
    if chosen_item:
        chosen_item.update_product()


menu = {
    1: ("view inventory", my_inventory.view_inventory),
    2: ("add item", add_item),
    3: ("search item", my_inventory.search_product),
    4: ("delete item", my_inventory.delete_product),
    5: ("update an item", update_item),
    6: ("calculate whole inventory value", my_inventory.calculate_inventory_value),
    7: ("calculate item value", calculate_item_value),
    8: ("quit", sys.exit)
}

for num, (option, action) in menu.items():
    action_list[str(num)] = action
    action_list[option] = action

print("hello and welcome to your inventory management system!")

while True:
    print(" menu ".center(40, "="))
    for num, (option, action) in menu.items():
        print(f"{num}: {option}")
    chosen_action = input("what whould you like to do? ").strip().lower()
    if chosen_action not in action_list:
        print("please choose from the menu!")
        continue
    else:
        action_list[chosen_action]()
