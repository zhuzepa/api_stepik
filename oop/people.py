class Person():
    """Создаем человек"""

    def __init__(self, name, age, height, weight):
        """Инициализируем атрубуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def description_person(self):
        """Получения описания человека"""
        description = f'{self.name} ему {self.age} месяца / лет, его рост {self.height} см и его вес {self.weight} кг'
        print(f'Нового человека зовут {description}')


one_people = Person('Диана', 3, 62, 5.7000)

two_people = Person('Даша', 25, 178, 57)

one_people.description_person()
two_people.description_person()