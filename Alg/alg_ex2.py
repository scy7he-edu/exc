# сортировка выбором
import random

class SelectionSorter:

    def __init__(self, items=None):
        if items is None:
            self.items = [random.randint(1, 50) for _ in range(15)]
        else:
            self.items = list(items)

    @staticmethod
    def find_smallest(arr):
        smallest_num = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest_num:
                smallest_num = arr[i]
                smallest_index = i
        return smallest_index, smallest_num

    def sort(self):
        list_to_sort = self.items[:]
        sorted_list = []
        for _ in range(len(list_to_sort)):
            smallest_index, _ = self.find_smallest(list_to_sort)
            sorted_list.append(list_to_sort.pop(smallest_index))
        return sorted_list

if __name__ == '__main__':
    sorter = SelectionSorter()
    print('Неотсортированный список:', sorter.items)

    s_index, s_num = SelectionSorter.find_smallest(sorter.items)
    print(f'Наименьшее значение: {s_num}. Его индекс: {s_index}')

    s_list = sorter.sort()
    print(f'Отсортированный список: {s_list}')