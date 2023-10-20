# экземпляр класса
class Dog:
    # Атрибут класса
    species = 'Canis familiaris'

    # Атрибуты, созданные в __init__() называются атрибутами экземпляра
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод экземпляра
    def description(self):
        print(f'{self.name} is {self.age} years old')

    # Метод экземпляра
    def speak(self, sound):
        print(f'{self.name} says {sound}')

bunny = Dog('Bunny', 23)
zeus = Dog('Zeus', 100)
jack = Dog("Jack", 3)
jim = Dog("Jim", 5)


class JackRussellTerrier(Dog):
    pass


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass

print(bunny.species)
print(bunny.name)
jim.speak('Woof')

print(type(bunny))