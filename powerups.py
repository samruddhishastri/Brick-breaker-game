from headers import *
import os

class PowerUps:

    def __init__(self):
        self.newtime = 0
        self.total_time = 20
        self.struct = ''
        self.y_pos = 0
        self.x_pos = 0
        self.act = False
        self.vx = 0
        self.vy = 0
        self.g = 1

    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def activate():
        pass
    def deactivate():
        pass
    def print_powerup(self):
        if(self.y_pos == -1 and self.x_pos == -1):
            return
        if(self.y_pos + self.vy + self.g <= 40):
            self.y_pos += self.vy + self.g
            self.vy = self.vy + self.g
        else:
            self.y_pos = 40
            self.vy = -self.g
            self.vx = 0
        if((self.x_pos+self.vx <= WIDTH-position-2) and (self.x_pos+self.vx >= position)):
            self.x_pos += self.vx
        else:
            self.vx *= -1
            self.x_pos += self.vx

        grid[self.y_pos][self.x_pos] = self.struct

class ExpandPaddle(PowerUps):
    def __init__(self):
        PowerUps.__init__(self)
        self.struct = EXPAND_PADDLE

    def activate(self, pd):
        os.system('aplay -q ./sounds/power_up.wav&')
        self.act = True
        self.newtime = round(time.time()) - round(start_time)
        if(pd.length + 6 < WIDTH-2*position-1):
            pd.length += 6
            if(pd.pos + pd.length > WIDTH-position-2):
                pd.pos -= 6

    def deactivate(self, pd):
        self.act = -1
        if(pd.length - 6 > 0):
            pd.length -= 6

class ShrinkPaddle(PowerUps):
    def __init__(self):
        PowerUps.__init__(self)
        self.struct = SHRINK_PADDLE

    def activate(self, pd):
        os.system('aplay -q ./sounds/power_up.wav&')
        self.act = True
        self.newtime = round(time.time()) - round(start_time)
        if(pd.length - 6 > 0):
            pd.length -= 6

    def deactivate(self, pd):
        self.act = -1
        if(pd.length + 6 < WIDTH-2*position-1):
            pd.length += 6
            if(pd.pos + pd.length > WIDTH-position-2):
                pd.pos -= 6

class BallMultiplier(PowerUps):
    def __init__(self):
        PowerUps.__init__(self)
        self.struct = None

    def activate(self):
        pass

    def deactivate(self):
        pass

class FastBall(PowerUps):
    def __init__(self):
        PowerUps.__init__(self)
        self.struct = FAST_BALL

    def activate(self, ball):
        os.system('aplay -q ./sounds/power_up.wav&')
        self.act = True
        self.newtime = round(time.time()) - round(start_time)
        if(ball.speed_y < 3 and ball.speed_y > 0):
            ball.speed_y += 1
        elif(ball.speed_y > -3 and ball.speed_y <= 0):
            ball.speed_y -= 1

    def deactivate(self, ball):
        self.act = -1
        if(ball.speed_y >= 0):
            ball.speed_y -= 1
        elif(ball.speed_y < 0):
            ball.speed_y += 1

class ThruBall(PowerUps):
    def __init__(self):
        PowerUps.__init__(self)
        self.struct = THRU_BALL

    def activate(self, ball):
        os.system('aplay -q ./sounds/power_up.wav&')
        self.act = True
        self.newtime = round(time.time()) - round(start_time)
        ball.thru = True

    def deactivate(self, ball):
        self.act = -1
        ball.thru = False

class PaddleGrab(PowerUps):
    def __init__(self):
        PowerUps.__init__(self)
        self.struct = PADDLE_GRAB

    def activate(self, ball):
        os.system('aplay -q ./sounds/power_up.wav&')
        self.act = True
        self.newtime = round(time.time()) - round(start_time)
        ball.grab_powerup = True

    def deactivate(self, ball):
        self.act = -1
        ball.grab_powerup = False

class ShootingPaddle(PowerUps):
    def __init__(self):
        PowerUps.__init__(self)
        self.struct = SHOOTING_PADDLE
    def activate(self, pd):
        os.system('aplay -q ./sounds/power_up.wav&')
        self.act = True
        self.newtime = round(time.time()) - round(start_time)
        pd.shooting = True
    def deactivate(self, pd):
        self.act = -1
        pd.shooting = False      

class FireBall(PowerUps):
    def __init__(self):
        PowerUps.__init__(self)
        self.struct = FIRE_BALL

    def activate(self, ball):
        os.system('aplay -q ./sounds/power_up.wav&')
        self.act = True
        self.newtime = round(time.time()) - round(start_time)
        ball.fire = True

    def deactivate(self, ball):
        self.act = -1
        ball.fire = False