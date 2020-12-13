#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#Например: длина 20м * ширина5000м * вес 25кг *  толщина 5см = 12500 т

userweight = int(input("введите вес"))
userdepth = int(input("введите толщину"))
userlength = int(input("введите длину"))
userwidth = int(input("введите ширину"))
class Road:
    __length = None
    __width = None
    weigth = None
    depth = None

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def intake(self):
        self.weigth = userweight
        self.depth = userdepth
        intake = self.length * self.width * self.weigth * self.depth / 1000
        print(f'Необходимо {intake} ')


road_to_village = Road(userlength, userwidth)
road_to_village.intake()