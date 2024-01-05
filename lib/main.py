#!/usr/bin/env python3
from planets import Planet
from stars import Star
from init import CURSOR, CONN

Star.create_table()
Planet.create_table()
star1 = Star.create_star("The Sun")
star2 = Star.create_star("Alpha Centauri")
star3 = Star.create_star("Virgo")

def list_stars_option():
    sql = """
        SELECT * FROM stars
    """
    CURSOR.execute(sql)
    stars_table = CURSOR.fetchall()
    star_names = [star[1] for star in stars_table]
    print(star_names)  
    return star_names

def list_planets_option():
    sql = """
        SELECT * FROM planets
    """
    CURSOR.execute(sql)
    planet_table = CURSOR.fetchall()
    planet_names = [planet[1] for planet in planet_table]
    print(planet_names)
    return planet_names

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
            Star.create_star(new_star)

        elif star_selection_input in star_names:
            print("")
            print("Traveling to star")
            print("")
            return star_selection_input
        


        print("")
        print("----------------Enter a valid star--------------------")

def planet_selection(username, star_choice):
    
    print("I'm in planet selection")
    while True:
        print("")
        print("Planets:")
        print("")
        planets_table = list_planets_option()
        print("")
        # Prints list of planets for the selected star
        for planet in planets_table:
            if planet.star.lower() == star_choice.lower():
                print(planet.name)
        # User choice to select or create planet
        planet_selection_input = input(f"{username}, please select or create a planet to establish a colony on (type 'menu' to go back): ")
        star_instance = Star.get_star_by_name(star_choice)
        if planet_selection_input.lower() == "menu":
            return None

        # Add logic to handle planet selection or creation based on user input
        if planet_selection_input.lower() == "create":
            print("Enter the attributes you would like your planet to have")
            name = input("Enter a name for the Planet:")
            terrain = input("Enter the terrain for the planet:")
            atmosphere = input("Enter the atmosphere for the planet:")
            Planet.create_planet(name, terrain, atmosphere, has_colony=False, star=star_instance)
            # Optionally, you can break out of the loop or perform other actions here

        # Add more conditions as needed

        print("")
        print("----------------Enter a valid planet--------------------")

        
  


#Exit message
def exit_option():
    
    print("Good job pioneer, go get some rest!")


def main():
    
    # Initialized variables
    exit_menu = False

    # Example List of pre-determined stars
    
    #Example list of pre determined planets
 
   
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
            if selected_star is not None:
                
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

