import random


def shows_random_num() -> int:
    '''Выдает случайное трехзначное число'''
    random_num = []
    for num in range(3):
        num = str(random.randint(0, 9))
        random_num.append(num)
    return ''.join(random_num)


print(shows_random_num())
