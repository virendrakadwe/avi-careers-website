class Item:  # Class
    pay_rate: float = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign to self object
        self.price = price
        self.name = name
        self.quantity = quantity

    # Actions to executed 
        Item.all.append(self)

    def calculate_total_amount(self):  # Methods
        return self.price * self.quantity

    # print(f"An instance created: {name} and price of {name} is {price} for {quantity} each and total price"
    #       f" will be {price*quantity}")

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

for instance in Item.all:
    print(instance.name)
    print(instance.price)
