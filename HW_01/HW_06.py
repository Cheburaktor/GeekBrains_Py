# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = float(input("Введите количество километров, преодоленных в первый день: "))
b = float(input("Введите целевое количество километров: "))
day = 1
while a < b:
    a *= 1.1
    day += 1
    print("В {} день: {}".format(day, (round(a, 2))))

print("Вы достигнете цели на {} день, если будете усердно заниматься ".format(day))
