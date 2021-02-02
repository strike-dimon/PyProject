from functools import reduce


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


list_int = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, list_int))
