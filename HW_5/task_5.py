from random import randint
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open ('text_5.txt', 'w', encoding='utf-8') as random_el_in_file:
    init_list = [randint(1,101) for n in range(102)]
    random_el_in_file.write("".join(map(str, init_list)))
    print(sum(init_list))