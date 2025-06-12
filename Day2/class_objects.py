


class Item:

    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def __str__(self):
            return f'{type(self).__name__} {self.__dict__}'


item1 = Item("pencil", 2)
print(item1)

item2=Item("bag",10)
print(item2)