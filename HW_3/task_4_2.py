def my_func_2(x, y):
    
    if (x >= 0) and (y <= 0):
        suma_1 = 1
        i = -1
        while True:
            if y <= i:
                i -= 1
                suma_1 *= x
                continue
            else:
                return round(1 / suma_1, 4)
    else:
        return 'Введено неправильно число. Будьте внимательны!'


print(my_func_2(float(input('Введите положительное действительное число:')),
                int(input('Введите целое отрицательное число:'))))
