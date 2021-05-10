from headers import *

class Bomb:
    def __init__(self, x_pos):
        self.x_pos = x_pos
        self.y_pos = 10
        self.struct = '0'
        self.speed = -1

    def shoot_bomb(self):
        self.y_pos -= self.speed
        grid[self.y_pos][self.x_pos] = self.struct