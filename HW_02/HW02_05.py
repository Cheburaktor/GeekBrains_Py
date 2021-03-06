# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют
# элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

number = int(input("Enter your number: "))
ex_numbers = [20, 18, 9, 7, 6]
c = ex_numbers.count(number)

for element in ex_numbers:
    if c > 0:
        i = ex_numbers.index(number)
        ex_numbers.insert(i + 1, number)
        break

    else:
        if number > element:
            n = ex_numbers.index(element)
            ex_numbers.insert(n, number)
            break
        elif number < ex_numbers[len(ex_numbers) - 1]:
            ex_numbers.append(number)
            break

print(ex_numbers)
