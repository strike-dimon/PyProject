proceeds = float(input("Введите сумму выручки"))
costs = float(input("Введите сумму издержек"))

if proceeds > costs:
    a = proceeds - costs
    print(f"Ваша прибыль за год составила +{a:.2f}")
    profit = (proceeds - costs) / proceeds
    print(f"Рентабельность выручки составляет {profit} %")
    staff = int(input("Введите количество сотрудников"))
    print(f"Прибыль фирмы из расчета на одного сотрудника {a / staff}")

elif costs == proceeds:
    print("фирма работает в ноль")

else:
    print(f"Ваш убыток за год составил -{costs - proceeds:.2f}")
