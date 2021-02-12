from headers import *

class Ball:
    def __init__(self, pos_x):
        self.pos_x = pos_x
        self.pos_y = 35
        self.speed_x = 0
        self.speed_y = 0
        self.grab = True

    def print_ball(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        grid[self.pos_y][self.pos_x] = BALL
    
    def change_speed(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y