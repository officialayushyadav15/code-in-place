from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    fill()
    move_forward()
    pass

def fill():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    for i in range (3):
        turn_left()


def move_down():
    while front_is_clear():
        move()
    turn_left()
    pass


def move_forward():
    while front_is_clear():
        for i in range(4):
            move()
        for i in range(3):
            turn_left()
        move_down()
        fill()
    turn_left()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

        
    pass




if __name__ == '__main__':
    main()