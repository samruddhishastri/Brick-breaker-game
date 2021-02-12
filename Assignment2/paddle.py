from headers import *

class Paddle:
    def __init__(self, pos, length):
        self.pos = pos
        self.length = length

    def print_paddle(self):
        for i in range(36,38):
            for j in range(self.pos):
                grid[i][j] = " "
            for j in range(self.pos, self.pos+self.length):
                grid[i][j] = PADDLE
            for j in range(self.pos+self.length, WIDTH):
                grid[i][j] = " "