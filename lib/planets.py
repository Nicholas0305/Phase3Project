# from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.orm import relationship
# from . import Base
from big_round_thing import big_round_thing
from stars import Star

"""
class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True, index=True)
    star_id = Column(Integer)
    name = Column(String, index=True)
    terrain = Column(String)
    atmosphere = Column(String)
    has_colony = Column(Boolean)
    population = Column(Integer)
    big_round_thing_id = Column(Integer) # We shouldn't need this column because we will not make any instances of big_round_thing. -Evan

    big_round_thing = relationship('BigRoundThing', back_populates='planet') # We shouldn't need this for the same reason. -Evan
"""

class planet(big_round_thing):
    def __init__(self, name, terrain, atmosphere, has_colony, star):
        super().__init__(name)
        self._terrain = terrain
        self._atmosphere = atmosphere
        self._has_colony = has_colony
        self._star = star

    # Terrain property
    def get_terrain(self):
        return self._terrain
        
    def set_terrain(self, terrain):
        if not isinstance(terrain, str):
            raise ValueError("terrain must be a string.")
        else:
            self._terrain = terrain

    terrain = property(get_terrain, set_terrain)

    # Atmosphere property
    def get_atmosphere(self):
        return self._atmosphere
        
    def set_atmosphere(self, atmosphere):
        if not isinstance(atmosphere, str):
            raise ValueError("atmosphere must be a string.")
        else:
            self._atmosphere = atmosphere

    atmosphere = property(get_atmosphere, set_atmosphere)

    # has_colony property
    def get_has_colony(self):
        return self._get_has_colony
        
    def set_has_colony(self, has_colony):
        if not isinstance(has_colony, bool):
            raise ValueError("has_colony must be a boolean.")
        else:
            self._has_colony = has_colony
            if (has_colony):
                print("Congratulations, you established a colony on " + self.name + "!")

    has_colony = property(get_has_colony, set_has_colony)

    # Star property
    def get_star(self):
        return self._star
        
    def set_star(self, star):
        if not isinstance(star, Star):
            raise ValueError("star must be an instance of Star.")
        elif hasattr(self, 'star'):
            raise ValueError("this planet already has a star.")
        else:
            self._star = star

    star = property(get_star, set_star)

    #Class method for creating planets with set features
    @classmethod
    def create_standard_planet(cls, name, star):
        return cls(name, 'Standard Terrain', 'Standard Atmosphere', False, star)

#Sean's code 
#from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
#from sqlalchemy.orm import relationship
#from base import Base
#from big_round_thing import BigRoundThing
#from star import Star

#class Planet(BigRoundThing):
#    __tablename__ = 'planets'

#    id = Column(Integer, ForeignKey('big_round_things.id'), primary_key=True)
#    terrain = Column(String)
#    atmosphere = Column(String)
#    has_colony = Column(Boolean)
#    star_id = Column(Integer, ForeignKey('stars.id'))

#    star = relationship('Star', back_populates='planets')

#    __mapper_args__ = {
#        'polymorphic_identity':'planets',
#    }