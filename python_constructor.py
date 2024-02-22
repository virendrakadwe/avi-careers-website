class Item:  # Class
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        #Assign to self object
        self.price = price
        self.name = name
        self.quantity = quantity

    def calculate_total_amount(self):  # Methods
        return self.price * self.quantity
    # print(f"An instance created: {name} and price of {name} is {price} for {quantity} each and total price"
    #       f" will be {price*quantity}")


item1 = Item("Phone", 100,3)
item2 = Item("Laptop", 1000,5)

print(item1.name, item1.price)
print(item2.name, item2.price)
print(item1.calculate_total_amount())
print(item2.calculate_total_amount())
