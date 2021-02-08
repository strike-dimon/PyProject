"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров)
 """


class Worker:
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'Developer'
    _income = {"wage": float(1500), "bonus": float(350)}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def _get_total_income(self):
        result = sum(self._income.values())
        print(result)


ivanov = Position()
ivanov.get_full_name()
ivanov._get_total_income()
