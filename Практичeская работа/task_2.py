from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке


for i in counts:
    '''Считает количество выпаданий орлов и решек'''
    eagle = 0
    tails = 0

    for j in range(i):
        side = choice(coin)
        if side == EAGLE:
            eagle += 1
        else:
            tails += 1


frequency = min(eagle, tails) / max(eagle, tails)
list_freq.append(frequency)

print(list_freq)
