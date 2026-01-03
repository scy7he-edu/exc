#числовая угадайка
from random import randint

num = randint(1, 101)
usernum = ''

print('Добро пожаловать в числовую угадайку!')

def is_valid(usernum):
    return usernum.isdigit() and 1 <= int(usernum) <= 100

while True:
    usernum = input("Введите целое число от 1 до 100: ")
    if not is_valid(usernum):
        print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        if int(usernum) < num:
            print('Ваше число меньше загаданного, попробуйте еще раз.')
        elif int(usernum) > num:
            print('Ваше число больше загаданного, попробуйте еще раз.')
        elif int(usernum) == num:
            print('Вы угадали, поздравляем!')
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')