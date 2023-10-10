from attractions import Attraction
# from movements import Walking


class PettingZoo(Attraction):

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

    # Number 2: Actual typing check
    # def add_animal_type_check(self, animal):
    #     if isinstance(animal, Walking):
    #         self.animals.append(animal)
    #         print(f"{animal} now lives in {self.name}")
    #     else:
    #         print(
    #             f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.name} attraction.')
