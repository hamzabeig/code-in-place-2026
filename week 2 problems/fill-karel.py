from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


from karel.stanfordkarel import *

def main():
    while left_is_clear():
        fill_row()
        go_back_to_start()
        move_up()
    fill_row()
    


def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()  


def go_back_to_start():
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def move_up():
    turn_left()
    move()
    turn_right()



def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
