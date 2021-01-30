import re


def int_func():
    """
    Даная функция позволяет:
     * вывести на экран  введенный текст, в котором каждое слово с заглавной буквы
     * вывести на экран введеный текст, где каждое слово начинается с заглавной буквы
    Валидный шаблон для ввода текста: <laboris nisi ut aliquip ex ea commodo>
    Не валидный шаблон для ввода текста: <nice апв ъdfg giтьб ыфстzasd cool>.
    """

    while True:
        line = input('Введите текст:')
        d = re.sub(r'[А-я]', '', line)
        if d != line:
            print('Введите текст со строчными латинскими буквами')
            continue
        else:
            print(line.title())
            break

    return


int_func()
