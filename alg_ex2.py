# сортировка выбором
import random
unsortedlist = []
for i in range (15):
    unsortedlist.append(random.randint(1,50))
print ('Неотсортированный список:', unsortedlist)
def Findsmallest(unsortedlist):
    smallestnum = unsortedlist[0]
    smallestindex = 0
    for i in range (1, len(unsortedlist)):
        if unsortedlist[i] < smallestnum:
            smallestnum = unsortedlist[i]
            smallestindex = i
    return smallestindex, smallestnum
s_index, s_num = Findsmallest(unsortedlist)
print(f'Наименьшее значение: {s_num}. Его индекс: {s_index}')
def sortselection(unsortedlist):
    sortedlist = []
    for i in range (len(unsortedlist)):
        smallest = Findsmallest(unsortedlist)[0]
        pop_elem = unsortedlist.pop(smallest)
        sortedlist.append(pop_elem)
    return sortedlist
s_list = sortselection(unsortedlist)
print(f'отсортированный список: {s_list}')
