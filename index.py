"""learning classes"""

from slithering import Snake, Earthworms, Leeches, Slugs, Lizard
from swiming import Dolphin, Orca, Penguin, Seal, Whale
from walking import Buffalo, Llama, Squirrel, Tiger, Wolf
# import the python datetime module to help us create a timestamp
from datetime import date

Buffy = Buffalo("buffy", "great-plains", date.today(), "morning")
print(f"{Buffy.name} will have the {Buffy.shift} shift")

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")

print(miss_fuzz)
