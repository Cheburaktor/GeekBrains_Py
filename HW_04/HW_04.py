# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

my_list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
items = [x for x in my_list if my_list.count(x) == 1]

print(items)
