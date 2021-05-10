from headers import *

class Bullet:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.struct = '^'
        self.speed = 1

    def shoot_bullet(self):
        self.y_pos -= self.speed
        grid[self.y_pos][self.x_pos] = self.struct