class ce:
    direction = ''
    shift = None
    lang = ''
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def work(self, text):
        current_shift = self.shift
        newtxt = ''
        if self.direction == 'left':
            current_shift = -self.shift
        for char in text:
            l_char = char.lower()

            if self.lang == 'ru':
                if l_char in ru_alph:
                    char_index = ru_alph.index(l_char)
                    new_index = (char_index + current_shift) % 32
                    new_char = ru_alph[new_index]
                    newtxt += new_char.upper() if char.isupper() else new_char
                else:
                    newtxt += char
            
            if self.lang == 'en':
                if l_char in eng_alph:
                    char_index = eng_alph.index(l_char)
                    new_index = (char_index + current_shift) % 26
                    new_char = eng_alph[new_index]
                    newtxt += new_char.upper() if char.isupper() else new_char
                else:
                    newtxt += char
        return newtxt

ru_alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alph = 'abcdefghijklmnopqrstuvwxyz'

print('введи сообщение, которое хочешь обработать')
msg = input()

dir_choice = input('введи направление "left" или "right": ').lower()
while True:
    if not (dir_choice == 'left' or dir_choice == 'right'):
        print('введи корректное направление. "left" или "right"')
        dir_choice = input().lower()
    else:
        if dir_choice == 'left':
            ce.direction = 'left'
            break
        else:
            ce.direction = 'right'
            break

shift_known = input('известен ли коэффициент сдвига? y/n: ')
shift_known = shift_known.lower()
if not (shift_known == 'y' or shift_known == 'n'):
    print('дай корректный ответ "y" или "n"')
    shift_known = input().lower()
else:
    if shift_known == 'y':
        shift_choice = input('введи коэффициент сдвига (только целое число): ')
        while True:
            if not shift_choice.isdigit():
                print('введи корректный коэффициент сдвига (только целое число)')
                shift_choice = input()
            else:
                ce.shift = int(shift_choice)
                break
    else:
        ce.shift = None

lang_choice = input('выбери язык "ru" или "en": ').lower()
while True:
    if not (lang_choice == 'ru' or lang_choice == 'en'):
        print('введи корректный выбор языка "ru" или "en"')
        lang_choice = input().lower()
    else:
        if lang_choice == 'ru':
            ce.lang = 'ru'
            break
        if lang_choice == 'en':
            ce.lang = 'en'
            break

enc = ce()

if ce.shift is not None:
    print(enc.work(msg))
else:
    limit = 32 if ce.lang == 'ru' else 26
    for i in range(limit):
        ce.shift = i
        print(f'сдвиг {i}: {enc.work(msg)}')
