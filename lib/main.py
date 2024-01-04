#!/usr/bin/env python3
from planets import Planet, create_engine, sessionmaker
from stars import Star
from big_round_thing import big_round_thing

def display_welcome_message(username):
    print(f"Welcome {username}! Each Pioneer's job is to establish colonies on other planets.")
    print("Thanks to advances in technology, we are able to create planets via the transformation of star matter into planet matter!")
    print("To get started, follow the prompts below! Good luck!\n")

def display_menu():
    return input("Menu: Colonize  Exit (Select an option): ").lower()

def colonize_option(username, stars, session):
    print("Available Stars:")
    for star in stars:
        print(star.name)
    print("")
    star_name = input(f"Welcome {username}! Please select from the list of available stars: ")
    selected_star = Star.get_star_by_name(session, star_name)

    if selected_star:
        #Create a planet associated with the selected star
        planet_name = input('Enter the name for the new planet: ')
        new_planet = Planet(name=planet_name, terrain='Standard Terrain', atmosphere='Standard Atmosphere', has_colony=False, star_id=selected_star.id)

        #Save the new planet to the database
        new_planet.save(session)
        print(f'Congratulations! Planet {planet_name} has been created and associated with star {selected_star.name}.')
    else: 
        print("Invalid star name. Please select a star from the list.")

def exit_option():
    print("Good job pioneer, go get some rest!")

def main():
    # Initialized variables
    exit_menu = False

    #Create the table for planets
    Planet.create_table()

    #Use sessionmaker to create a session
    Session = sessionmaker(bind=create_engine)
    session = Session()

    # Example List of pre-determined stars
    star1 = Star("The Sun")
    star2 = Star("Alpha Centauri")
    star3 = Star("Virgo")
    example_list = [star1, star2, star3]

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
            colonize_option(user_name, example_list, session)

        # Exits program if the user inputs exit
        elif menu_input == "exit":
            exit_option()
            exit_menu = True
    
    #Close the session after use
    session.close()

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
