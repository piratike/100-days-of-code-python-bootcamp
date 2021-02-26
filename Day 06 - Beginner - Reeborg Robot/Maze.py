def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if front_is_clear() and not right_is_clear():
        move()

    else:
        if right_is_clear():
            turn_right()
            move()

        else:
            turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
