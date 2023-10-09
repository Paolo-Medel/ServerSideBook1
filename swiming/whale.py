from animal_dir.animal import Animal


class Whale(Animal):
    """Creating a class for Whale
    """
    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
