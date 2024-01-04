#sean's code
#from .base import Base
#from .big_round_thing import BigRoundThing
#from .star import Star
#from .planet import Planet
#from .solar_system import SolarSystem
import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()