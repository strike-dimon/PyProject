import re


def count_list():
    result_a = 0

    while True:
        input_str = input('Введите строку чисел:')
        if 'q' in input_str:
            input_str = re.sub(r'[A-Za-z!@#$%^&*()]', ' ', input_str)
            list_with_num = [int(i) for i in input_str.split()]
            result_b = sum(list_with_num)
            result_a += result_b
            print(result_a)
            break
        else:
            input_str = re.sub(r'[A-Za-z!@#$%^&*()]', ' ', input_str)
            list_with_num = [int(i) for i in input_str.split()]
            result_a += sum(list_with_num)
            print(result_a)
    return


count_list()
