from datetime import date
from movements import Walking
from .animal import Animal


class Llama(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        print(f'on {date.today()}, {
              self.name} had "Rockytop" sung to it so it would eat its {self.food}')

    def __str__(self):
        return f"{self.name} the {self.species}"
