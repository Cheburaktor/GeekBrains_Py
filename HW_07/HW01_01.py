"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица."""

class Matrix:
    value: list = []

    def __init__(self, value: list):
        self.value = value

    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            items_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(items_count)
                ]
                for row in range(rows_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Матрицы разного размера")
            exit(1)

    def __str__(self):
        return "\n".join(
            str(row).strip('[]'). replace(',', '')
            for row in self.value
        )

a = Matrix([
    [15, 16, 18],
    [19, 15, 16],
])

b = Matrix([
    [20, 21, 22],
    [26, 27, 28],
])

c = a + b
print(c)
