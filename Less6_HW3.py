#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_full_profit(self):
        self.__income = {'Оклад': self.profit, 'Бонус': self.bonus}
        return self.__income

    def get_all_profit(self):
        self.all_prof = {"Общий доход в месяц",self.profit + self.bonus}
        return self.all_prof


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
position = input("Введите должность: ")
profit = int(input("Введите оклад: "))
bonus = int(input("Введите пермию: "))

manager = Position(name, surname, position, profit, bonus)
print(manager.get_full_name(), manager.get_full_profit(), manager.get_all_profit())