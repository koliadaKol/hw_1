#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    if not wall_is_above():
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()
        return
    while not wall_is_on_the_right():
        if wall_is_above():
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
            return
        move_right()
        if wall_is_on_the_right():
            while not wall_is_on_the_left():
                if not wall_is_above():
                    while not wall_is_above():
                        move_up()
                    while not wall_is_on_the_left():
                        move_left()
                    return
                move_left()
    pass


if __name__ == '__main__':
    run_tasks()
