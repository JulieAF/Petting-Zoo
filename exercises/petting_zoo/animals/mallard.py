from datetime import date
from movements import Walking, Swimming
from .animal import Animal


class Mallard(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def feed(self):
        print(f'{self.name} was fed {self.food} on {
              date.today().strftime("%m/%d/%Y")} after being bathed')

    def __str__(self):
        return f"{self.name} the {self.species}"
