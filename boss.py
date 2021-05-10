from headers import *

class Boss:
    def __init__(self):
        self.pos_x = 10
        self.pos_y = 5
        self.strength = 10
        self.struct = UFO

    def update_coordinates(self,x):
        self.pos_x = x

    def move_boss(self, x, y):
        self.pos_x += x
        self.pos_y += y

    def create_enemy(self):
        for i in range (self.pos_y, self.pos_y+len(UFO)):
            for j in range(self.pos_x, self.pos_x+len(UFO[0])):
                grid[i][j] = UFO[i-self.pos_y][j-self.pos_x]