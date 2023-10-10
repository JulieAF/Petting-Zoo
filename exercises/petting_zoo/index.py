from animals import Goose
from animals import Cow, Horse, Goat, Donkey, Llama, Frog, Turtle, Goldfish, Water_Bug, Mallard, Anaconda, Mamba, Boa, Blind, Queen, Goose
from attractions import SnakePit, WetLands, PettingZoo

annie = Anaconda("Annie", "snake", "mole-rat", "18205")

missy = Mamba("Missy", "snake", "rats", "02847")
print(missy.feed())

dee = Boa("Dee", "snake", "eggs", "89256")
print(dee.feed())
tess = Blind("Tess", "snake", "mice", "49172")

rose = Queen("Rose", "snake", "murids", "83051")

mabel = Cow("Mabel", "cow", "morning", "grass", "93811")
print(f'{mabel.name} the {mabel.species} is available to pet during the {
      mabel.shift} shift.')

jack_azz = Donkey("Jack", "donkey", "midday", "oats", "14550")
print(f'{jack_azz.name} the {jack_azz.species} is available to pet during the {
      jack_azz.shift} shift.')

billy = Goat("Billy", "goat", "morning", "tin", "21156")
print(f'{billy.name} the {billy.species} is available to pet during the {
      billy.shift} shift.')

hank = Horse("Hank", "horse", "afternoon", "hay", "44655")
print(f'{hank.name} the {hank.species} is available to pet during the {
      hank.shift} shift.')

miss_fuzz = Llama("Miss Fuzz", "domestic llama",
                  "afternoon", "Llama Chow", "98815")
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {
      miss_fuzz.shift} shift.')
print(miss_fuzz.feed())

gilly = Goose("Gilly", "Canada goose", "watercress sandwiches", "26719")
gilly.run()
gilly.swim()

todd = Frog("Todd", "frog", "flies", "99448")

gina = Goldfish("Gina", "fish", "kelp", "12363")

mitch = Mallard("Mitch", "duck", "bread", "23876")
print(mitch.feed())

ham = Turtle("Ham", "turtle", "lettuce", "97311")

ken = Water_Bug("Ken", "bug", "gnats", "33551")

varmint_village = PettingZoo(
    "Varmint Village", "cute and fuzzy critters to cuddle")
varmint_village.add_animal(mabel)
varmint_village.add_animal(hank)
varmint_village.add_animal(billy)
varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(jack_azz)
varmint_village.display()

slither_inn = SnakePit("Slither Inn", "more serpents than Indiana Jones")
slither_inn.add_animal(annie)
slither_inn.add_animal(missy)
slither_inn.add_animal(dee)
slither_inn.add_animal(tess)
slither_inn.add_animal(rose)
slither_inn.display()

critter_cove = WetLands("Critter Cove", "aquatic creatures")
critter_cove.add_animal(ken)
critter_cove.add_animal(mitch)
critter_cove.add_animal(gina)
critter_cove.add_animal(todd)
critter_cove.add_animal(ham)
critter_cove.display()
