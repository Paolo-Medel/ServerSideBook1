from animal_dir.animal import Animal


class Snake(Animal):
    """Creating a class for snake
    """
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
