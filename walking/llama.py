class Llama:
    """Creating a class for Llamas
    """

    def __init__(self, name, species, date_added, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True
        self.shift = shift
