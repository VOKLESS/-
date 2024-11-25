# TODO Напишите функцию find_common_participants
import re


def find_common_participants(a,b,separator = ","):

    clear_group_1 = re.sub(r"[|&;/.?+#=-]",separator,a)
    clear_group_2 = re.sub(r"[|&;/.?+#=-]", separator, b)

    common_group_1 = set(clear_group_1.split(separator))
    common_group_2 = set(clear_group_2.split(separator))
    return sorted(list(common_group_1 & common_group_2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group,";"))

