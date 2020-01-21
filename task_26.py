#!/usr/bin/python3

from pyrob.api import *
def draw_plus():
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
    move_left()
    move_up()
    pass

@task(delay=0.02)
def task_2_4():
    for i in range(5):
        draw_plus()
        
    
    pass


if __name__ == '__main__':
    run_tasks()
