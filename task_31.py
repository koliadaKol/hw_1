#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.03)
def task_8_30():
    
    while not wall_is_on_the_left():
        if wall_is_beneath():
            move_left()
        else:
            move_down()
    while not wall_is_on_the_right():
        if wall_is_beneath():
            move_right()
        else:
            move_down()
    pass


if __name__ == '__main__':
    run_tasks()
