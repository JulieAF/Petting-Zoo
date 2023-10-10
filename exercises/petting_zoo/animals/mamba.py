from datetime import date
from movements import Slithering
from .animal import Animal


class Mamba(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        print(f'{self.name} was fed {self.food} on {
              date.today().strftime("%m/%d/%Y")} after a nap')

    def __str__(self):
        return f"{self.name} the {self.species}"
