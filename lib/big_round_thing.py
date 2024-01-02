class big_round_thing:

    all = []
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("names must be strings.")
        elif (name in [thing.name for thing in big_round_thing.all]):
            raise ValueError("that name is already taken.")
        else:
            self._name = name
            big_round_thing.all.append(self)

    name = property(get_name, set_name)

    def delete(self):
        big_round_thing.all.remove(self)
