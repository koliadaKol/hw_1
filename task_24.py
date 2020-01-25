#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_right(2)
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_right()
    move_down()
    fill_cell()
    move_up(2)
    move_left()
    pass


if __name__ == '__main__':
    run_tasks()
