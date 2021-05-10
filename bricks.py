from headers import *

class Brick:
    def __init__(self):
        self.width = 12
        self.height = 3
        self.strength = 0
        self.struct = ''
        self.pos_x = 0
        self.pos_y = 0
        self.is_rainbow = False

    def create_brick(self):
        for i in range (self.pos_y, self.pos_y+3):
            for j in range(self.pos_x, self.pos_x + self.width):
                grid[i][j] = self.struct
                brick_board[i][j]['x'] = self.pos_x
                brick_board[i][j]['y'] = self.pos_y
                brick_board[i][j]['struct'] = self.struct
                brick_board[i][j]['is_rainbow'] = self.is_rainbow

    def update_coordinates(self, x, y):
        self.pos_x = x
        self.pos_y = y
    
    def make_rainbow_brick(self):
        self.is_rainbow = True

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

class ExplodingBrick(Brick):
    def __init__(self):
        Brick.__init__(self)
        self.strength = 1
        self.struct = EXPLODING_BRICK

def create_all_bricks_lvl1():
    b = unbreakableBrick()
    b.update_coordinates(position, 1)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position, 4)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position, 7)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position, 10)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position, 13)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position, 16)
    b.create_brick()

    b = Brick1()
    b.update_coordinates(position+12, 1)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+12, 4)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+12, 7)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+12, 10)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+12, 13)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+12, 16)
    b.make_rainbow_brick()
    b.create_brick()

    b = Brick2()
    b.update_coordinates(position+24, 1)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+24, 4)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+24, 7)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+24, 10)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+24, 13)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+24, 16)
    b.create_brick()

    b = Brick3()
    b.update_coordinates(position+36, 1)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+36, 4)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+36, 7)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+36, 10)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+36, 13)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+36, 16)
    b.create_brick()

    b = Brick1()
    b.update_coordinates(position+48, 1)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+48, 4)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+48, 7)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+48, 10)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+48, 13)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+48, 16)
    b.create_brick()

    b = ExplodingBrick()
    b.update_coordinates(position+60, 1)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+60, 4)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+60, 7)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+60, 10)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+60, 13)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+60, 16)
    b.create_brick()

    b = Brick1()
    b.update_coordinates(position+72, 1)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+72, 4)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+72, 7)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+72, 10)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+72, 13)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+72, 16)
    b.create_brick()

    b = unbreakableBrick()
    b.update_coordinates(position+84, 1)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+84, 4)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+84, 7)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+84, 10)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+84, 13)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+84, 16)
    b.create_brick()

def create_all_bricks_lvl2():

    b = Brick2()
    b.update_coordinates(position+12, 4)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+12, 7)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+12, 10)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+12, 13)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+12, 16)
    b.make_rainbow_brick()
    b.create_brick()


    b = unbreakableBrick()
    b.update_coordinates(position+24, 4)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+24, 7)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+24, 10)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+24, 13)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+24, 16)
    b.create_brick()


    b = Brick1()
    b.update_coordinates(position+36, 4)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+36, 7)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+36, 10)
    b.create_brick()
    b.make_rainbow_brick()
    b = Brick3()
    b.update_coordinates(position+36, 13)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+36, 16)
    b.create_brick()


    b = Brick2()
    b.update_coordinates(position+48, 4)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+48, 7)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+48, 10)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+48, 13)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+48, 16)
    b.create_brick()


    b = unbreakableBrick()
    b.update_coordinates(position+60, 4)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+60, 7)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+60, 10)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+60, 13)
    b.create_brick()
    b = Brick3()
    b.update_coordinates(position+60, 16)
    b.create_brick()

    b = Brick3()
    b.update_coordinates(position+72, 4)
    b.create_brick()
    b = unbreakableBrick()
    b.update_coordinates(position+72, 7)
    b.create_brick()
    b = Brick1()
    b.update_coordinates(position+72, 10)
    b.create_brick()
    b = ExplodingBrick()
    b.update_coordinates(position+72, 13)
    b.create_brick()
    b = Brick2()
    b.update_coordinates(position+72, 16)
    b.create_brick()

def spawn_bricks():
    m = 0
    for i in range(0, 85, 12):
        if(m==0):
            b = Brick2()
            b.update_coordinates(position+i, 19)
            b.create_brick()
            m = 1
        elif(m==1):
            b = Brick3()
            b.update_coordinates(position+i, 19)
            b.create_brick()
            m = 0

def add_few_unbreakable_bricks():
    for i in range(0, 85, 36):
        b = unbreakableBrick()
        b.update_coordinates(position+i, 16)
        b.create_brick()

def show_bricks():
    for i in range(1,17,3):
        for j in range(position, WIDTH-position, 12):
            if(brick_board[i][j]['is_rainbow'] == True):
                if(brick_board[i][j]['struct'] == BRICK1):
                    brick_board[i][j]['struct'] = BRICK2
                    b = Brick2()
                elif(brick_board[i][j]['struct'] == BRICK2):
                    brick_board[i][j]['struct'] = BRICK3
                    b = Brick3()
                elif(brick_board[i][j]['struct'] == BRICK3):
                    brick_board[i][j]['struct'] = BRICK1
                    b = Brick1()
                b.make_rainbow_brick()
            elif(brick_board[i][j]['struct'] == UNBREAKABLE_BRICK):
                b = unbreakableBrick()
            elif(brick_board[i][j]['struct'] == BRICK1):
                b = Brick1()
            elif(brick_board[i][j]['struct'] == BRICK2):
                b = Brick2()
            elif(brick_board[i][j]['struct'] == BRICK3):
                b = Brick3()
            elif(brick_board[i][j]['struct'] == EXPLODING_BRICK):
                b = ExplodingBrick()
            else:
                continue
            b.update_coordinates(j,i)
            b.create_brick()

def show_bricks_lvl3():
    for i in range(1,20,3):
        for j in range(position, WIDTH-position, 12):
            if(brick_board[i][j]['is_rainbow'] == True):
                if(brick_board[i][j]['struct'] == BRICK1):
                    brick_board[i][j]['struct'] = BRICK2
                    b = Brick2()
                elif(brick_board[i][j]['struct'] == BRICK2):
                    brick_board[i][j]['struct'] = BRICK3
                    b = Brick3()
                elif(brick_board[i][j]['struct'] == BRICK3):
                    brick_board[i][j]['struct'] = BRICK1
                    b = Brick1()
                b.make_rainbow_brick()
            elif(brick_board[i][j]['struct'] == UNBREAKABLE_BRICK):
                b = unbreakableBrick()
            elif(brick_board[i][j]['struct'] == BRICK1):
                b = Brick1()
            elif(brick_board[i][j]['struct'] == BRICK2):
                b = Brick2()
            elif(brick_board[i][j]['struct'] == BRICK3):
                b = Brick3()
            elif(brick_board[i][j]['struct'] == EXPLODING_BRICK):
                b = ExplodingBrick()
            else:
                continue
            b.update_coordinates(j,i)
            b.create_brick()