#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_28():
    while not wall_is_on_the_left():
        move_left()
    if not wall_is_above():
            while not wall_is_above():
                move_up()
                if wall_is_above():
                    while not wall_is_on_the_left():
                        move_left()
                        if wall_is_on_the_left() and wall_is_above():
                            return
    while wall_is_above():
        while not wall_is_on_the_right():
            move_right()
            while not wall_is_above():
                move_up()
                if wall_is_above():
                    while not wall_is_on_the_left():
                        move_left()
                        if wall_is_on_the_left() and wall_is_above():
                            return
    pass

if __name__ == '__main__':
    run_tasks()
