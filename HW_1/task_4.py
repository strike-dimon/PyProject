num = int(input("Please input number"))
i = -1
while num >= 9:
    a = num % 10
    num //= 10
    if a > i:
        i = a
print(i)
