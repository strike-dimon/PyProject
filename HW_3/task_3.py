def sum_two_max(a, b, c):
    list_1 = [a, b, c]
    first_max = max(list_1)
    list_1.remove(first_max)
    second_max = max(list_1)
    result = first_max + second_max
    print(result)


sum_two_max(int(input('Введите число')), int(input('Введите число')), int(input('Введите число')))
