"""
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]..
Результат: [12, 44, 4, 10, 78, 123]

"""

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [i for n, i in enumerate(my_list[1:]) if i > my_list[n]]

print(my_list)
print(new_list)
