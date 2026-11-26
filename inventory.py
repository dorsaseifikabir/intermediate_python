from product import Product


class Inventory:
    def __init__(self):
        self.products = {}

    def add_to_inventory(self, new_item):
        if new_item.name in self.products:
            print("\nthat product ia already registered in your inventory!\n")
        else:
            self.products[new_item.name] = new_item

    def view_inventory(self):
        if not self.products:
            print(f"\nthere is no item in your inventory yet!\n")
        else:
            for name, item in self.products.items():
                print(name.center(20, "+"))
                item.show_status()

    def delete_product(self):
        del_item = input(
            "\nwhich item do you want to delete?\n").strip().lower()
        if del_item in self.products:
            del self.products[del_item]
        else:
            print("\nyou don't have that item in your inventory!\n")

    def search_product(self):
        search_item = input(
            "\nwhich product are you looking for?\n").lower().strip()
        if search_item in self.products:
            self.products[search_item].show_status()
            return self.products[search_item]
        else:
            print("\nyou don't have that item in your inventory!\n")

    def calculate_inventory_value(self):
        total_value = 0
        if not self.products:
            print(f"\nthere is no item in your inventory yet!\n")
        else:
            for item in self.products.values():
                item_value = item.calculate_product_value()
                total_value = total_value + item_value
            print(f"\ntotal inventory value is: {total_value}s\n")
