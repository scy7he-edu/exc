# Рекурсия (далась легко)
num = 20
def countdown(num):
    print(num, end = ' ')
    if num != 0:
        countdown(num - 1)
countdown(num)