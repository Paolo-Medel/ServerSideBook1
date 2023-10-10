class Attraction:

    def __init__(self, name):
        self.name = name
        self.animals = list()
    @property
    def last_critter_added(self):
        return f'The last critter added was {self.animals[-1].name}'