from movements import Walking, Swimming
from .animal import Animal


class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def honk(self):
        print("The goose honks. A lot")

    def run(self):
        print(f'{self} waddles')

    def __str__(self):
        return f"{self.name} the {self.species}"
