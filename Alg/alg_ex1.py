from random import randint, choice

class Random:
    
    def __init__(self):
        self.fill_list()
        self.guess_num = choice(self.num_list)

    def fill_list(self):
        self.num_list = []
        for _ in range(30):
            self.num_list.append(randint(1, 800))
        self.num_list.sort()

    @staticmethod
    def find_num(arr, num):
        counter = 0
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = arr[mid]
            if guess == num:
                return mid, counter
            if guess > num:
                counter += 1
                high = mid - 1
            else:
                counter += 1
                low = mid + 1
        return guess, counter
    
if __name__ == '__main__':
    init = Random()
    res = init.find_num(init.num_list, init.guess_num)
    print(f'Число {res[0]} угадано за {res[1]} итераций') 