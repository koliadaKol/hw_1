#!/usr/bin/python3

from pyrob.api import *
def draw_plus():
    move_down()
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
    
def draw_inv_plus():
    move_down()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_up()
    fill_cell()
    move_up()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    if not wall_is_on_the_left():
        move_left(2)
        move_up()
    pass

@task(delay=0.0002)
def task_2_4():
    for k in range(2):
        for i in range(10):
            draw_plus()
        move_down(3)
        for j in range(10):
            draw_inv_plus()
        move_down(3)
    while not wall_is_on_the_right():
        move_right()
    for l in range(10):
        draw_inv_plus()
    move_up()
    pass


if __name__ == '__main__':
    run_tasks()
