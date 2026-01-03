# рекурсия 3...
somearr = [15, 6, 25, 65, 77, 31]
def count_items(somearr):
    if somearr == []:
        return 0
    else:
        return 1 + count_items(somearr[1:])
print(f'{count_items(somearr)} элементов в массиве')