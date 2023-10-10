from animal_dir.animal import Animal


class Orca(Animal):
    """Creating a class for Orca
    """

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
