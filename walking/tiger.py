from datetime import date


class Tiger:
    """Creating a class for Tigers
    """

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

    def food(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
