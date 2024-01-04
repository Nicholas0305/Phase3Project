from big_round_thing import big_round_thing
from init import CURSOR, CONN

class Star(big_round_thing):
    def __init__(self, name, id = None):
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
        sql = """
            DROP TABLE IF EXISTS stars;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO stars (name)
            VALUES (?)
        """

        CURSOR.execute(sql, [self.name])
        CONN.commit()

        self.id = CURSOR.lastrowid

    # @classmethod
    # def create_star(cls, name):
    #     star = cls(name)
    #     star.save()
    #     return star
    
    @classmethod
    def create_star(cls, name):
        # Check if a star with the same name already exists
        existing_star = cls.get_star_by_name(name)
        if existing_star:
            print(f"A star with the name '{name}' already exists.")
            return existing_star

        # If no existing star, create a new one
        star = cls(name)
        star.save()
        return star

    @classmethod
    def get_star_by_name(cls, name):
        sql = "SELECT * FROM stars WHERE name = ?;"
        result = CURSOR.execute(sql, (name,)).fetchone()

        if result:
            star_id, star_name = result
            return cls(star_name, id=star_id)
        else:
            return None
        
    @classmethod
    def get_star_by_id(cls, id):
        sql = "SELECT * FROM stars WHERE id = ?;"
        result = CURSOR.execute(sql, (id,)).fetchone()

        if result:
            star_id, star_name = result
            return cls(star_name, id=star_id)
        else:
            return None
    
    def update(self):
        sql = """
            UPDATE stars
            SET name = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM stars
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        super().delete(self)
