from time import sleep

"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод
"""


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        while True:
            for i in self.__color:
                if i == 'Red':
                    print(("\033[7m\033[31m {}".format(self.__color[0])))
                    sleep(7)
                elif i == 'Yellow':
                    print(("\033[5m\033[33m {}".format(self.__color[1])))
                    sleep(2)
                elif i == 'Green':
                    print(("\033[32m {}".format(self.__color[2])))
                    sleep(5)


TL_num_1 = TrafficLight()
TL_num_1.running()
