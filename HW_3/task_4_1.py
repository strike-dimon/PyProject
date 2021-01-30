def my_func_1():
    x = float(input('Введите положительное действительное число'))
    y = int(input('Введите целое отрицательное число:'))
    result = float(pow(x, y))
    print(round(result, 4))
    return


my_func_1()
