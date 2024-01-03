
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
        # is the planet/star being renamed?
        old_name = None
        if hasattr(self,'name'):
            old_name = self.name
        # Ensure the given name is valid
        if not isinstance(name, str):
            raise ValueError("names must be strings.")
        elif not 1 <= len(name) <= 100:
            raise ValueError("name lengths must be between 1 and 100 characters")
        elif (name in big_round_thing.all_names()):
            raise ValueError("that name is already taken.")
        else:
            self._name = name
            if not self in big_round_thing.all:
                big_round_thing.all.append(self)
            if old_name:
                print(f'{old_name} was renamed to {self.name}.')

    name = property(get_name, set_name)

    def all_names():
        return [thing.name for thing in big_round_thing.all]
    
    def sql_insert_command(self):
        props = list(self.__dict__.keys())
        print("props = " , props)
        vals = ""
        for prop in props:
            vals += self.prop + " "
        print("vals = " , vals)
        command = "INSERT INTO " + table + " " + str(set(props)) + " VALUES (" + vals +");"
        return command

    def delete(self):
        big_round_thing.all.remove(self)
        # The object still exists in memory with a variable assigned to it.
