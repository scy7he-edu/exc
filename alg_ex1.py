#бинарный поиск
import random
nlist = [] # создал пустой массив для чисел
for _ in range(30): # цикл заполнения массива рандомными положительными числами от 1 до 800 в количестве 30шт.
    nlist.append(random.randint(1, 800))

# Ниже - аналогичный способ заполнения массива числами при помощи while

# while len(nlist) != 30:
    # nlist.append(random.randint(1, 800))

nlist.sort() # сортировка списка по возрастанию для имплементации алгоритма бинарного поиска
print('Массив чисел:', nlist)
rnum = random.choice(nlist) # рандомно выбираем число из списка
print ('Число для поиска:', rnum)
def Findnum(): # объявляю функцию поиска выбранного числа
    counter = 0
    low = 0
    high = len(nlist) - 1
    while low <= high:
        mid = (low + high)//2
        guess = nlist[mid]
        if guess == rnum:
            return mid, counter
        if guess > rnum:
            counter += 1
            high = mid - 1
        else:
            counter += 1
            low = mid + 1
    return guess, counter
gnum, iternum = Findnum()
print('Искомое число:', nlist[gnum], 'угадано за:', iternum, 'итераций')