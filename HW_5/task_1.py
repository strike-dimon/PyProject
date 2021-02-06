"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_file = open(r'new_txt_file_task_1.txt', "r+", encoding="utf-8")
a = input('Введите текст:')
while a:
    new_file.writelines(a)
    b = new_file.tell()
    new_file.seek(b)
    new_file.write('\n')
    a = input('Введите текст:')

    if not a:
        break
content = new_file.readlines()
print(content)
new_file.close()
