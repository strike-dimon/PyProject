seasons = int(input("Введите месяц в виде целого числа для определения сезона:"))
list_winter = (1, 2, 12)
list_spring = (3, 4, 5)
list_summer = (6, 7, 8)
list_fall = (9, 10, 11)
if seasons in list_winter:
    print('зима')
elif seasons in list_spring:
        print('весна')
elif seasons in list_summer:
        print('лето')
elif seasons in list_fall:
        print('осень')
