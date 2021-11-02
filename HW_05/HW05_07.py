"""Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности,
выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл."""

import json

firms_data = []

with open("firms.txt") as input_data:
    firm_dict = {}
    profit_list = []

    for firm_row in input_data:
        name, form, revenue, costs = firm_row.split()

        profit = float(revenue) - float(costs)
        firm_dict[name] = profit

        if profit:
            profit_list.append(profit)

    firms_data.append(firm_dict)
    firms_data.append({
        "avg_profit": round(sum(profit_list) / len(profit_list), 2)
    })

with open("firms.txt", "w") as output_data:
    json.dump(firms_data, output_data)
