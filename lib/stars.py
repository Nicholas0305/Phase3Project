from big_round_thing import big_round_thing

class Star(big_round_thing):
    def __init__(self,name):
        super().__init__(name)
    
    #Class method for creating stars with set features
    @classmethod
    def create_standard_star(cls, name):
        return cls(name)
    
    #Method to remove the star
    def remove_star(self):
        print(f'Removing star: {self.name}')
        self.delete()

#sean's code
#from sqlalchemy import Column, Integer, ForeignKey
#from sqlalchemy.orm import relationship
#from base import Base
#from big_round_thing import BigRoundThing

#class Star(BigRoundThing):
#    __tablename__ = 'stars'

#    id = Column(Integer, ForeignKey('big_round_things.id'), primary_key=True)
#    solar_system_id = Column(Integer, ForeignKey('solar_systems.id'))

#    __mapper_args__ = {
#        'polymorphic_identity':'stars',
#    }