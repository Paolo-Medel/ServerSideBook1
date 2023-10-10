from animal_dir.animal import Animal


class Dolphin(Animal):
    """Creating a class for Dolphin
    """
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
