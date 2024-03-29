#!/usr/bin/env python3
from planets import Planet
from stars import Star
from big_round_thing import big_round_thing
from init import CURSOR, CONN
#import ipdb

def list_stars_option():
    sql = """
        SELECT * FROM stars
    """
    CURSOR.execute(sql)
    stars_table = CURSOR.fetchall()
    star_names = [star[1] for star in stars_table]
    print(star_names)  
    return star_names

def make_planets_from_db():
    # When main.py starts, initialize instances corresponding to the rows in the database
    sql = """
        SELECT * FROM planets
    """
    CURSOR.execute(sql)
    planets_table = CURSOR.fetchall()
    # print(planets_table)
    planets = [list(planet) for planet in planets_table]
    print(planets[len(planets)-1])
    planets = [Planet(planet[1], planet[2], planet[3], bool(planet[4]), [star for star in big_round_thing.all if isinstance(star,Star) and star.id == planet[6]][0], planet[0]) for planet in planets]
    return planets

def make_stars_from_db():
    # When main.py starts, initialize instances corresponding to the rows in the database
    sql = """
        SELECT * FROM stars
    """
    CURSOR.execute(sql)
    stars_table = CURSOR.fetchall()
    # stars_table is a list of tuples. make them lists.
    stars = [list(star) for star in stars_table]
    # initialize star objects without adding them to the db
    stars = [Star(star[1], star[0]) for star in stars]
    return stars

def list_planets_option():
    sql = """
        SELECT * FROM planets
    """
    CURSOR.execute(sql)
    planet_table = CURSOR.fetchall()
    # Create planet objects from sql response data
    planets = make_planets_from_sql(planet_table)
    for planet in planets:
        print(planet.name)
    pass

#Captures user name 
def display_welcome_message(username):
    print(f"Welcome {username}! Each Pioneer's job is to establish colonies on other planets.")
    print("Thanks to advances in technology, we are able to create planets via the transformation of star matter into planet matter!")
    print("")
    print("To get started, enter colonize below. Enter Menu anytime to access it\n")

#Navigation menu
def display_menu():
    return input("Menu: Colonize  Exit (Select an option): ").lower()

#Lets the user travel to a star
def star_selection(username):
    while True:
        print("")
        print("Available Stars:")
        print("")
        star_names = list_stars_option()
        star_selection_input = input(f"Welcome {username}! Please select from the list of available stars (type 'menu' to go back): ")

        if star_selection_input.lower() == "menu":
            return None
        elif star_selection_input.lower() == "create":
            new_star=input("New Star:")
            new_star = Star.create_star(new_star)
        elif star_selection_input == "Destroy":
             star_choice = input("Enter star to destroy:")
             star_instance = [star for star in big_round_thing.all if star.name.lower() == star_choice.lower()][0]
             star_instance.remove_star()

        elif star_selection_input in star_names:
            print("")
            print("Traveling to star")
            print("")
            return star_selection_input
    
        print("")
        print("----------------Enter a valid star--------------------")

def planet_selection(username, star_choice):
    star_choice = str(star_choice)
    planet_menu = True
    star_instance = [star for star in big_round_thing.all if star.name.lower() == star_choice.lower()][0]
    if not isinstance(star_instance, Star):
        print(f"star_instance value is {star_instance}")
        raise ValueError("failed to get star_instance in planet_selection().")
    while planet_menu:
        planets = [item for item in big_round_thing.all if isinstance(item, Planet)]
        planets = [planet for planet in planets if planet.star.name.lower() == star_choice.lower()]
        planet_names = [planet.name for planet in planets]
        print('\n' + "Planets:" + '\n' + str(planet_names))
        planet_selection_input = input(f"{username}, please select an existing planet to establish a colony on or type 'create' to create a new planet(type 'menu' to go back): ")
        if planet_selection_input.lower() == "menu":
            return None
        elif planet_selection_input.lower() == "create":
            print("Enter the attributes you would like your planet to have")
            name = input("Enter a name for the Planet:")
            terrain = input("Enter the terrain for the planet:")
            atmosphere = input("Enter the atmosphere for the planet:")
            Planet.create_planet(name, terrain, atmosphere, False, star_instance)
        elif planet_selection_input.lower() == "destroy":
            
            planet_selection_input = input("Enter a planet to destroy:")
            planet = [planet for planet in big_round_thing.all if planet.name.lower() == planet_selection_input.lower()][0]
            print(planet)
            planet.remove_planet()
        elif planet_selection_input in planet_names:
            print(f"You have selected {planet_selection_input}")
            # Add code here to handle the selected planet
            planet = [planet for planet in big_round_thing.all if planet.name.lower() == planet_selection_input.lower()][0]
            has_colony_text = "has a colony." if planet.has_colony else "does not have a colony. "
            print(f"{planet.name} {has_colony_text}")
            if not planet.has_colony:
                colony_input = input(f"{planet.name} Establish a colony? Eanter Y/N: ")
                if colony_input == "Y":
                    planet.has_colony = True
                    planet.update()

        else:
            print("")
            print("----------------Enter a valid planet--------------------")

#Exit message
def exit_option():
    print("Good job pioneer, go get some rest!")


def main():
    # Prepare to CRUD

    Star.create_table()
    Planet.create_table()
    print("""===========================================================
============ PLANET COLONIZER: THE VIDEO GAME =============
===========================================================""")
    print("loading database...")
    loaded_stars = make_stars_from_db()
    loaded_star_names = [star.name for star in loaded_stars]
    print(f"Loaded {loaded_star_names}")    
    loaded_planets = make_planets_from_db()
    loaded_planet_names = [planet.name for planet in loaded_planets]
    print(f"Loaded {loaded_planet_names}")

    
    # Initialized variables
    exit_menu = False

    # DEBUGGING
    # # Example List of pre-determined stars
    # star1 = Star.create_star("The Sun")
    # star2 = Star.create_star("Alpha Centauri")
    # star3 = Star.create_star("Virgo")
    # #Example list of pre determined planets
    # planet1 = Planet.create_planet("Earth", "Rocky", "Air", True, star1)
    # planet2 = Planet.create_planet("Mars", "Rocky", "Thin", False, star1)
    # planet3 = Planet.create_planet("Pluto", "Rocky", "None", False, star1)
    # print(big_round_thing.all)
   
    # User input for Username
    user_name = input("Welcome Pioneer and thank you for choosing Space Tech as your pioneering company! "
                      "To begin your journey, please insert your name: ")

    # Welcome Onboarding message
    display_welcome_message(user_name)

    # Main Program Loop
    while not exit_menu:
        # User inputs if they want to begin the game or exit
        menu_input = display_menu()
        
        # If user inputs colonize, the main game begins and displays stars to travel to.
        if menu_input == "colonize":
            selected_star = star_selection(user_name)
            if selected_star:
                planet_selection(user_name, selected_star)

            
            
            
        #Allows the user to return to menu whenever
        elif menu_input == "menu":
            return None

        # Exits program if the user inputs exit
        elif menu_input == "exit":
            exit_option()
            exit_menu = True

if __name__ == "__main__":
    main()

