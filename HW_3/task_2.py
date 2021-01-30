def contacts(name, surname, date, city, email, tel):
    my_list = [name, surname, date, city, email, tel]
    print(('|'.join(my_list)))
    return


contacts(name=input('Введите имя:'), surname=input('Введите фамилию:'), date=(input('Введите год рождения:')),
         city=input('Введите город проживания:'), email=input('Введите город email:'),
         tel=(input('Введите телефон:')))
