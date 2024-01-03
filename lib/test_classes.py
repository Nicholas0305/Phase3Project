# Run this script to quickly initialize some classes and interact with them

from planets import planet
from stars import Star
from big_round_thing import big_round_thing
import ipdb

star1 = Star("The Sun")
star2 = Star("Alpha Centauri")
star3 = Star("Virgo")

# This should raise an exception:
# star4 = Star("The Sun")

planet1 = planet("Mars", "Rocky", "thin", False, star1) 
planet2 = planet("Earth", "Rocky", "nice", True, star1) 
planet3 = planet("Krypton", "Rocky", "unknown", False, star2)

#Establish colonies:
planet1.set_has_colony(True)
planet2.set_has_colony(True)

#Create a standard planet and star
standard_star = Star.create_standard_star('Standard Star')
standard_planet = planet.create_standard_planet('Standard Planet', standard_star)

#Remove the planet and star
standard_planet.remove_planet()
standard_star.remove_star()

# These should all raise exceptions:
# planet4 = planet(100, "Rocky", "thin", False, star1) 
# planet5 = planet("Mars", None, "thin", False, star1) 
# planet6 = planet("Mars", "Rocky", [1,2], False, star1) 
# planet7 = planet("Mars", "Rocky", "thin", 0, star1) 
# planet8 = planet("Mars", "Rocky", "thin", False, "The Sun") 
# planet1.set_has_colony(True)
# planet1.set_star(star3)

# print(planet1.sql_insert_command())

ipdb.set_trace()
