class Car:
    """Создаем машину"""

    def __init__(self, model, year_of_issue, engine_capacity, price, mileage):
        self.model = model
        self.year_of_issue = year_of_issue
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = 4

    def description(self):
        """Получение описания машины"""
        description = (f'Модель машины {self.model}, она {self.year_of_issue} года выпуска, у неё объём двигателя'
                       f' {self.engine_capacity} л/с, стоит такая машина {self.price} с пробегом {self.mileage}'
                       f' и у нее {self.number_of_wheels} колес')
        return description


"""Создали 1 экземпляр класса"""
car = Car('Kia', 2021, 199, 4099000, 36102)
print(car.description())


class Truck(Car):
    """Создаем класс наследник грузовик"""

    def __init__(self, model, year_of_issue, engine_capacity, price, mileage):
        super().__init__(model, year_of_issue, engine_capacity, price, mileage)
        self.number_of_wheels = 8

    def description_truck(self):
        """Получение описания грузовика"""
        description = (f'Модель машины {self.model}, она {self.year_of_issue} года выпуска, у неё объём двигателя'
                       f' {self.engine_capacity} л/с, стоит такая машина {self.price} с пробегом {self.mileage}'
                       f' и у нее {self.number_of_wheels} колес')
        return description


truck = Truck('Jac', 2015, 2.6, 3400000, 280000)
print(truck.description_truck())
