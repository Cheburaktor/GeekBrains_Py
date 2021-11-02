"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randrange

rand_num = [randrange(1, 200) for _ in range(50)]

with open("num_02", "w") as output:
    output.write(" ".join((map(str, rand_num))))

with open ("num_02") as inp:
    numbers = inp.read().split()
    
    print(sum(int(x) for x in numbers))
