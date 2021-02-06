import re

'''
 Создать текстовый файл (не программно), сохранить в нем несколько строк,
  выполнить подсчет количества строк, количества слов в каждой строке.
'''
lines = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labor",
         "uis aute irure dolor in reprehenderit",
         "xcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia"]
with open(r'txt_file_task_2.txt', "w", encoding="utf-8") as new_file:
    new_file.writelines("%s\n" % line for line in lines)

count = 0
with open(r"txt_file_task_2.txt", "r") as file:
    for line in file:
        count += 1
        res = len(re.findall(r'\w+', line))
        print(f'В {count} строке {res} слов')
    print(f'Количество строк- {count}')
