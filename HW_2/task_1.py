my_list = [2, 4.5, 5 + 6j, 'text', [1, 'gsdf'], (1, 2, 3), {'a', 'k', 'b', 'd', 'r'}, {'key': '12', 'key': 'text'},
           False, (bytes('text', encoding='utf-8')), (bytes([10, 20, 30, 40])), None]
for n in my_list:
    print(type(n))
