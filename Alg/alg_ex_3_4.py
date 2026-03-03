# рекурсия 5
class KeyFinder:
    def __init__(self, box):
        self.box = box

    def find_key(self, key, box=None):
        if box is None:
            box = self.box

        if len(box) == 0:
            return False
        
        first_elem = box[0]
        rest_elem = box[1:]
        if first_elem == key:
            return True
        else:
            return self.find_key(key, rest_elem)

if __name__ == '__main__':
    box = [10, 20, 30, 7]
    key = 25
    finder = KeyFinder(box)
    print(finder.find_key(key))
