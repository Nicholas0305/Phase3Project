from big_round_thing import big_round_thing
from init import CURSOR, CONN
from stars import Star

class Planet(big_round_thing):
    all = []

    def __init__(self, name, terrain, atmosphere, has_colony, star, id = None):
        super().__init__(name)
        self.terrain = terrain
        self.atmosphere = atmosphere
        self.has_colony = has_colony
        self.star = star
        self.id = id
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS planets (
                id INTEGER PRIMARY KEY,
                star_id INTEGER,
                name TEXT,
                terrain TEXT,
                atmosphere TEXT,
                has_colony BOOLEAN,
                population INTEGER,
                big_round_thing_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS planets;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO planets (star_id, name, terrain, atmosphere, has_colony, population, big_round_thing_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        values = (self.star.id, self.name, self.terrain, self.atmosphere, self.has_colony, self.population, self.big_round_thing_id)
        CURSOR.execute(sql, values)
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    @classmethod
    def create_planet(cls, name, terrain, atmosphere, has_colony, star):
        planet = cls(name, terrain, atmosphere, has_colony, star)
        planet.save()
        return planet
    
    def update(self):
        sql = """
            UPDATE planets
            SET star_id = ?, name = ?, terrain = ?, atmosphere = ?,
                has_colony = ?, population = ?, big_round_thing_id = ?
            WHERE id = ?
        """
        values = (self.star.id, self.name, self.terrain, self.atmosphere, self.has_colony, self.population, self.big_round_thing_id, self.id)
        CURSOR.execute(sql, values)
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM planets
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit
    
    @classmethod
    def get_planets(cls):
        sql = """
            SELECT * FROM planets;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        planets = []

        for row in rows:
            planet = cls(*row)
            planets.append(planet)
        return planets
    
    @classmethod
    def get_planets_by_name(cls, name):
        sql = """
            SELECT * FROM planets WHERE name = ?;
        """
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()

        if row:
            planet = cls(*row)
            return planet
        else:
            return None

    # Terrain property
    def get_terrain(self):
        return self._terrain
        
    def set_terrain(self, terrain):
        if not isinstance(terrain, str):
            raise ValueError("terrain must be a string.")
        elif not 1 <= len(terrain) <= 100:
            raise ValueError("terrain lengths must be between 1 and 100 characters")
        else:
            self._terrain = terrain

    terrain = property(get_terrain, set_terrain)

    # Atmosphere property
    def get_atmosphere(self):
        return self._atmosphere
        
    def set_atmosphere(self, atmosphere):
        if not isinstance(atmosphere, str):
            raise ValueError("atmosphere must be a string.")
        elif not 1 <= len(atmosphere) <= 100:
            raise ValueError("atmosphere lengths must be between 1 and 100 characters")
        else:
            self._atmosphere = atmosphere

    atmosphere = property(get_atmosphere, set_atmosphere)

    # has_colony property
    def get_has_colony(self):
        return self._has_colony
        
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
    
    #Method to remove the planet
    def remove_planet(self):
        print(f'Removing planet: {self.name}')
        self.delete()
        