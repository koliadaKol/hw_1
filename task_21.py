#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    a=1
    r=12
    move_down()
    for j in range(6):
        a = a+2
        for i in range(r):
            move_right()
            fill_cell()
            move_down()
            fill_cell()
        move_right()
        fill_cell()
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()
        move_down(a)
        r = r-2
    move_right()
    fill_cell()
    move_down()
    pass


if __name__ == '__main__':
    run_tasks()
