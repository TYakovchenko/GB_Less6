#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

#Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начало движения'

    def stop(self):
        return f'{self.name} остановилась'

    def right(self):
        return f'{self.name} поворот направо'

    def left(self):
        return f'{self.name} поворот налево'

    def speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость составляет {self.speed}')
        if self.speed > 40:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} в допустимом интервале'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше нормы'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


car1 = SportCar(220, "Белая", "Ferrari", True)
car2 = TownCar(68, 'Черная', 'РАВ4', False)
car3 = WorkCar(90, 'Синяя', 'РЕНО', False)
car4 = PoliceCar(100, 'Оранжевая', 'БМВ', True)

print(car4.go())
print(car1.go())
print(car1.left())
print(car4.right())
print(car2.show_speed())
print(car3.show_speed())
print(car1.stop(), car2.stop(), car3.stop())