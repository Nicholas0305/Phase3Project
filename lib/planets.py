from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from . import Base
from big_round_thing import big_round_thing

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True, index=True)
    star_id = Column(Integer)
    name = Column(String, index=True)
    terrain = Column(String)
    atmosphere = Column(String)
    has_colony = Column(Boolean)
    population = Column(Integer)
    big_round_thing_id = Column(Integer)

    big_round_thing = relationship('BigRoundThing', back_populates='planet')

class planet(big_round_thing):
    def __init__(self,name,terrain,atmosphere,has_colony):
        super().__init__(name)
        self.name = name
        self.terrain = terrain
        self.atmosphere = atmosphere
        self.has_colony = has_colony