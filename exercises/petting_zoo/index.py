from walking import Cow, Horse, Goat, Donkey, Llama
from swimming import Frog, Turtle, Goldfish, Water_Bug, Mallard
from slithering import Anaconda, Mamba, Boa, Blind, Queen
from attractions import SnakePit, WetLands, PettingZoo

annie = Anaconda("Annie", "snake", "mole-rat")

missy = Mamba("Missy", "snake", "rats")

dee = Boa("Dee", "snake", "eggs")

tess = Blind("Tess", "snake", "mice")

rose = Queen("Rose", "snake", "murids")

mabel = Cow("Mabel", "cow", "morning", "grass")
print(f'{mabel.name} the {mabel.species} is available to pet during the {
      mabel.shift} shift.')

jack_azz = Donkey("Jack", "donkey", "midday", "oats")
print(f'{jack_azz.name} the {jack_azz.species} is available to pet during the {
      jack_azz.shift} shift.')

billy = Goat("Billy", "goat", "morning", "tin")
print(f'{billy.name} the {billy.species} is available to pet during the {
      billy.shift} shift.')

hank = Horse("Hank", "horse", "afternoon", "hay")
print(f'{hank.name} the {hank.species} is available to pet during the {
      hank.shift} shift.')

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "afternoon", "Llama Chow")
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {
      miss_fuzz.shift} shift.')

todd = Frog("Todd", "frog", "flies")

gina = Goldfish("Gina", "fish", "kelp")

mitch = Mallard("Mitch", "duck", "bread")

ham = Turtle("Ham", "turtle", "lettuce")

ken = Water_Bug("Ken", "bug", "gnats")

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
