#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    while not wall_is_beneath():
        move_right()
        while not wall_is_on_the_right():
            move_down()
            if wall_is_beneath():
                move_up()
                return
            move_up()
            fill_cell()
            move_right()
        move_down()
        move_left()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        move_down()
    
    pass


if __name__ == '__main__':
    run_tasks()
