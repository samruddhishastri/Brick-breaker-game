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
position = 54
initial_pos_pd = random.randint(position, WIDTH-position-12)
initial_pos_ball = random.randint(initial_pos_pd+2, initial_pos_pd+12)
grid = []
lives = 5
score = 0
brick_board = []

FLOOR = (Back.WHITE+"|"+Style.RESET_ALL)
CEIL = (Back.WHITE+"/"+Style.RESET_ALL)
LEFT_WALL = (Back.WHITE+","+Style.RESET_ALL)
RIGHT_WALL = (Back.WHITE+"."+Style.RESET_ALL)
PADDLE = (Back.BLUE+"_"+Style.RESET_ALL)
BALL = '\u25CF'
UNBREAKABLE_BRICK = (Back.BLACK+" "+Style.RESET_ALL)
BRICK1 = (Back.YELLOW+" "+Style.RESET_ALL)
BRICK2 = (Back.GREEN+" "+Style.RESET_ALL)
BRICK3 = (Back.RED+" "+Style.RESET_ALL)

def print_header(newtime, score):
    for j in range (WIDTH):
        print(Back.CYAN, "", end ="")
    text = "BRICK BREAKER GAME"
    dist = WIDTH
    print(Back.CYAN, text.center(dist), end="")
    for j in range (WIDTH-1):
        print(Back.CYAN, "", end ="")
    for j in range (WIDTH):
        print(Back.MAGENTA, "", end ="")
    
    text = "LIVES:"+str(lives)+" "*75+"SCORE:"+str(score)+" "*75+"TIME:"+str(newtime)
    
    print(Back.MAGENTA, text.center(0), end="")
    
    for j in range (WIDTH-len(text)-1):
        print(Back.MAGENTA, "", end ="")
    for j in range (WIDTH):
        print(Back.MAGENTA, "", end ="")
    print(Style.RESET_ALL,"\n")

def create_board():
    for i in range(HEIGHT):
        temp=[]
        for j in range(WIDTH):
            temp.append(" ")
        grid.append(temp)

    for i in range(HEIGHT):
        temp=[]
        for j in range(WIDTH):
            temp.append({'x':-1, 'y':-1, 'struct':-1})
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

def update_cursor(x, y):
    print("\033[%d;%dH" % (x, y))