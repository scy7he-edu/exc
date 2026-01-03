from random import randint, choice, shuffle

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'
user_choice = '1 - Да. 0 - Нет.'
errormsg = f'Введи корректный ответ {user_choice}'

class pw:

    contain_digits = False
    contain_lowercase = False
    contain_uppercase = False
    contain_punctuation = False
    password_len = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def generator(self):
        chars = ''
        self.password_len = randint(20, 50)
        while len(chars) < self.password_len:
            if self.contain_digits:
                chars += choice(digits)
            if self.contain_lowercase:
                chars += choice(lowercase_letters)
            if self.contain_punctuation:
                chars += choice(punctuation)
            if self.contain_uppercase:
                chars += choice(uppercase_letters)
        
        char_list = []
        for elem in chars:
            char_list.append(elem)
        shuffle(char_list)
        chars = ''
        chars = ''.join(char_list)
        return chars
    
    

print('Привет! Это генератор паролей. Ответь на вопросы ниже, чтобы настроить генерацию.')

c_d = input(f'Использовать цифры? {user_choice}: ')
while True:
    if c_d == '1' or c_d == '0':
        if c_d == '1':
            pw.contain_digits = True
            break
        else:
            break
    else:
        print(errormsg)
        c_d = input(f'Использовать цифры? {user_choice}: ')

c_l = input(f'Использовать буквы нижнего регистра? {user_choice}: ')
while True:
    if c_l == '1' or c_l == '0':
        if c_l == '1':
            pw.contain_lowercase = True
            break
        else:
            break
    else:
        print(errormsg)
        c_l = input(f'Использовать буквы нижнего регистра? {user_choice}: ')

c_u = input(f'Использовать буквы верхнего регистра? {user_choice}: ')
while True:
    if c_u == '1' or c_u == '0':
        if c_u == '1':
            pw.contain_uppercase = True
            break
        else:
            break
    else:
        print(errormsg)
        c_u = input(f'Использовать буквы верхнего регистра? {user_choice}: ')

c_p = input(f'Использовать специальные символы? {user_choice}: ')
while True:
    if c_p == '1' or c_p == '0':
        if c_p == '1':
            pw.contain_punctuation = True
            break
        else:
            break
    else:
        print(errormsg)
        c_p = input(f'Использовать специальные символы? {user_choice}: ')

password = pw()
print(password.generator())