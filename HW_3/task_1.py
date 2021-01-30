def division_two_arg(val_1, val_2):
    while True:
        try:
            result = val_1 / val_2
            print(round(result, 3))
            break
        except ZeroDivisionError:
            print('Деление на 0 запрещено')
            val_2 = int(input('Введите второе число'))
            continue
    return


division_two_arg(int(input('Введите первое число')), int(input('Введите второе число')))
