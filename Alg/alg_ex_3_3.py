# рекурсия 4
class MaxFinder:
    def __init__(self, items):
        self.items = items

    def find_max(self, items=None):
        if items is None:
            items = self.items

        if len(items) == 1:
            return items[0]

        first_num = items[0]
        rest_nums = items[1:]
        sub_max = self.find_max(rest_nums)

        if first_num > sub_max:
            return first_num
        else:
            return sub_max

if __name__ == '__main__':
    mylist = [1, 10, 3, 5]
    finder = MaxFinder(mylist)
    print(finder.find_max())