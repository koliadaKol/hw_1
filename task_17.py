#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while not cell_is_filled():
        move_up()
<<<<<<< HEAD
    move_right()
    if cell_is_filled():
        return
    else:
        move_left(2)
=======
    move_left()
    if cell_is_filled():
        return
    else:
        move_right(2)
>>>>>>> 1f06268b01a3b9569a7cb3064ddb6b3e62a04c76
    pass


if __name__ == '__main__':
    run_tasks()
