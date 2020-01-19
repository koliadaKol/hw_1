#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down(2)
    for i in range(5):
        fill_cell()
        move_down()
        move_right()
        fill_cell()
        move_up()
        fill_cell()
        move_up()
        fill_cell()
        move_right()
        move_down()
        fill_cell()
        if not wall_is_on_the_right():
            move_right(2)
    move_up()
    move_left(2)
    pass


if __name__ == '__main__':
    run_tasks()
