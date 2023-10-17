# Наследование классов
class Dogs:
    """Создаем собак"""

    def __init__(self, name, bred, color, delicacy, favorite_toy):
        self.name = name
        self.bred = bred
        self.color = color
        self.weight = 25
        self.delicacy = delicacy
        self.favorite_toy = favorite_toy

    def description_dog(self):
        """Получение описание собаки"""
        description = (
            f"{self.name}, породой {self.bred}, он имеет {self.color} цвет и его вес"
            f" {self.weight} кг, он любит {self.delicacy} и любимая игрушка это"
            f" {self.favorite_toy}"
        )
        print(f'Новую собачку зовут {description}')

    def get_weight(self):
        """Получение веса собаки"""
        print(f'Вес собаки: {self.weight}')

    def update_weight(self, kg):
        """Изменение веса собаки"""
        self.weight = kg


dog_one = Dogs('Дафна', 'Американский Булли', 'лилловый', 'кобаски', 'колечко')
dog_two = Dogs('Челки', 'Тойтерер', 'коричневый', 'перчик', 'мячик')
dog_three = Dogs('Джагер', 'Английский Бульдог', 'Тигровый', 'боченки', 'бутылка')

dog_two.update_weight(10)
dog_three.update_weight(27)
dog_one.description_dog()
dog_two.description_dog()
dog_three.description_dog()
