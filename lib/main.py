import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.refresh()

    # Create a window for the Textbox
    
    planet_win = curses.newwin(13, 38, 2, 2)

    # Draw a box around the Textbox
    rectangle(stdscr, 1, 1, 15, 40)
    stdscr.refresh()

    # Print the contents
    stdscr.addstr(5,5,"Planet PlaceHolder")
    stdscr.refresh()

    # Create a second window below planet_win
    second_win = curses.newwin(10, 30, 20, 2)
    second_box = Textbox(second_win)

    # Draw a box around the second_win
    rectangle(stdscr, 18, 1, 12, 32)
    stdscr.refresh()

    # Let the user edit the second_box
    second_box.edit()

    # Get the contents of the second_box
    second_contents = second_box.gather()

    # Wait for a key press before exiting
    stdscr.getch()

# Run the application using curses.wrapper
wrapper(main)
