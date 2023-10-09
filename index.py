"""learning classes"""
from datetime import date
from slithering import Snake, Earthworms, Leeches, Slugs, Lizard
from swiming import Dolphin, Orca, Penguin, Seal, Whale
from walking import Buffalo, Llama, Tiger, Wolf, Squirrel


class SnakePit:

    def __init__(self, name):
        self.name = name
        self.description = "I'm a snaaaaaaake"
        self.animals = list()
    @property
    def last_critter_added(self):
        return f'The last critter added was {self.animals[-1].name}'


class Wetlands:

    def __init__(self, name):
        self.name = name
        self.description = "Wetlands"
        self.animals = list()


class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

miss_fuzz = Llama("miss fuzz", "Peruvian Llama", "Morning", "Fruity Loops", 123)
print(miss_fuzz.feed())
