from animal_dir.animal import Animal


class Earthworms(Animal):
    """Creating a class for Earthworms
    """
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
