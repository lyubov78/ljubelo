import json


FILENAME = 'input.json'


def task() -> float:
    '''Считает сумму произведений двух значений в каждом словаре'''
    with open(FILENAME, 'r') as f:
        json_data = json.load(f)
        total = []
        for num in json_data:
            mlp = num['score'] * num['weight']
            total.append(mlp)
        result = sum(total)
    return round(result, 3)


print(task())
