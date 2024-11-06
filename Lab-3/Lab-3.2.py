# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    participants1 = set(participants_first_group.split(delimiter))
    participants2 = set(participants_second_group.split(delimiter))
    common_participants = participants1.intersection(participants2)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)

