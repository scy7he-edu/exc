# рекурсия 3
class ItemCounter:
    def __init__(self, items):
        self.items = items

    def count_items(self, items=None):
        if items is None:
            items = self.items
        
        if not items:
            return 0
        else:
            return 1 + self.count_items(items[1:])

if __name__ == '__main__':
    somearr = [15, 6, 25, 65, 77, 31]
    counter = ItemCounter(somearr)
    print(f'{counter.count_items()} элементов в массиве')