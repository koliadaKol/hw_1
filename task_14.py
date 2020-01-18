#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while not wall_is_on_the_right():
        if not wall_is_beneath()and  wall_is_above():
            move_down()
            fill_cell()
            move_up()
        if wall_is_beneath()and not wall_is_above():
            move_up()
            fill_cell()
            move_down()
        if not wall_is_beneath() and not wall_is_above():
            move_down()
            fill_cell()
            move_up(2)
            fill_cell()
            move_down()
        if  wall_is_beneath() and wall_is_above():
            fill_cell()
        move_right()
    if not wall_is_beneath()and  wall_is_above():
        move_down()
        fill_cell()
        move_up()
    if wall_is_beneath()and not wall_is_above():
        move_up()
        fill_cell()
        move_down()
    if not wall_is_beneath() and not wall_is_above():
        move_down()
        fill_cell()
        move_up(2)
        fill_cell()
        move_down()
    if  wall_is_beneath() and wall_is_above():
            fill_cell()
    pass


if __name__ == '__main__':
    run_tasks()
