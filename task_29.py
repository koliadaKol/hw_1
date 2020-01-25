#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    a = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            a=a+1
            move_right()
            if cell_is_filled():
                a=a+1
                move_right()
                if cell_is_filled():
                    a=a+1
                    move_right()
                else:
                    a=0
                    move_right()
            else:
                a=0
                move_right()
        else:
            a=0
            move_right()
        if a==3:
            move_left()
            return
        
    pass


if __name__ == '__main__':
    run_tasks()
