from headers import *
from paddle import *
from ball import *
from bricks import *
from powerups import *
from bullets import *
from boss import *
from bombs import *
import os

os.system('clear')
pd = Paddle(initial_pos_pd, 15)
ball = Ball(initial_pos_ball)
enemy = Boss()

initial_speed_y = -1
speed_paddle = 4

all_bullets = []
all_bombs = []

all_power_ups = [0]*70
all_power_ups[9] = 'ep'
all_power_ups[19] = 'sp'
all_power_ups[29] = 'fb'
all_power_ups[39] = 'tb'
all_power_ups[49] = 'pg'
all_power_ups[59] = 'shp'
all_power_ups[69] = 'fbl'

lives = 10
score = 0

total_spawns = 0

tim = 0

def reinitialise():
    pd = Paddle(initial_pos_pd, 15)
    ball = Ball(initial_pos_ball)

    initial_speed_y = -1
    speed_paddle = 4

def update_total_bricks(num):
    global total_bricks
    total_bricks = num

def create_boss():
    enemy.create_enemy()
    if(pd.pos+16 < WIDTH-position-2):
        enemy.update_coordinates(pd.pos)
    else:
        enemy.update_coordinates(WIDTH-position-16)

def deactivate_all_powerups():
    for i in range(len(power_ups)):
        if(power_ups[i].struct == EXPAND_PADDLE):
            if(power_ups[i].act == True):
                power_ups[i].deactivate(pd)
            
        elif(power_ups[i].struct == SHRINK_PADDLE):
            if(power_ups[i].act == True):
                power_ups[i].deactivate(pd)

        elif(power_ups[i].struct == FAST_BALL):
            if(power_ups[i].act == True):
                power_ups[i].deactivate(ball)

        elif(power_ups[i].struct == THRU_BALL):
            if(power_ups[i].act == True):
                power_ups[i].deactivate(ball)

        elif(power_ups[i].struct == PADDLE_GRAB):
            if(power_ups[i].act == True):
                power_ups[i].deactivate(ball)

        elif(power_ups[i].struct == SHOOTING_PADDLE):
            if(power_ups[i].act == True):
                power_ups[i].deactivate(pd)
                stop_shooting_bullets()

        elif(power_ups[i].struct == FIRE_BALL):
            if(power_ups[i].act == True):
                power_ups[i].deactivate(ball)

def print_header(newtime):

    global total_spawns

    for j in range (WIDTH):
        print(Back.CYAN, "", end ="")
    text = "BRICK BREAKER GAME"
    dist = WIDTH
    print(Back.CYAN, text.center(dist), end="")
    for j in range (WIDTH-1):
        print(Back.CYAN, "", end ="")
    for j in range (WIDTH):
        print(Back.MAGENTA, "", end ="")
    if(lvl < 3):
        if(pd.shooting == False):
            text = "LVL:"+str(lvl)+" "*7+"BALLS:"+str(lives)+" "*7+"SCORE:"+str(score)+" "*7+"TIME:"+str(newtime)+" "*7+"BRICKS:"+str(total_bricks)
        else:
            text = "LVL:"+str(lvl)+" "*7+"BALLS:"+str(lives)+" "*7+"SCORE:"+str(score)+" "*7+"TIME:"+str(newtime)+" "*7+"BRICKS:"+str(total_bricks) + " "*7 +"SHOOTING TIME LEFT:"+str(tim)
    else:
        text = "LVL:"+str(lvl)+" "*7+"BALLS:"+str(lives)+" "*7+"SCORE:"+str(score)+" "*7+"TIME:"+str(newtime)+" "*7+"BRICKS:"+str(total_bricks)+" "*7+"ENEMY LIFE:"+ str(enemy.strength)
    print(Back.MAGENTA, text.center(dist), end="")
    
    for j in range (WIDTH-1):
        print(Back.MAGENTA, "", end ="")
    print(Style.RESET_ALL,"\n")

    if(total_bricks <= 0):
        if(lvl != 3):
            lvl_up()
        elif(total_spawns == 1):
            spawn_bricks()
            update_total_bricks(8)
            total_spawns += 1

    return lvl

