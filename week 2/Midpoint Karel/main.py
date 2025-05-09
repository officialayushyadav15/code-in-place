from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        move()
    turn_left()
    turn_left()
    if front_is_clear():
        put_beeper()
        while front_is_clear():
            move()
    if front_is_blocked():
        put_beeper()
        turn_left()
        turn_left()
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
            turn_left()
            turn_left()
            if no_beepers_present():
                move()
                put_beeper()
    turn_left()
    turn_left()
    while no_beepers_present():
        move()
    pick_beeper()
    turn_left()
    if front_is_clear():
        turn_left()
        turn_left()
        turn_left()
    else:
        turn_left()
    pass

if __name__ == '__main__':
    main()