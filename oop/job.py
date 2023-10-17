class QaSpecialist():
    def __init__(self, name, level, age):
        self.name = name
        self.level = level
        self.age = age
        print('Cпециалист записан на собеседование')

    def testing(self):
        print(f'{self.name}, {self.level}, {self.age} лет выполняет тестовое задание')

    def done(self):
        print(f'{self.name}, {self.level}, {self.age} лет  успешно прошел тестовое задание')


    def linkedin(self):
        print(f'{self.name}, {self.level}, {self.age} появился новый специалист на сайте')




test = QaSpecialist('Алексей', 'Senior', 32)


test.testing()
test.done()
print()
test_lin = QaSpecialist('Дарья', 'middle', 26)
test_lin.linkedin()