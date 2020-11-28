def get_around():
    for i in range(3):
        turn_left()

def jump():
    turn_left()
    move()
    get_around()

def fall():
    move()
    get_around()
    move()

def jump_wall():
    jump()
    fall()
    turn_left()

while(not at_goal()):
    if not front_is_clear():
        jump_wall()

    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
