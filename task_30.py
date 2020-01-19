#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    move_right()
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
    move_down()
    while not wall_is_beneath():
        fill_cell()
        move_down()
    move_left()
    while not wall_is_on_the_left():
        fill_cell()
        move_left()
    move_up()
    while not wall_is_above():
        fill_cell()
        move_up()
    pass


if __name__ == '__main__':
    run_tasks()
