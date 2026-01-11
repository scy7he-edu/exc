class BackpackItem:

    def __init__(self, name: str, weight: int, importance: int):

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
        self._name = name

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def importance(self):
        return self._importance
    
    @importance.setter
    def importance(self, importance):
        self._importance = importance

class Backpack:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items_list = []

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
        
    def add_item(self, item_object: BackpackItem):
        self.items_list.append(item_object)

    def find_best_fillment(self):
        grid = [[0 for column in range(self.capacity + 1)] for rows in range(len(self.items_list) + 1)]
        for row in range(1, len(grid)):
            item = self.items_list[row - 1]
            for column in range(self.capacity + 1):
                nonfit = grid[row - 1][column]
                if item.weight > column:
                    fit = 0
                else:
                    fit = item.importance + grid[row - 1][column - item.weight]

                grid[row][column] = max(nonfit, fit)

        return grid
    
    def convert_to_names(self, grid):
        row = len(grid) - 1
        column = len(grid[0]) - 1
        items_list = []

        while row > 0 and column > 0:
            if grid[row][column] != grid[row - 1][column]:
                items_list.append(self.items_list[row-1].name)
                column -= self.items_list[row - 1].weight
            row -= 1

        items = ', '.join(items_list)
        return items


# manual item test (book items test)
   
itm1 = BackpackItem('water', 3, 10)
itm2 = BackpackItem('food', 2, 9)
itm3 = BackpackItem('jacket', 2, 5)
itm4 = BackpackItem('book', 1, 3)
itm5 = BackpackItem('camera', 1, 6)

bck = Backpack(6)
bck.add_item(itm1)
bck.add_item(itm2)
bck.add_item(itm3)
bck.add_item(itm4)
bck.add_item(itm5)
best_fillment = bck.find_best_fillment()
print(f'Наилучшее наполнение для рюкзака вместимостью {bck.capacity} фунтов - > {bck.convert_to_names(best_fillment)}')


# ---randomized test---
# ---сам написал :)----

from string import ascii_letters
from random import randint, choice
if __name__ == '__main__':

# ---generating item names---
    names = []
    for i in range(randint(5, 51)):
        names.append(choice(ascii_letters))
    
# ---generating backpack, items and testing---
    bck = Backpack(randint(1, 10))
    for i in range(len(names)):
        i = BackpackItem(choice(names), randint(1, 11), randint(1, 10))
        bck.add_item(i)
    
    best_fillment = bck.find_best_fillment()
    print(f'Наилучшее наполнение для рюкзака вместимостью {bck.capacity} фунтов - > {bck.convert_to_names(best_fillment)}')