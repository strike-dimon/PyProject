from sys import argv

hours, s_per_hour, bonus = argv[1], argv[2], argv[3]
a, b, c = float(hours), float(s_per_hour), float(bonus)
print((a * b) + c)
