#!/usr/bin/env python3
from planets import Planet
from stars import Star
from init import CURSOR, CONN


def list_stars_option():
    sql = """
        SELECT * FROM stars
    """
    stars_table = CURSOR.execute(sql)
    for star in stars_table:
        print(star)
    return stars_table

def list_planets_option():
    sql = """
        SELECT * FROM planets
    """
    planets_table = CURSOR.execute(sql)
    for planet in planets_table:
        print(planet)
    return planets_table

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
        stars_table =list_stars_option()
        star_selection_input = input(f"Welcome {username}! Please select from the list of available stars (type 'menu' to go back): ") 

        if star_selection_input.lower() == "menu":
            return None

        for star in stars_table:
            if star_selection_input.lower() == star.name.lower():
                print("Traveling to star")
                return star_selection_input
        print("")
        print("----------------Enter a valid star--------------------")

def planet_selection(username):
    star_choice = star_selection(username)
    
    while True:
        planets_table = list_planets_option()
        print("Planets:")
        print("")
        #Prints list of planets
        for planet in planets_table:
            if planet.star.lower() == star_choice.lower():
                print(planet.name)
        #User choice to select or create planet
        planet_selection = input(f"{username}, please select or create a planet to establish a colony on")
        
        if planet_selection.lower() == "create":
            print("Enter the attributes you would like your planet to have")
            name = input("Enter a name for the Planet")
            terrain = input("Enter the terrain for the planet")
            atmosphere = input("Enter the atmosphere for the planet")
            Planet.create_planet(name,terrain,atmosphere,has_colony=False,star=star_choice)
        
  


#Exit message
def exit_option():
    
    print("Good job pioneer, go get some rest!")

def main():

    # Prepare to CRUD
    Star.create_table()
    Planet.create_table()
    
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
            star_selection(user_name)
            
            
            
        #Allows the user to return to menu whenever
        elif menu_input == "menu":
            return None

        # Exits program if the user inputs exit
        elif menu_input == "exit":
            exit_option()
            exit_menu = True

if __name__ == "__main__":
    main()

#OLDER IMPLEMENTATIONS


# from planets import planet
# from stars import Star
# from big_round_thing import big_round_thing

# #Initialized variables
# exit_menu = False

# #Example List of pre determined stars
# star1 = Star("The Sun")
# star2 = Star("Alpha Centauri")
# star3 = Star("Virgo")
# example_list = [star1,star2,star3]    

# #User input for Username
# user_name=input("Welcome Pioneer and thank you for choosing Space Tech as your pioneering company! To begin your journey, please insert your name:")
# print("")

# #Welcome Onboarding message
# print("")
# print(f"Welcome {user_name}! Each Pioneer's job is to establish colonies on other planets. Thanks to advances in technology, we are")
# print("able to create planets via the transformation of star matter into planet matter!")
# print("")
# print("To get started, follow the prompts below! Good luck!")
# print("")

# #Main Program Loop
# while exit_menu == False:
    
#     #User inputs if they want to begin the game or exit
#     menu_input = input("Menu: Colonize  Exit (Select an option):")
#     print()
    
#     #If user inputs colonize, the main game begins and displays stars to travel to.
#     if menu_input.upper() == "COLONIZE":
#         for star in example_list:
#             print(star.name)
#         print("")
#         input(f"Welcome {user_name}! Please select from the list of avaliable stars:")
        
#     #Exits program if the user inputs exit
#     elif menu_input.upper() == "EXIT":
#         print("Good job pioneer, go get some rest!")
#         exit_menu = True
    








# # CURSES IMPLEMENTATION 

# # import curses
# # from curses import wrapper
# # from curses.textpad import Textbox, rectangle

# # def main(stdscr):
# #     # Set up the screen
# #     curses.curs_set(0)  # Hide the cursor
# #     stdscr.clear()
# #     stdscr.refresh()

# #     # Create a window for the Textbox
    
# #     planet_win = curses.newwin(13, 38, 2, 2)

# #     # Draw a box around the Textbox
# #     rectangle(stdscr, 1, 1, 15, 40)
# #     stdscr.refresh()

# #     # Print the contents
# #     stdscr.addstr(5,5,"Planet PlaceHolder")
# #     stdscr.refresh()

# #     # Create a second window below planet_win
# #     second_win = curses.newwin(10, 30, 20, 2)
# #     second_box = Textbox(second_win)

# #     # Draw a box around the second_win
# #     rectangle(stdscr, 18, 1, 12, 32)
# #     stdscr.refresh()

# #     # Let the user edit the second_box
# #     second_box.edit()

# #     # Get the contents of the second_box
# #     second_contents = second_box.gather()

# #     # Wait for a key press before exiting
# #     stdscr.getch()

# # # Run the application using curses.wrapper
# # wrapper(main)
