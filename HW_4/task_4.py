"""
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

list_inp = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

list_out = []
result = [x for x in list_inp if list_inp.count(x) == 1]
print(result)
