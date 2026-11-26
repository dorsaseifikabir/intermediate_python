class Product:
    def __init__(self, name, brand, category, price, quantity):
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name

    def show_status(self):
        print(f"""
        Name: {self.name}
        Brand: {self.brand}
        Category: {self.category}
        Price: ${self.price}
        Quantity: {self.quantity}
        """
              )

    @classmethod
    def add_item(cls):
        name = input(
            "please enter the item name\t").strip().lower()
        brand = input("what is the brand of the new item:\t").strip().lower()
        category = input(
            "what category does the new item belong to:\t").strip().lower()

        while True:
            try:
                price = int(input("how much does the new item cost:\t"))
            except ValueError:
                print("you must enter the price!")
                continue
            else:
                break

        while True:
            try:
                quantity = int(input(
                    "how many of the new item do you have in your inventory:\t"))
            except ValueError:
                print("you must enter the quantity!")
                continue
            else:
                break

        new_item = cls(name, brand,
                       category, price, quantity)
        return new_item

    def calculate_product_value(self):
        product_value = self.quantity * self.price
        return product_value

    def update_product(self):
        which_attribute = input(
            "\nwhich info would you like to update?\n").lower().strip()
        if hasattr(self, which_attribute) and which_attribute != 'name':
            while True:
                try:
                    new_value = input(
                        "\nwhat is the updated value?\n").lower().strip()
                    if which_attribute in ['price', 'quantity']:
                        new_value = int(new_value)
                        break
                    else:
                        break
                except ValueError:
                    print("\nyou must enter a number!\n")
                    continue
            setattr(self, which_attribute, new_value)
        else:
            print("\nyou don't have that info about your products in your inventory!\n")
