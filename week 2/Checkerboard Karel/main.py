from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    tag_all_rows() # this refers to Step 1
    tag_row() # this refers to Step 2
    while left_is_clear(): #the rest of this section refers to Step 3
        turn_left()
        move()
        turn_right()
        tag_row()
    turn_right()
    move_to_wall()
    turn_left()

def tag_all_rows():
    turn_left()
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_around()
    move_to_wall()
    turn_left()

def tag_row():
    if beepers_present():
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
    else:
        while front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()
    turn_around()
    move_to_wall()
    turn_around()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()