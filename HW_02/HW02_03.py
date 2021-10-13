# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#Решение через dict:

seasons_dict = {
    "Зима": [12, 1, 2],
    "Весна": (3, 4, 5),
    "Лето": (6, 7, 8),
    "Осень": (9, 10, 11)
}

month_number = int(input("Введите номер месяца: "))

if 0 < month_number <= 12:
    for key in seasons_dict.keys():
        if month_number in seasons_dict[key]:
            print(key)
else:
    print ("Incorrect")

# Решение через list

seasons_list = [
    ["Зима", [12, 1, 2]],
    ["Весна", [3, 4, 5]],
    ["Лето", [6, 7, 8]],
    ["Осень", [9, 10, 11]]
]

month_number = int(input("Введите номер месяца: "))

if 0 < month_number <= 12:
    for season, month in seasons_list:
        if month_number in month:
            print(season)
else:
    print ("Incorrect")