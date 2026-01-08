class Item:

    def __init__(self, name, weight, importance):

        self.name = name
        self.weight = weight
        self.importance = importance

    def __str__(self):
        return self._name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) < 1:
            raise KeyError('Item name can not be empty')
        else:
            self._name = name
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        if type(weight) != int or weight <= 0:
            raise ValueError('Item weight can not be 0 or less')
        else:
            self._weight = weight

    @property
    def importance(self):
        return self._importance
    
    @importance.setter
    def importance(self, importance):
        if type(importance) != int or importance <= 0:
            raise ValueError('Item importance can not be 0 or less')
        else:
            self._importance = importance


class Backpack:


    def __init__(self, backpack):
        self.backpack = backpack
        self.items = {} # fill with class Item objects with attrs[name, weight, importance]

    @property
    def backpack(self):
        return self._backpack

    @backpack.setter
    def backpack(self, backpack):
        if type(backpack) != int or backpack <= 0:
            raise ValueError('Backpack capacity can not be 0 or less')
        else:
            self._backpack = backpack

    @classmethod
    def items_fill(self, items):
        items.add(self)

    def best_fillment(self, items):
        checked_items = ()
        best_items = []
        curr_count = 0
        item = self.best_item(items, checked_items)

        while self.backpack != curr_count:
            checked_items.add(item)
            best_items.append(item)
            curr_count += 1
            item = self.best_item(items, checked_items)

        return best_items
            

    @classmethod
    def best_item(self, items, checked_items):
        lowest_weight = float('inf')
        highest_importance = 0
        best = None

        for item in items:
            item_weight = item.weight
            item_importance = item.importance
            if item_weight < lowest_weight and item_importance > highest_importance and item not in checked_items:
                lowest_weight = item_weight
                highest_importance = item_importance
                best = item

        return best
    
if __name__ == '__main__':

    bck = Backpack(6)

    itm1 = Item('water', 3, 10)
    itm2 = Item('book', 1, 3)
    itm3 = Item('food', 2, 9)
    itm4 = Item('jacket', 2, 5)
    itm5 = Item('camera', 1, 6)

    bck.items_fill(itm1)
    bck.items_fill(itm2)
    bck.items_fill(itm3)
    bck.items_fill(itm4)
    bck.items_fill(itm5)

    print(bck.best_fillment())

