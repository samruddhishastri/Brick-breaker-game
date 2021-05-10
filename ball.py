from headers import *

class Ball:
    def __init__(self, pos_x):
        self.pos_x = pos_x
        self.pos_y = 35
        self.speed_x = 0
        self.speed_y = 1
        self.grab = True
        self.grab_powerup = False
        self.thru = False
        self.fire = False

    def print_ball(self):
        if(self.grab == False):
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
            grid[self.pos_y][self.pos_x] = BALL
        else:
            grid[self.pos_y][self.pos_x] = BALL
    
    def change_speed(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y