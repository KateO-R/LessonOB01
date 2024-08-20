class Store:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def add_multiple_items(self, items):
        for name, price in items:
            self.add_item(name, price)

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

store1 = Store("First Store", "Main Street 1")
store2 = Store("Second Store", "Second Street 2")
store3 = Store("Third Store", "Third Street 3")

store1.add_multiple_items([
    ('apples', 0.5),
    ('bananas', 0.3),
    ('oranges', 0.7)
])
print(store1.get_price("apples"))

store1.update_price("apples", 0.6)
print(store1.get_price("apples"))

store1.remove_item("bananas")
print(store1.get_price("bananas"))



