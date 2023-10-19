from base_person import Person, Wizard

man = Person('Федор', 50, 115)
print(man.description_person())


wizard = Wizard('Эльф крови', 34, 70, 'огонь', 'чародейский заряд', 'посох')
print(wizard.description_wizard())
