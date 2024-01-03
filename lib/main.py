import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.refresh()

    # Create a window for the Textbox
    win = curses.newwin(13, 38, 2, 2)
    box = Textbox(win)

    # Draw a box around the Textbox
    rectangle(stdscr, 1, 1, 15, 40)
    stdscr.refresh()

    # Let the user edit the Textbox
    box.edit()

    # Get the contents of the Textbox
    contents = box.gather()

    # Print the contents
    stdscr.addstr(10, 2, "You entered: " + contents)
    stdscr.refresh()

    # Wait for a key press before exiting
    stdscr.getch()

# Run the application using curses.wrapper
curses.wrapper(main)
