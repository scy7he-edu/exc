#числовая угадайка
from random import randint

class GuessingGame:
    def __init__(self):
        self.secret_number = randint(1, 100)
        self.user_guess = None

    @staticmethod
    def is_valid(user_input):
        return user_input.isdigit() and 1 <= int(user_input) <= 100

    def play(self):
        print('Добро пожаловать в числовую угадайку!')
        while True:
            self.user_guess = input("Введите целое число от 1 до 100: ")
            if not self.is_valid(self.user_guess):
                print('А может быть все-таки введем целое число от 1 до 100?')
            else:
                guess = int(self.user_guess)
                if guess < self.secret_number:
                    print('Ваше число меньше загаданного, попробуйте еще раз.')
                elif guess > self.secret_number:
                    print('Ваше число больше загаданного, попробуйте еще раз.')
                else:
                    print('Вы угадали, поздравляем!')
                    break
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

if __name__ == '__main__':
    game = GuessingGame()
    game.play()