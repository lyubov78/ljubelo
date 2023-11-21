import os
import time


maps = [i for i in range(1, 10)]


victories = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)


def print_maps():
    print('—' * 13)
    for i in range(3):
        print(f'| {maps[0 + i * 3]} | {maps[1 + i * 3]} | {maps[2 + i * 3]} |')
        print('—' * 13)


def step_in_map(n, symbol):
    ind = maps.index(n)
    maps[ind] = symbol


def get_result():
    s = ''
    for line in victories:
        if maps[line[0]] == 'X' and maps[line[1]] == 'X' and maps[line[2]] == 'X':
            s = 'X'
        if maps[line[0]] == 'O' and maps[line[1]] == 'O' and maps[line[2]] == 'O':
            s = 'O'
    return s


def game():
    name_player_1 = input('Первый игрок, введите Ваше имя: ')
    name_player_2 = input('Второй игрок, введите Ваше имя: ')
    os.system('cls')
    play = True
    count = 0
    while True:
        count += 1
        print_maps()
        if play:
            number = input((f'Ваш ход, {name_player_1}: '))
            time.sleep(0.5)
            step_in_map(int(number), 'X')
            os.system('cls')
            play = False
        else:
            number = input(f'Ваш ход, {name_player_2}: ')
            time.sleep(0.5)
            step_in_map(int(number), 'O')
            os.system('cls')
            play = True

        win = get_result()
        if win == 'X':
            print(f'{name_player_1}, Вы победили!!!')
            break
        elif win == 'O':
            print(f'{name_player_2}, Вы победили!!!')
            break
        elif count == 9:
            print('Ничья!!!')
            break
    print(f'Конец игры!\nИгра закроется через 5 секунд.')
    time.sleep(5)


print(game())
