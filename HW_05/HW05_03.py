"""Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."""

with open("salary.txt") as f:
    worker_list = [worker_line.split() for worker_line in f.readlines()]
    
workers_info = [ 
    {"name": worker[0], "salary": float(worker[1])}
    for worker in worker_list
    if len(worker) > 1    
]

for worker in workers_info:
    if worker["salary"] < 20000:
        print(worker['name'])
