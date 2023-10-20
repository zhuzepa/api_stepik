class Person:
    """Создаем человека"""

    #  Атрибуты, созданные в __init__() называются атрибутами экземпляра
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 115

    def description_person(self):
        """Получение описание человека"""
        description = (f'{self.name} ему {self.age} лет, его рост {self.height} см и его вес {self.weight} кг')
        return description

    def get_weight(self):
        """Получение веса человека"""
        return (f'Вес человека: {self.weight}')

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg

class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты клааса родителя, а функция super() связывает родительский класс с потомком"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        return (f'Заряд ярости равен: {self.rage}')

    def description_person(self):
        """Переопределение метода родителя"""
        description = (f'{self.name} ему {self.age} лет, его заряд ярости {self.rage}')
        return description


class Wizard(Person):
    """Создаем класс волшебника"""

    def __init__(self, name, age, height, specializations, resource, weapon):
        super().__init__(name, age, height)
        self.name = name
        self.specializations = specializations
        self.resource = resource
        self.weapon = weapon

    def description_wizard(self):
        description = (f'Маг является {self.name}, ему {self.age} лет, его вес составляет {self.weight} кг, '
                       f' а также он владеет специализацией {self.specializations}'
                       f' для магий он использует ресурс такой как {self.resource} и владеет оружием {self.weapon} ')
        return description

wizard_elf = Wizard('Эльф крови', 34, 70, 'огонь', 'чародейский заряд', 'посох')
wizard_dreney = Wizard('Дреней', 222, 56, 'лёд', 'мана', 'жезл')

# print(wizard_elf.description_wizard())
# print(wizard_dreney.description_wizard())