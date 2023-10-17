class Person:
    """Модель человека"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Человек создан')

    def sing(self):
        """Просим человека спеть"""
        print(f'{self.name} читает рэп')

    def dance(self):
        """Просим человека танцевать"""
        print(f'{self.name} танцует')

    def game(self):
        """"Просим человека играть"""
        print(f'{self.name} играет в доту')

    def food(self):
        """Кушает мороженное"""
        print(f'{self.name} кушает мороженное')

    def shamil(self):
        """Дает Шаме денег"""
        print(f'{self.name} даёт Шаме денег за хорошую работу')

    def petr(self):
        """Дает Петр денег"""
        print(f'{self.name} даёт Пете денег за хорошую работу')

    def dasha(self):
        print(f'{self.name} есть яблоки которые режет Даша')

man = Person('Alex', 30)

man.dasha()
man.dance()

women = Person('Dasha', 26)

women.dance()