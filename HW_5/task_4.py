from googletrans import Translator

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open(r'new_text_4.txt', "w", encoding="utf-8") as new_file:
    with open("text_4.txt", 'r', encoding='utf-8') as old_file:
        text = old_file.read()
        new_file.write(Translator().translate(text, dest='ru').text)
        print("Текст переведен!")
