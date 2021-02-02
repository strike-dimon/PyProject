from itertools import count, cycle


def count_num(x, y):
    for el in count(x):
        if el > y:
            break
        else:
            print(el)
    с = 0
    for el in cycle(["Lorem ipsum dolor sit amet"]):
        if с > y:
            break
        print(el)
        с += 1



count_num(x=int(input('Введите целое число')), y=int(input('Введите целое число')))
