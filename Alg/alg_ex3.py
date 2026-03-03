# Рекурсия
class Countdown:
    def __init__(self, start_num):
        self.start_num = start_num

    def countdown(self, num=None):
        if num is None:
            num = self.start_num
        
        print(num, end=' ')
        if num != 0:
            self.countdown(num - 1)

if __name__ == '__main__':
    num = 20
    counter = Countdown(num)
    counter.countdown()