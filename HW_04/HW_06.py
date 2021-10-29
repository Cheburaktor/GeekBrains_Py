# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

#Var1

print("*" * 20, "Var1")
start_iterator = 7

for el in count(start_iterator):
    if el > 10:
        break

    print(el)

# var2
print("*" * 20, "Var2")
cycling_list = [2, 5, 6, 8, 32, 140]
max_iteration = 12
iteration_count = 0

for el in cycle(cycling_list):
    print(el)
    iteration_count += 1
    
    if iteration_count >= max_iteration:
        break
