# TODO импортировать необходимые молули
import json
import csv
import collections


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    '''Конвертирует файл из формата CSV в формат JSON'''
    with open(INPUT_FILENAME, 'r') as f_i:
        csv_data = [lines for lines in csv.DictReader(f_i, delimiter=',', lineterminator='\n')]

    with open(OUTPUT_FILENAME, 'w') as f_o:
        json_data = json.dump(csv_data, f_o, indent=4)

    return json_data


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
