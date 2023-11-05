import string
import random


all_elem = [string.ascii_uppercase, string.ascii_lowercase, string.digits]
valid_symb = list(''.join(all_elem))


def get_random_password() -> str:
    '''Генерирует случайный пароль из 8 символов'''
    password = random.sample(valid_symb, 8)
    return ''.join(password)


print(get_random_password())
