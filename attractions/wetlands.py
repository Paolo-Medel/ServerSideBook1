from attractions.attraction import Attraction


class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    # Number 1: Duck typing check
    def add_animal_pythonic(self, animal):

        # Check if the animal has a 'walk_speed' attribute
        if hasattr(animal, 'walk_speed'):
            self.animals.append(animal)
            print(f"{animal.name} now lives in {self.name}")
        else:
            print(
                f"{animal.name} doesn't have a 'walk_speed' attribute, so it cannot be added to the {self.name} attraction.")
