import random


def get_unique_list_numbers() -> list[int]:
    '''Создает список случайных чисел в диапозоне от -10 до 10'''
    random_nums = set()
    for num in range(15):
        num = random.randint(-10, 10)
        random_nums.add(num)
    return list(random_nums)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
