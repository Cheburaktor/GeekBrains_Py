# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

a = int(input("Введите первый аргумент>>> "))
b = int(input("Введите второй аргумент>>> "))
c = int(input("Введите третий аргумент>>> "))

print(f"Сумма двух наибольших аргументов - {my_func(a, b, c)}")
