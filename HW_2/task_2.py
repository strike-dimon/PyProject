my_list = list(input())
a = len(my_list)
for i in range(1, a, 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)
