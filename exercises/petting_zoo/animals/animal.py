from datetime import date


class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_num = chip_num
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {
              date.today().strftime("%m/%d/%Y")}')

    @property
    def chip_num(self):
        return self.__chip_num

    @chip_num.setter
    def chip_num(self, number):
        if self.__chip_num is None:
            self.__chip_num = number
