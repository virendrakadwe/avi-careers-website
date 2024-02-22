class Item:  # Class
    pay_rate: float = 0.8  # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign to self object
        self.price = price
        self.name = name
        self.quantity = quantity

    def calculate_total_amount(self):  # Methods
        return self.price * self.quantity

    # print(f"An instance created: {name} and price of {name} is {price} for {quantity} each and total price"
    #       f" will be {price*quantity}")

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 500, 3)  # These are instance attributes
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 10000, 5)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

# print(item1.name, item1.price)
# print(item2.name, item2.price)
# print(item1.calculate_total_amount())
# print(item2.calculate_total_amount())
# print(Item.pay_rate)  # he pay_rate is the class attribute which was call directly from the class

print(Item.__dict__)  # All the attributes from the class level
  # All the attributes from the instance level
