
class PettingZoo:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def display(self):
        print(f"{self.attraction_name} is where you'll find {
              self.description}, like")
        for animal in self.animals:
            print(f" * {animal}")
