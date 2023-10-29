# TODO Напишите функцию find_common_participants

def find_common_participants(group_1, group_2, separator=','):
    spisok_1 = set(group_1.replace(separator, ' ').split())
    spisok_2 = set(group_2.replace(separator, ' ').split())
    result = spisok_1.intersection(spisok_2)
    return sorted(result)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(list(find_common_participants(participants_first_group, participants_second_group, '|')))
