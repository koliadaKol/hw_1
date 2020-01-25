#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.00005)
def task_8_18():
    a=0
    ax=0
    while not wall_is_on_the_right():
        while wall_is_above() and wall_is_beneath():
            fill_cell()
            move_right()
        if wall_is_on_the_right():
            return
        while not wall_is_above():
            move_up()
        while not wall_is_beneath():
            if not cell_is_filled():
                fill_cell()
            else:
                a=a+1
                print(a)
            move_down()
        if not wall_is_on_the_right() and not wall_is_above():
            move_right()
        if wall_is_on_the_right():
            return
        print(a)
        mov('ax', a)
    pass


if __name__ == '__main__':
    run_tasks()
