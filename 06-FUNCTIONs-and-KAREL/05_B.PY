# SOLVE:  03_A_EXERCISE.PY CHALLENGE USING WHILE LOOP

# SON'T TRY TO SEE CODE, SOLVE IT AGAIN BY YOURSELF
























































































































































































































































































































































































































































































































































































































def turn_right():
    turn_left()
    turn_left()
    turn_left()

def master_move():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#master_move()
#master_move()
#master_move()
#master_move()
#master_move()
#master_move()

#for step in range(0,6):
#    master_move()


number_of_jump = 6

while number_of_jump > 0:
    master_move()
    number_of_jump -= 1
    print(number_of_jump)










