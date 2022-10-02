class User:
    def __init__(self, first_name: str, last_name: str, nick_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.age = age

    def info(self):
        print(f'Имя: {self.first_name}\nФамилия: {self.last_name}\nНикнейм: {self.nick_name}\nВозраст: {self.age}')

    def add_age(self, num):
        self.age += num




user_1 = User('Вася', 'Залупкин', 'vasya1234', 25)
user_1.info()
user_1.add_age(5)
user_1.info()


class Car:
    def __init__(self, make, color, year):
        self.make = make
        self.color = color
        self.year = year

    def get_desription(self):
        print(f'Марка: {self.make}\nЦвет: {self.color}\nГод: {self.year}')


class ElectricCar(Car):
    def __init__(self, make, color, year, odometer, battery_size):
        super().__init__(make, color, year)
        self.odometer = odometer
        self.battery_size = battery_size

    def describe_battery(self):
        if self.battery_size <= 75:
            print(f'Запас хода: < 200km')
        else:
            print(f'Запас хода: > 200km')








my_car = Car('BMW', 'White', 2015)
my_car.get_desription()

my_electric_car = ElectricCar('Tesla', 'black',2019, 50000, 150)
my_electric_car.describe_battery()









