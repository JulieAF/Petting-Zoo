from movements import Walking, Swimming
from .animal import Animal


class Frog(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def run(self):
        print(f'{self} hops')

    def __str__(self):
        return f"{self.name} the {self.species}"
