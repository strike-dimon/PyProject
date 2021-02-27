from abc import ABC, abstractclassmethod

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property.
 """


class Clothes:
    result = 0

    def __init__(self, value):
        self.value = value

    @property
    @abstractclassmethod
    def consuption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consuption + other.consuption
        return Suit(0)

    def __str__(self):
        return f"{Clothes.result}"


class Coat(Clothes):
    @property
    def consuption(self):
        return round(self.value / 6.5) + 0.5


class Suit(Clothes):
    @property
    def consuption(self):
        return round((2 * self.value + 0.3) / 100)


coat = Coat(48)
suit = Suit(175)
print(coat + suit + coat)
