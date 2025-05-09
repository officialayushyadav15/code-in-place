from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    """
    pre: we ssee at starting
    post: we see that the hospitals are constructed
    """
    while front_is_clear():
        if(beepers_present()):
            build()
        if front_is_clear():
            move() 
    pass

def build():
    """
    pre: found a beeper
    post: travelled and created all hospitals required
    """
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_angle()
    move()
    turn_angle()
    for i in range(2):
        put_beeper()
        move()
    put_beeper()
    turn_left()

    pass

def turn_angle():
    """
    pre: we see block at position
    post: we see it in correct direction
    """
    for i in range (3):
        turn_left()

if __name__ == '__main__':
    main()