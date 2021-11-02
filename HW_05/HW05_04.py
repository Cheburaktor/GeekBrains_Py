"""Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

trans = {
    'One': 'Один'
    'Two': 'Два'
    'Three': 'Три'
    'Four' 'Четыре'

}

conv = []

with open('numbers') as data:
    for row in data:
        name, value = row.split(' - ')
        conv.append(f"{trans[name]} - {value}")
        
with open ("numbers", "w") as out_data:
    out_data.writelines(conv)

