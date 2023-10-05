class Orca:
    """Creating a class for Orca
    """

    def __init__(self, name, species, date_added):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True
