"""learning classes"""
from datetime import date
from animal_dir import Snake, Earthworms, Leeches, Slugs, Lizard, Dolphin, Orca, Penguin, Seal, Whale, Buffalo, Llama, Tiger, Wolf, Squirrel
from attractions import PettingZoo, Attraction, SnakePit, Wetlands
from movements import Slithering, Swimming, Walking

miss_fuzz = Llama("miss fuzz", "Peruvian Llama", "Morning", "Fruity Loops", 123)
print(miss_fuzz.feed())
