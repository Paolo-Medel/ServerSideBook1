from movements import Walking
from .animal import Animal


class Llama(Animal, Walking):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift  # stays on Llama because not all animals have shifts

    def feed(self):
        return f'{self.name} was fed {self.food} on {self.date_added.strftime("%m/%d/%Y")}'
