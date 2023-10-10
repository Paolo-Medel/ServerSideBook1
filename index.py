"""learning classes"""
from datetime import date
from animal_dir import Snake, Earthworms, Leeches, Slugs, Lizard, Dolphin, Orca, Penguin, Seal, Whale, Buffalo, Llama, Tiger, Wolf, Squirrel
from attractions import PettingZoo, Attraction, SnakePit, Wetlands
from movements import Slithering, Swimming, Walking

varmint_village = PettingZoo(
    "The Varmint Village", "critters that love to be pet!")

# remember, some animals may require more arguments than others; e.g. shift
dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
snappy = Orca("Snappy", "Orca", "fish", 1044)

varmint_village.add_animal_pythonic(dolly)
varmint_village.add_animal_pythonic(snappy)
dolly.run()
