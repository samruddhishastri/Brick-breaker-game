from headers import *
from paddle import *
from ball import *
from bricks import *

os.system('clear')
pd = Paddle(initial_pos_pd, 15)
ball = Ball(initial_pos_ball)

initial_speed_y = -2
speed_paddle = 4

def move_paddle():
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=0.08):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    INPUT_CHAR = user_input()
    char=INPUT_CHAR

    if(ball.grab == True):
        if char == 'd':
            if(pd.pos + pd.length + speed_paddle < WIDTH-position+1):
                pd.pos += speed_paddle
                ball.pos_x += speed_paddle
            else:
                ball.pos_x += (WIDTH-position+1) - (pd.pos + pd.length)
                pd.pos += (WIDTH-position+1) - (pd.pos + pd.length)

        elif char == 'a':
            if(pd.pos-speed_paddle> position):
                pd.pos -= speed_paddle
                ball.pos_x -= speed_paddle
            else:
                ball.pos_x -= pd.pos - position
                pd.pos -= (pd.pos - position)

        elif char == ' ':
            ball.change_speed((ball.pos_x - pd.pos -(pd.length//2)-1)//2, initial_speed_y)
            ball.grab = False

        elif char == 'q':
            #os.system('clear')
            quit()
    else:
        if char == 'd':
            if(pd.pos + pd.length+speed_paddle < WIDTH-position + 1):
                pd.pos += speed_paddle
            else:
                pd.pos = WIDTH-position + 1 - pd.length

        elif char == 'a':
            if(pd.pos - speed_paddle > position):
                pd.pos -= speed_paddle
            else:
                pd.pos = position

        elif char == 'q':
            #os.system('clear')
            quit()

def demote_brick(y1,x1):
    x = brick_board[y1][x1]['x']
    y = brick_board[y1][x1]['y']
    if(brick_board[y][x]['struct'] == BRICK1):
        brick_board[y][x]['struct'] = -1
    if(brick_board[y][x]['struct'] == BRICK2):
        brick_board[y][x]['struct'] = BRICK1
    if(brick_board[y][x]['struct'] == BRICK3):
        brick_board[y][x]['struct'] = BRICK2

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
    if(vx > 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == UNBREAKABLE_BRICK):
                    flag = 1
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == UNBREAKABLE_BRICK):
                    flag = 1
                    break
            if(flag==1):
                break
    elif(vx > 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == UNBREAKABLE_BRICK):
                    flag = 1
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == UNBREAKABLE_BRICK):
                    flag = 1
                    break
            if(flag==1):
                break

    if(flag == 1):
        return True
    else:
        return False

def check_collision_with_brick():
    x = ball.pos_x
    y = ball.pos_y
    vx = ball.speed_x
    vy = ball.speed_y
    flag = 0
    if(vx > 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3):
                    flag = 1
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy >= 0):
        for i in range(y, y+vy+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3):
                    flag = 1
                    break
            if(flag==1):
                break
    elif(vx > 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x, x+vx+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3):
                    flag = 1
                    break
            if(flag==1):
                break
    elif(vx <= 0 and vy < 0):
        for i in range(y+vy, y+1):
            for j in range(x+vx, x+1):
                if(grid[i][j] == BRICK1 or grid[i][j] == BRICK2 or grid[i][j] == BRICK3):
                    flag = 1
                    break
            if(flag==1):
                break
    if(flag == 1):
        return True
    else:
        return False

def check_collision():
    global score
    if(ball.pos_x + ball.speed_x > WIDTH-position+1):
        ball.change_speed(-1*ball.speed_x, ball.speed_y)
    elif(ball.pos_x + ball.speed_x < position):
       ball.change_speed(-1*ball.speed_x, ball.speed_y)
    elif(ball.pos_y + ball.speed_y < 1):
       ball.change_speed(ball.speed_x, -1*ball.speed_y)
    elif(ball.pos_y + ball.speed_y >= 40):
        ball.change_speed(ball.speed_x, -1*ball.speed_y)
    elif(check_collision_with_paddle() == True):
        ball.change_speed((ball.pos_x - pd.pos -(pd.length//2)-1)//2, -1*ball.speed_y)
    elif(check_collision_with_brick() == True):
        demote_brick(ball.pos_y+ball.speed_y, ball.pos_x+ball.speed_x)
        score += 1
        ball.change_speed(ball.speed_x, -1*ball.speed_y)
    elif(check_collision_with_unbreakable_brick() == True):
        ball.change_speed(ball.speed_x, -1*ball.speed_y)

create_board()
create_all_bricks()

while True:
    newtime = round(time.time()) - round(start_time)
    update_cursor(0,0)
    screen_time=time.time()
    create_ceil()
    show_bricks()
    ball.print_ball()
    pd.print_paddle()
    create_side_walls()
    create_floor()
    print_header(newtime, score)
    print_grid()
    time.sleep(0.03)
    move_paddle()
    check_collision()
    clear_grid()