def lvl_up():
    global lvl
    lvl += 1
    ball.grab = True
    initial_pos_ball = random.randint(pd.pos, pd.pos+pd.length-2)
    ball.pos_x = initial_pos_ball
    ball.pos_y = 35
    ball.change_speed(0, ball.speed_y)

def move_paddle():
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=0.1):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None

    INPUT_CHAR = user_input()
    char=INPUT_CHAR

    if(ball.grab == True):
        if char == 'd':
            if(pd.pos + pd.length + speed_paddle < WIDTH-position):
                pd.pos += speed_paddle
                ball.pos_x += speed_paddle
            else:
                ball.pos_x += (WIDTH-position+1) - (pd.pos + pd.length) -1
                pd.pos += (WIDTH-position+1) - (pd.pos + pd.length) -1

        elif char == 'a':
            if(pd.pos-speed_paddle> position):
                pd.pos -= speed_paddle
                ball.pos_x -= speed_paddle
            else:
                ball.pos_x -= pd.pos - position
                pd.pos -= (pd.pos - position)

        elif char == 's':
            ball.change_speed((ball.pos_x - pd.pos -(pd.length//2)-1)//2, ball.speed_y)
            ball.grab = False

        elif char == 'q':
            os.system('clear')
            quit()
        
        elif char == 'n':
            lvl_up()

    else:
        if char == 'd':
            if(pd.pos + pd.length+speed_paddle < WIDTH-position):
                pd.pos += speed_paddle
            else:
                pd.pos = WIDTH-position- pd.length

        elif char == 'a':
            if(pd.pos - speed_paddle > position):
                pd.pos -= speed_paddle
            else:
                pd.pos = position
        
        elif char == 'q':
            os.system('clear')
            quit()

        elif char == 'n':
            lvl_up()

def demote_brick():
    global score
    global total_bricks

    x = ball.pos_x
    y = ball.pos_y
    vx = ball.speed_x                                                                       
    vy = ball.speed_y
    flag = 0
    x_cood = -1
    y_cood = -1
    if(vx > 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3 or grid[i][j] == UNBREAKABLE_BRICK or grid[i][j] == EXPLODING_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3 or grid[i][j] == UNBREAKABLE_BRICK or grid[i][j] == EXPLODING_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx > 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3 or grid[i][j] == UNBREAKABLE_BRICK or grid[i][j] == EXPLODING_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3 or grid[i][j] == UNBREAKABLE_BRICK or grid[i][j] == EXPLODING_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break

    if(flag == 1):
        x = brick_board[y_cood][x_cood]['x']
        y = brick_board[y_cood][x_cood]['y']
        if(brick_board[y][x]['is_rainbow'] == True):
            brick_board[y][x]['is_rainbow'] = False
        if(brick_board[y][x]['struct'] == EXPLODING_BRICK or ball.fire == True):
            os.system('aplay -q ./sounds/explosion.wav&')
            explosives = []
            explosives.append({'x':x, 'y':y})
            for k in explosives:
                y = k['y']
                x = k['x']
                for i in range(y-3,y+4,3):
                    for j in range(x-12, x+13,12):
                        if(brick_board[i][j]['struct'] == EXPLODING_BRICK and (j!=x or i!=y)):
                            explosives.append({'x':j, 'y':i})
                            continue
                        if(brick_board[i][j]['struct'] == BRICK1 or (brick_board[i][j]['struct'] == EXPLODING_BRICK and j==x and i==y)):
                            score += 1
                            brick_board[i][j]['struct'] = -1
                            total_bricks -= 1
                        elif(brick_board[i][j]['struct'] == BRICK2):
                            score += 2
                            brick_board[i][j]['struct'] = -1
                            total_bricks -= 1
                        elif(brick_board[i][j]['struct'] == BRICK3):
                            score += 3
                            brick_board[i][j]['struct'] = -1
                            total_bricks -= 1
                        elif(brick_board[i][j]['struct'] == UNBREAKABLE_BRICK):
                            brick_board[i][j]['struct'] = -1
                        if(brick_board[i][j]['is_rainbow'] == True):
                            brick_board[i][j]['is_rainbow'] = False

        elif(brick_board[y][x]['struct'] == BRICK1):
            brick_board[y][x]['struct'] = -1
            total_bricks -= 1
            os.system('aplay -q ./sounds/break.wav&')
        elif(brick_board[y][x]['struct'] == UNBREAKABLE_BRICK and ball.thru == True):
            brick_board[y][x]['struct'] = -1
            os.system('aplay -q ./sounds/break.wav&')
        elif(brick_board[y][x]['struct'] == BRICK2):
            brick_board[y][x]['struct'] = BRICK1
            os.system('aplay -q ./sounds/bounce.wav&')
        elif(brick_board[y][x]['struct'] == BRICK3):
            brick_board[y][x]['struct'] = BRICK2
            os.system('aplay -q ./sounds/bounce.wav&')

def ball_brick_collision(vx, x, vy, y):
    ball.change_speed(ball.speed_x, -1*ball.speed_y)

def check_collision_with_paddle():
    x = ball.pos_x
    y = ball.pos_y
    vx = ball.speed_x
    vy = ball.speed_y
    flag = 0
    if(vx > 0):
        for i in range(y, y+vy+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == PADDLE):
                    flag = 1
                    break
            if(flag==1):
                break
    else:
        for i in range(y, y+vy+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == PADDLE):
                    flag = 1
                    break
            if(flag==1):
                break

    if(flag == 1):
        return True
    else:
        return False

def check_collision_with_unbreakable_brick():
    x = ball.pos_x
    y = ball.pos_y
    vx = ball.speed_x
    vy = ball.speed_y
    flag = 0
    x_cood = -1
    y_cood = -1
    if(vx > 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == UNBREAKABLE_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == UNBREAKABLE_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx > 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == UNBREAKABLE_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == UNBREAKABLE_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break

    if(flag == 1):
        x1 = brick_board[y_cood][x_cood]['x']
        y1 = brick_board[y_cood][y_cood]['y']
        if(y >= y1+3 or y <= y1):
            return 2        
        else:
            return 1
    else:
        return -1

def check_collision_with_brick():
    x = ball.pos_x
    y = ball.pos_y
    vx = ball.speed_x                                                                       
    vy = ball.speed_y
    flag = 0
    x_cood = -1
    y_cood = -1
    if(vx > 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3 or grid[i][j] == EXPLODING_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3 or grid[i][j] == EXPLODING_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx > 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3 or grid[i][j] == EXPLODING_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3 or grid[i][j] == EXPLODING_BRICK):
                    flag = 1
                    x_cood = j
                    y_cood = i
                    break
            if(flag==1):
                break

    if(flag == 1):
        n = random.randint(0, len(all_power_ups)-1)
        c = all_power_ups[n]
        if(c=='ep'):
            p = ExpandPaddle()
            if(ball.speed_x != 0):
                p.set_position(x, y)
            else:
                p.set_position(x+2, y)
            power_ups.append(p)
            p.vx = ball.speed_x
            p.vy = ball.speed_y
            if(p.vy == 0):
                p.vy = -1
        elif(c=='sp'):
            p = ShrinkPaddle()
            if(ball.speed_x != 0):
                p.set_position(x, y)
            else:
                p.set_position(x+2, y)
            power_ups.append(p)
            p.vx = ball.speed_x
            p.vy = ball.speed_y
            if(p.vy == 0):
                p.vy = -1
        elif(c=='fb'):
            p = FastBall()
            if(ball.speed_x != 0):
                p.set_position(x, y)
            else:
                p.set_position(x+2, y)
            power_ups.append(p)
            p.vx = ball.speed_x
            p.vy = ball.speed_y
            if(p.vy == 0):
                p.vy = -1
        elif(c=='tb'):
            p = ThruBall()
            if(ball.speed_x != 0):
                p.set_position(x, y)
            else:
                p.set_position(x+2, y)
            power_ups.append(p)
            p.vx = ball.speed_x
            p.vy = ball.speed_y
            if(p.vy == 0):
                p.vy = -1
        elif(c=='pg'):
            p = PaddleGrab()
            if(ball.speed_x != 0):
                p.set_position(x, y)
            else:
                p.set_position(x+2, y)
            power_ups.append(p)
            p.vx = ball.speed_x
            p.vy = ball.speed_y
            if(p.vy == 0):
                p.vy = -1
        elif(c=='shp'):
            p = ShootingPaddle()
            if(ball.speed_x != 0):
                p.set_position(x, y)
            else:
                p.set_position(x+2, y)
            power_ups.append(p)
            p.vx = ball.speed_x
            p.vy = ball.speed_y
            if(p.vy == 0):
                p.vy = -1
        elif(c=='fbl'):
            p = FireBall()
            if(ball.speed_x != 0):
                p.set_position(x, y)
            else:
                p.set_position(x+2, y)
            power_ups.append(p)
            p.vx = ball.speed_x
            p.vy = ball.speed_y
            if(p.vy == 0):
                p.vy = -1

        x1 = brick_board[y_cood][x_cood]['x']
        y1 = brick_board[y_cood][y_cood]['y']
        
        if(y >= y1+3 or y <= y1):
            return 2        
        else:
            return 1
    else:
        return -1

def check_collision():
    global score
    global lives
    
    if(ball.pos_x + ball.speed_x > WIDTH-position-2):
        os.system('aplay -q ./sounds/bounce.wav&')
        ball.change_speed(-1*ball.speed_x, ball.speed_y)
    elif(ball.pos_x + ball.speed_x < position):
        os.system('aplay -q ./sounds/bounce.wav&')
        ball.change_speed(-1*ball.speed_x, ball.speed_y)
    elif(ball.pos_y + ball.speed_y < 1):
        os.system('aplay -q ./sounds/bounce.wav&')
        ball.change_speed(ball.speed_x, -1*ball.speed_y)
    elif(ball.pos_y + ball.speed_y >= 40):
        lives -= 1
        os.system('aplay -q ./sounds/lose_life.wav&')
        if(lives == 0):
            lose_game()
        ball.grab = True
        initial_pos_ball = random.randint(pd.pos, pd.pos+pd.length-2)
        ball.pos_x = initial_pos_ball
        ball.pos_y = 35
        ball.change_speed(0, ball.speed_y)
    elif(check_collision_with_paddle() == True):
        if(ball.grab_powerup == False):
            os.system('aplay -q ./sounds/bounce.wav&')
            ball.change_speed((ball.pos_x - pd.pos -(pd.length//2)-1)//2, -1*ball.speed_y)
        else:
            ball.grab = True
            ball.change_speed(0, -1*ball.speed_y)
    elif(check_collision_with_brick() != -1):
        ret = check_collision_with_brick()
        demote_brick()
        score += 1
        if(ball.thru == False):
            if(ret==1):
                ball.change_speed(-1*ball.speed_x, ball.speed_y)
            else:
                ball.change_speed(ball.speed_x, -1*ball.speed_y)
    elif(check_collision_with_unbreakable_brick() != -1):
        ret = check_collision_with_unbreakable_brick()
        if(ball.thru == False):
            os.system('aplay -q ./sounds/bounce.wav&')
            if(ret==1):
                ball.change_speed(-1*ball.speed_x, ball.speed_y)
            else:
                ball.change_speed(ball.speed_x, -1*ball.speed_y)
        else:
            demote_brick()

def check_powerups():
    global tim

    g = 2
    for i in range(len(power_ups)):
        if(power_ups[i].struct == EXPAND_PADDLE):
            if(power_ups[i].act == False):
                y = power_ups[i].y_pos
                x = power_ups[i].x_pos
                vy = power_ups[i].vy
                vx = power_ups[i].vx
                flag = 0
                if(vx > 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx > 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break

                if(flag == 1):
                    power_ups[i].activate(pd)
                    power_ups[i].set_position(-1, -1)
            elif(power_ups[i].act == True):
                if(power_ups[i].newtime + power_ups[i].total_time <= round(time.time()) - round(start_time)):
                    power_ups[i].deactivate(pd)
            
        elif(power_ups[i].struct == SHRINK_PADDLE):
            if(power_ups[i].act == False):
                y = power_ups[i].y_pos
                x = power_ups[i].x_pos
                vy = power_ups[i].vy
                vx = power_ups[i].vx
                flag = 0
                if(vx > 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx > 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break

                if(flag == 1):
                    power_ups[i].activate(pd)
                    power_ups[i].set_position(-1, -1)
            elif(power_ups[i].act == True):
                if(power_ups[i].newtime + power_ups[i].total_time <= round(time.time()) - round(start_time)):
                    power_ups[i].deactivate(pd)

        elif(power_ups[i].struct == FAST_BALL):
            if(power_ups[i].act == False):
                y = power_ups[i].y_pos
                x = power_ups[i].x_pos
                vy = power_ups[i].vy
                vx = power_ups[i].vx
                flag = 0
                if(vx > 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx > 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break

                if(flag == 1):
                    power_ups[i].activate(ball)
                    power_ups[i].set_position(-1, -1)
            elif(power_ups[i].act == True):
                if(power_ups[i].newtime + power_ups[i].total_time <= round(time.time()) - round(start_time)):
                    power_ups[i].deactivate(ball)

        elif(power_ups[i].struct == THRU_BALL):
            if(power_ups[i].act == False):
                y = power_ups[i].y_pos
                x = power_ups[i].x_pos
                vy = power_ups[i].vy
                vx = power_ups[i].vx
                flag = 0
                if(vx > 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx > 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break

                if(flag == 1):
                    power_ups[i].activate(ball)
                    power_ups[i].set_position(-1, -1)
            elif(power_ups[i].act == True):
                if(power_ups[i].newtime + power_ups[i].total_time <= round(time.time()) - round(start_time)):
                    power_ups[i].deactivate(ball)

        elif(power_ups[i].struct == PADDLE_GRAB):
            if(power_ups[i].act == False):
                y = power_ups[i].y_pos
                x = power_ups[i].x_pos
                vy = power_ups[i].vy
                vx = power_ups[i].vx
                flag = 0
                if(vx > 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx > 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break

                if(flag == 1):
                    power_ups[i].activate(ball)
                    power_ups[i].set_position(-1, -1)
            elif(power_ups[i].act == True):
                if(power_ups[i].newtime + power_ups[i].total_time <= round(time.time()) - round(start_time)):
                    power_ups[i].deactivate(ball)

        elif(power_ups[i].struct == SHOOTING_PADDLE):
            if(power_ups[i].act == False):
                y = power_ups[i].y_pos
                x = power_ups[i].x_pos
                vy = power_ups[i].vy
                vx = power_ups[i].vx
                flag = 0
                if(vx > 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx > 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break

                if(flag == 1):
                    power_ups[i].activate(pd)
                    power_ups[i].set_position(-1, -1)
            elif(power_ups[i].act == True):
                tim = power_ups[i].total_time - round(time.time()) + round(power_ups[i].newtime) + round(start_time) 
                if(power_ups[i].newtime + power_ups[i].total_time <= round(time.time()) - round(start_time)):
                    power_ups[i].deactivate(pd)
                    stop_shooting_bullets()

        elif(power_ups[i].struct == FIRE_BALL):
            if(power_ups[i].act == False):
                y = power_ups[i].y_pos
                x = power_ups[i].x_pos
                vy = power_ups[i].vy
                vx = power_ups[i].vx
                flag = 0
                if(vx > 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy >= 0):
                    for k in range(y, y+vy+g+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx > 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x, x+vx+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break
                elif(vx <= 0 and vy < 0):
                    for k in range(y+vy+g, y+1):
                        for j in range(x+vx, x+1):
                            try:
                                if(grid[k][j] == PADDLE):
                                    flag = 1
                                    break
                            except:
                                continue
                        if(flag==1):
                            break

                if(flag == 1):
                    power_ups[i].activate(ball)
                    power_ups[i].set_position(-1, -1)
            elif(power_ups[i].act == True):
                if(power_ups[i].newtime + power_ups[i].total_time <= round(time.time()) - round(start_time)):
                    power_ups[i].deactivate(ball)

def shoot_bullets():
    for i in all_bullets:
        if(i.y_pos - i.speed <= 1):
            all_bullets.remove(i)
        i.shoot_bullet()

def shoot_new_bullets():
    os.system('aplay -q ./sounds/shoot2.wav&')
    b = Bullet(pd.pos, 35)
    b.shoot_bullet()
    all_bullets.append(b)
    b = Bullet(pd.pos+pd.length-1, 35)
    b.shoot_bullet()
    all_bullets.append(b)

def drop_bombs():
    for i in all_bombs:
        if(i.y_pos - i.speed >= 41):
            all_bombs.remove(i)
        i.shoot_bomb()

def shoot_new_bombs():
    b = Bomb(pd.pos+pd.length//2)
    b.shoot_bomb()
    all_bombs.append(b)

def stop_shooting_bullets():
    all_bullets = []

def check_bullet_collision():
    global total_bricks
    global score

    for i in all_bullets:
        if(grid[i.y_pos - i.speed][i.x_pos] == BRICK1 or grid[i.y_pos - i.speed][i.x_pos] == BRICK2 or grid[i.y_pos - i.speed][i.x_pos] == BRICK3 or grid[i.y_pos - i.speed][i.x_pos] == EXPLODING_BRICK or grid[i.y_pos - i.speed][i.x_pos] == UNBREAKABLE_BRICK):
            all_bullets.remove(i)
            x = brick_board[i.y_pos - i.speed][i.x_pos]['x']
            y = brick_board[i.y_pos - i.speed][i.x_pos]['y']

            if(brick_board[y][x]['is_rainbow'] == True):
                brick_board[y][x]['is_rainbow'] = False
            if(brick_board[y][x]['struct'] == BRICK1):
                os.system('aplay -q ./sounds/break.wav&')
                brick_board[y][x]['struct'] = -1
                total_bricks -= 1
            elif(brick_board[y][x]['struct'] == BRICK2):
                brick_board[y][x]['struct'] = BRICK1
            elif(brick_board[y][x]['struct'] == BRICK3):
                brick_board[y][x]['struct'] = BRICK2
            elif(brick_board[y][x]['struct'] == EXPLODING_BRICK):
                os.system('aplay -q ./sounds/explosion.wav&')
                explosives = []
                explosives.append({'x':x, 'y':y})

                for k in explosives:
                    y = k['y']
                    x = k['x']
                    for i in range(y-3,y+4,3):
                        for j in range(x-12, x+13,12):
                            if(brick_board[i][j]['struct'] == EXPLODING_BRICK and (j!=x or i!=y)):
                                explosives.append({'x':j, 'y':i})
                                continue
                            if(brick_board[i][j]['struct'] == BRICK1 or (brick_board[i][j]['struct'] == EXPLODING_BRICK and j==x and i==y)):
                                score += 1
                                brick_board[i][j]['struct'] = -1
                                total_bricks -= 1
                            elif(brick_board[i][j]['struct'] == BRICK2):
                                score += 2
                                brick_board[i][j]['struct'] = -1
                                total_bricks -= 1
                            elif(brick_board[i][j]['struct'] == BRICK3):
                                score += 3
                                brick_board[i][j]['struct'] = -1
                                total_bricks -= 1
                            elif(brick_board[i][j]['struct'] == UNBREAKABLE_BRICK):
                                brick_board[i][j]['struct'] = -1

def check_bomb_collision():
    global lives

    for i in all_bombs:
        y = i.y_pos
        x = i.x_pos
        if(grid[y+1][x] == PADDLE):
            lives -= 1
            os.system('aplay -q ./sounds/lose_life.wav&')
            all_bombs.remove(i)
            if(lives == 0):
                lose_game()
                quit()

def check_ball_enemy_collision():
    global total_spawns

    if(ball.pos_y+ball.speed_y < 14 and ball.pos_y+ball.speed_y >= 5 and ball.pos_x+ball.speed_x >= enemy.pos_x and ball.pos_x+ball.speed_x < enemy.pos_x + 16):
        enemy.strength -=1
        os.system('aplay -q ./sounds/win.wav&')
        if(enemy.strength == 4):
            spawn_bricks()
            update_total_bricks(8)
            total_spawns += 1

        if(ball.pos_y >= 14 or ball.pos_y <= 5):
            ball.change_speed(ball.speed_x, -ball.speed_y)
        else:
            ball.change_speed(-ball.speed_x, ball.speed_y)
        if(enemy.strength == 0):
            win_game()