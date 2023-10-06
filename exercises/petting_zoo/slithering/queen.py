from datetime import date


class Queen:

    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
        self.chip_number = chip_num

    def feed(self):
        print(f'{self.name} was fed {self.food} on {
              date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} the {self.species}"

    @property
    def chip_num(self):
        return self.chip_num

    @serial_num.setter
    def serial_num(self, number):
        pass
