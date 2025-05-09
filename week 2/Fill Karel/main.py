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
    while front_is_clear():
        fill()
        return_back()
        move_up()
    pass

def fill():
    """
    pre: empty row
    post: filled row
    """
    while front_is_clear():
        put_beeper()
        if front_is_clear():
            move()
    put_beeper()

def return_back():
    """
    pre: ending of row
    post: starting of row
    """
    turn_left()
    turn_left()
    while front_is_clear():
        move()

def move_up():
    """
    pre: lower row
    post: moved up
    """
    turn_left()
    turn_left()
    turn_left()
    if front_is_clear():
        move()
        turn_left()
        turn_left()
        turn_left()
    else:
        turn_left()
        turn_left()
        turn_left()
        while front_is_clear():
            move()



    pass
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()