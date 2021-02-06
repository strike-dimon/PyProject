"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open(r'text_3.txt', "r", encoding="utf-8") as new_file:
    dict_em = {line.split()[0]: float(line.split()[1]) for line in new_file}
    awr = round(sum(dict_em.values()) / len(dict_em), 2)
    print('Средняя зарплата всех сотрудников =', awr)
    homless_em = [el[0] for el in dict_em.items() if el[1] < 20000]
    print('Список сотрудников с зп < 20 000 -', homless_em)
