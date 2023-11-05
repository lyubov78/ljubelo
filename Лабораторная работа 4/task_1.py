from random import randint


def get_unique_list_numbers() -> list[int]:
    '''Создает список случайных чисел в диапозоне от -10 до 10'''
    random_nums = []
    while len(random_nums) < 15:
        x = randint(-10, 10)
        if x not in random_nums:
            random_nums.append(x)

    random_nums = set()
    while len(random_nums) < 15:
        random_nums.add(randint(-10, 10))

    return list(random_nums)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
