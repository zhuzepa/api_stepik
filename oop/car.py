class CarCountry:  # создаем класса с любым названием
    def __init__(self, model, country, ):  # __init__ - создаем параметры для ввода данных, это конструктор
        self.model = model  # self - это ссылка на параметры (обязательно вначале добавляем)
        self.country = country
        print('Запись о машине создана, ожидаейте комментария')

    """После создания по конструктору по параметрам, создаем функционал, что будем оценивать? """

    def nice_car(self):
        print(f'{self.model}, {self.country} это хорошая машина')

    def bad_car(self):
        print(f'{self.model}, {self.country} это плохая машина')


# создаем переменную с название и класса и добавляем параметры
car_1 = CarCountry('Chery', 'China')

car_1.bad_car()

print()

car_2 = CarCountry('BMW', 'Deutschland')

car_2.nice_car()
