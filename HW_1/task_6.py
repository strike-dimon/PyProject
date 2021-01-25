a = int(input())
b = int(input())
i = 1
if a > 0 and b > 0:
    while a <= b:
        a = (((a / 100) * 10) + a)
        i += 1
    print(i)

else:
    print('количество км должно быть больше нуля')
