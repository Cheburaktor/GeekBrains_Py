# 3. Узнайте у пользователя число n. Найдите сумму чисел
# n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n0 = int(input("Введите целое число: "))
n1 = int(str(n0) + str(n0))
n2 = int(str(n0) + str(n0) + str(n0))
sum = n0 + n1 + n2
print(sum)