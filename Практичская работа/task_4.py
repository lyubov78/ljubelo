from typing import Any


def remove(data: list, item: Any) -> list:
    '''Удаляет самое последнее искомое значение'''
    if item not in data:
        raise ValueError('Элемент не найден')

    index_iteam = 0
    for i, value in enumerate(data):
        if value == item:
            index_iteam = i
    return data[:index_iteam] + data[index_iteam + 1:]


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
