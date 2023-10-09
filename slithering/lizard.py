from animal_dir.animal import Animal


class Lizard(Animal):
    """Creating a class for Lizard
    """
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
