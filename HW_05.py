# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input("Введите значение выручки: "))
costs = float(input("Введите значение издержек: "))
if revenue > costs:
    print("Поздравляем! Вы работаете в прибыль! Ваша фирма процветает!")
    profit = ((revenue - costs) / revenue) * 100
    print("Рентабельность вашего бизнеса составляет: ", profit, "%")
    num_staff = int(input("Введите количество сотрудников: "))
    profit_staff = (revenue - costs) / num_staff
    print("Прибыль в расчете на одного сотрудника составляет: ", profit_staff)
else:
    print("Сожалеем, ваша фирма терпит убытки. Нужно что-то менять!")
