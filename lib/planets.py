from big_round_thing import big_round_thing

class planet(big_round_thing):
    def __init__(self,name,terrain,atmosphere,has_colony):
        super().__init__(name)
        self.name = name
        self.terrain = terrain
        self.atmosphere = atmosphere
        self.has_colony = has_colony