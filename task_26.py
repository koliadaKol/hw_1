#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    for i in range(5):
        move_right()
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            if not wall_is_on_the_right():
                move_right(3)
        move_down()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
            fill_cell()
            move_left()
            fill_cell()
            if not wall_is_on_the_left():
                move_left(2)
        move_down()
        move_right()
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            if not wall_is_on_the_right():
                move_right(3)
        if wall_is_on_the_right() and wall_is_beneath():
            move_down()
            while not wall_is_on_the_left():
                move_left()
            move_down()
    
    pass


if __name__ == '__main__':
    run_tasks()
