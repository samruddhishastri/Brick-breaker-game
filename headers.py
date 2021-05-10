from colorama import init, Fore, Back, Style
init()
import numpy as np
import os
import sys
import math
import random
import time
import signal
from alarmexception import AlarmException
from getch import _getChUnix as getChar

start_time = time.time()
siz = os.get_terminal_size()
WIDTH = siz.columns
HEIGHT = siz.lines - 8
position = 50
initial_pos_pd = random.randint(position, WIDTH-position-14)
initial_pos_ball = random.randint(initial_pos_pd+2, initial_pos_pd+12)
grid = []
brick_board = []
power_ups = []
total_bricks = 38

lvl = 1

FLOOR = (Back.LIGHTWHITE_EX+"|"+Style.RESET_ALL)
CEIL = (Back.LIGHTWHITE_EX+"/"+Style.RESET_ALL)
LEFT_WALL = (Back.LIGHTWHITE_EX+","+Style.RESET_ALL)
RIGHT_WALL = (Back.LIGHTWHITE_EX+"."+Style.RESET_ALL)
PADDLE = (Back.BLUE+"_"+Style.RESET_ALL)
BALL = '\u25CF'
EXPAND_PADDLE = '\u25A0'
SHRINK_PADDLE = '\u25A1'
FAST_BALL = '\u25C6'
THRU_BALL = '\u25CC'
PADDLE_GRAB = '\u25C9'
SHOOTING_PADDLE = '*'
FIRE_BALL = '@'
UNBREAKABLE_BRICK = (Back.BLACK+" "+Style.RESET_ALL)
BRICK1 = (Back.YELLOW+" "+Style.RESET_ALL)
BRICK2 = (Back.GREEN+" "+Style.RESET_ALL)
BRICK3 = (Back.RED+" "+Style.RESET_ALL)
EXPLODING_BRICK = (Back.LIGHTBLUE_EX+" "+Style.RESET_ALL)
UFO = [
    list(" o            o "),
    list("  \          /  "),
    list("   \        /   "),
    list('    :-""""-:    '),
    list(" .-'  ____  `-. "),
    list("( (  (_()_)  ) )"),
    list(" `-.   ^^   .-' "),
    list("    `._==_.'    "),
    list("     __)(___    ")
]

def create_board():
    for i in range(HEIGHT):
        temp=[]
        for j in range(WIDTH):
            temp.append(" ")
        grid.append(temp)

    for i in range(HEIGHT):
        temp=[]
        for j in range(WIDTH):
            temp.append({'x':-1, 'y':-1, 'struct':-1, 'is_rainbow':False})
        brick_board.append(temp)

def create_ceil():
    for i in range(1):
        for j in range(WIDTH):
            grid[i][j] = CEIL

def create_side_walls():
    for i in range(HEIGHT-6):
        for j in range(position-2,position):
            grid[i][j] = LEFT_WALL
    for i in range(HEIGHT-6):
        for j in range(WIDTH-position,WIDTH-position+2):
            grid[i][j] = RIGHT_WALL

def create_floor():
    for i in range(41,42):
        for j in range(WIDTH):
            grid[i][j] = FLOOR

def print_grid():
    for i in range(HEIGHT-3):
        for j in range(WIDTH):
            print(grid[i][j], end='')
        print()

def clear_grid():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            grid[i][j] =" "

def reset_brick_board():
    brick_board.clear()
    for i in range(HEIGHT):
        temp=[]
        for j in range(WIDTH):
            temp.append({'x':-1, 'y':-1, 'struct':-1, 'is_rainbow':False})
        brick_board.append(temp)


def clear_power_ups():
    power_ups = []

def update_cursor(x, y):
    print("\033[%d;%dH" % (x, y))

def lose_game():
    os.system('clear')
    a = '''
    
Y88b   d88P                     888                   888    
 Y88b d88P                      888                   888    
  Y88o88P                       888                   888    
   Y888P  .d88b.  888  888      888  .d88b.  .d8888b  888888 
    888  d88""88b 888  888      888 d88""88b 88K      888    
    888  888  888 888  888      888 888  888 "Y8888b. 888    
    888  Y88..88P Y88b 888      888 Y88..88P      X88 Y88b.  
    888   "Y88P"   "Y88888      888  "Y88P"   88888P'  "Y888 
                                                                                                                     
'''
    print(a.center(WIDTH))
    quit()

def win_game():
    os.system('clear')
    os.system('aplay -q ./sounds/win.wav&')
    a = '''
    
Y88b   d88P                                                     
 Y88b d88P                                                      
  Y88o88P                                                       
   Y888P  .d88b.  888  888      888  888  888  .d88b.  88888b.  
    888  d88""88b 888  888      888  888  888 d88""88b 888 "88b 
    888  888  888 888  888      888  888  888 888  888 888  888 
    888  Y88..88P Y88b 888      Y88b 888 d88P Y88..88P 888  888 
    888   "Y88P"   "Y88888       "Y8888888P"   "Y88P"  888  888 
                                                                                                                                           
    '''
    print(a.center(WIDTH))
    quit()