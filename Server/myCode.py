
#Import classes, functions, variables, from "mdev" files
from mDev import *
import random
import time
from datetime import datetime, timedelta

mdev = mDEV() #create object

# mdev.move(0, 0) 

inf = 1
buzzer = 1
move = 0

mdev.setServo('1', 42)

while inf == 1:

    # * THESE LINES ARE FOR SETTING THE TIME *

    # now = datetime.now()
    # new_time = now - timedelta(seconds=1)

    # current_time = now.strftime("%H:%M:%S")
    # updated_time = new_time.strftime("%H:%M:%S")

    # print(current_time)

    # alarm = "13:11:15" # set this to the value you want to test with

    # if updated_time == alarm:
    #     mdev.setBuzzer(0)
    #     move = 1

    # * * #

    # * THESE LINES ARE FOR TESTING WITHOUT TIME *

    current_time = "0"
    if current_time == "0":
        mdev.setBuzzer(0)
        move = 1

    # * * #

    while move == 1:
        
        angle = random.randint(0 - 42, 180 - 42)
        print(angle)

        direction = random.randint(1, 2)

        if direction == 1:
            mdev.move(500, 500, angle)
        else:
            mdev.move(-500, -500, angle)

        time.sleep(1)
        
        mdev.move(0, 0)
        
        # * TO END INFINITE LOOP * set both to 0 and run code to end loop
        move = 0
        inf = 0