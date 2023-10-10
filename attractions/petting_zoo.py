from attractions.attraction import Attraction

class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        