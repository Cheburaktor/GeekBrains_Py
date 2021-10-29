# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

numbers = [15, 2, 3, 1, 7, 5, 4, 10]
result_list = [
    val for idx, val in enumerate(numbers)
    if idx > 0 and numbers[idx - 1] < val
]

print(result_list)
