from big_round_thing import big_round_thing
from init import CURSOR, CONN

class Star(big_round_thing):
    def __init__(self,name, id = None):
        super().__init__(name)
        self.id = id
    
    #Class method for creating stars with set features
    @classmethod
    def create_standard_star(cls, name):
        return cls(name)
    
    #Method to remove the star
    def remove_star(self):
        print(f'Removing star: {self.name}')
        self.delete()

    # Method to create sql table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS stars (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()



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