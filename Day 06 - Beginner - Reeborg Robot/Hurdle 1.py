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
    move()
    jump()
    fall()
    turn_left()

while(not at_goal()):
    jump_wall()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
