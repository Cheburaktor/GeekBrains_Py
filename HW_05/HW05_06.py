"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран."""


sub = {}

with open("lessons.txt") as file:
    for row in file:
        sub_info = row.split()
        name = sub_info[0].rstrip(":")
        sub[name] = sub_info[1:]

result = {}

for key, value in sub.items():
    result[key] = sum(
        [
            int(hours[:hours.index("(")])
            for hours in value
            if hours != "-"
        ]
    )

print(result)
