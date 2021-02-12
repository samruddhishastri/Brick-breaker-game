from headers import *

class Brick:
    def __init__(self):
        self.width = 12
        self.height = 3
        self.strength = 0
        self.struct = ''
        self.pos_x = 0
        self.pos_y = 0

    def create_brick(self):
        for i in range (self.pos_y, self.pos_y+3):
            for j in range(self.pos_x, self.pos_x + self.width):
                grid[i][j] = self.struct
                brick_board[i][j]['x'] = self.pos_x
                brick_board[i][j]['y'] = self.pos_y
                brick_board[i][j]['struct'] = self.struct

    def update_coordinates(self, x, y):
        self.pos_x = x
        self.pos_y = y

class unbreakableBrick(Brick):
    def __init__(self):
        Brick.__init__(self)
        self.strength = math.inf
        self.struct = UNBREAKABLE_BRICK

class Brick3(Brick):
    def __init__(self):
        Brick.__init__(self)
        self.strength = 3
        self.struct = BRICK3

class Brick2(Brick):
    def __init__(self):
        Brick.__init__(self)
        self.strength = 2
        self.struct = BRICK2

class Brick1(Brick):
    def __init__(self):
        Brick.__init__(self)
        self.strength = 1
        self.struct = BRICK1

def create_all_bricks():
    f = 0
    i=1
    for j in range(position, WIDTH-position, 12):
        if(f==0):
            b = unbreakableBrick()
            f=1
        else:
            b = Brick3()
            f=0
        b.update_coordinates(j,i)
        b.create_brick()

    f = 0
    i=4
    for j in range(position, WIDTH-position, 12):
        if(f==0):
            b = Brick3()
            f=1
        else:
            b = Brick2()
            f=0
        b.update_coordinates(j,i)
        b.create_brick()
    
    f = 0
    i=7
    for j in range(position, WIDTH-position, 12):
        if(f==0):
            b = Brick2()
            f=1
        else:
            b = unbreakableBrick()
            f=0
        b.update_coordinates(j,i)
        b.create_brick()

    f = 0
    i=10
    for j in range(position, WIDTH-position, 12):
        if(f==0):
            b = Brick3()
            f=1
        else:
            b = Brick1()
            f=0
        b.update_coordinates(j,i)
        b.create_brick()
    
    f = 0
    i=13
    for j in range(position, WIDTH-position, 12):
        if(f==0):
            b = Brick1()
            f=1
        else:
            b = Brick3()
            f=0
        b.update_coordinates(j,i)
        b.create_brick()

def show_bricks():
    for i in range(1,14,3):
        for j in range(position, WIDTH-position, 12):
            if(brick_board[i][j]['struct'] == UNBREAKABLE_BRICK):
                b = unbreakableBrick()
            elif(brick_board[i][j]['struct'] == BRICK1):
                b = Brick1()
            elif(brick_board[i][j]['struct'] == BRICK2):
                b = Brick2()
            elif(brick_board[i][j]['struct'] == BRICK3):
                b = Brick3()
            else:
                continue
            b.update_coordinates(j,i)
            b.create_brick()