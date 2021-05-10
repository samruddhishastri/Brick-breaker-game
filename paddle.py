from headers import *

class Paddle:
    def __init__(self, pos, length):
        self.pos = pos
        self.length = length
        self.shooting = False

    def print_paddle(self):
        if(self.shooting == True):
            grid[35][self.pos] = PADDLE
            grid[35][self.pos+self.length-1] = PADDLE
        for i in range(36,38):
            for j in range(self.pos):
                grid[i][j] = " "
            for j in range(self.pos, self.pos+self.length):
                grid[i][j] = PADDLE
            for j in range(self.pos+self.length, WIDTH):
                grid[i][j] = " "