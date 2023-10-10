from . import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def display(self):
        print(f"{self.attraction_name} is where you'll find {
              self.description}, like")
        for animal in self.animals:
            print(f" * {animal}")

    @property
    def last_critter_added(self):
        return self.animals[-1] if self.animals else None
