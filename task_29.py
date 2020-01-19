#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    while not wall_is_on_the_right():
        move_right()
        for i in range(3):
            if cell_is_filled():
                move_right()
                a=a+1
            if a==3:
                return
    pass


if __name__ == '__main__':
    run_tasks()
