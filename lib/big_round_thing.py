
#Sean's code
#from sqlalchemy import Column, Integer, String
#from base import Base

#class BigRoundThing(Base):
#    __tablename__ = 'big_round_things'

#    id = Column(Integer, primary_key=True)
#    name = Column(String, unique=True)

class big_round_thing:

    all = []

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("names must be strings.")
        elif not 1 <= len(name) <= 100:
            raise ValueError("name lengths must be between 1 and 100 characters")
        elif (name in big_round_thing.all_names()):
            raise ValueError("that name is already taken.")
        else:
            self._name = name
            big_round_thing.all.append(self)

    name = property(get_name, set_name)

    def all_names():
        return [thing.name for thing in big_round_thing.all]

    # def delete(self):
    #     big_round_thing.all.remove(self)
