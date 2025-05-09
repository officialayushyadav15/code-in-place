from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
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
        spread_beeper()
        back()
        row()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    
    


    
    pass

def row():
    turn_left()
    if front_is_clear():
        move()
        turn_left()
        turn_left()
        turn_left()

def spread_beeper():
    while beepers_present():
        pick_beeper()
        if beepers_present():
            while beepers_present():
                move()
            put_beeper()
            reset()
    put_beeper()

def reset():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()
    move()

def back():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()