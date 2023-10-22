list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

total_players = len(list_players)
average = total_players // 2

first_team = list_players[:average]
second_team = list_players[average:]

print(first_team)
print(second_team)
