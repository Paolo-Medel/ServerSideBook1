from animal_dir.animal import Animal


class Seal(Animal):
    """Creating a class for Seal
    """

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
