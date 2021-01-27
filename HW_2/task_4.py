text = input('Введите текст')
list_text = text.split()
list_x = []
for n in list_text:
    a = n[:10]
    list_x.append(a)
for i in enumerate(list_x, 1):
    print(i)

