from random import choice

"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        def go(self):
            return f'{self.name} is started'

        def stop(self):
            return f'{self.name} is stopped'

        def turn_direction(self):
            direction = ['right', 'left', 'back', 'straight']
            direct = choice(direction)
            return f'{self.name} go to {direct}'

        def show_speed(self):
            return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

    def turn_direction(self):
        direction = ['right', 'left', 'back', 'straight']
        direct = choice(direction)
        return f'{self.name} go to {direct}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def stop(self):
        return f'{self.name} is stopped'

    def show_speed(self):
        print(f'Current speed of sport car {self.name} is {self.speed}')
        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for sport car'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'

    def turn_direction(self):
        direction = ['right', 'left', 'back', 'straight']
        direct = choice(direction)
        return f'{self.name} go to {direct}'

    def go(self):
        return f'{self.name} is started'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

    def show_speed(self):
        print(f'Current speed of police car {self.name} is {self.speed}')
        if self.speed > 60:
            return f'Speed of {self.name} is normal for police car'


Kamaz = TownCar(40, 'Grey', 'Kamaz', False)
maserati = SportCar(120, 'Purple', 'maserati', False)
gazel = WorkCar(80, 'White', 'gazel', False)
geely = PoliceCar(190, 'Black', 'geely', True)
print(gazel.turn_direction())
print(f'When {Kamaz.turn_direction()}, then {maserati.stop()}')
print(f'{gazel.go()} with speed exactly. {gazel.show_speed()}')
print(f'{gazel.name} is {gazel.color}')
print(f'Is {maserati.name} a police car? {maserati.is_police}')
print(f'Is {geely.name}  a police car? {geely.is_police}')
print(maserati.show_speed())
print(Kamaz.show_speed())
print(geely.police())
print(geely.show_speed())
