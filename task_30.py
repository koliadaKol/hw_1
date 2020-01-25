#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_9_3():
    a=0
    b=0
    move_right()
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
        a = a+1
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
    move_down()
    b= a-2
    for j in range(b):
        move_right(a-2)
        fill_cell()
    pass


if __name__ == '__main__':
    run_tasks()
