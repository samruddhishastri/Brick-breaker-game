from utility import *

create_board()
create_all_bricks_lvl1()

t = 0

while True:
    newtime = round(time.time()) - round(start_time)
    update_cursor(0,0)
    screen_time=time.time()
    create_ceil()
    show_bricks()
    pd.print_paddle()
    create_side_walls()
    create_floor()
    for i in range(len(power_ups)):
        power_ups[i].print_powerup()
    if(pd.shooting == True):
        shoot_bullets()
        if(t%15 == 0):
            shoot_new_bullets()
    t+=1
    ball.print_ball()
    m = print_header(newtime)
    if(m == 2):
        break
    print_grid()
    time.sleep(0.03)
    check_powerups()
    check_collision()
    check_bullet_collision()
    move_paddle()
    clear_grid()

os.system('clear')
stop_shooting_bullets()
deactivate_all_powerups()
clear_grid()
reset_brick_board()
reinitialise()
create_all_bricks_lvl2()
update_total_bricks(24)

t = 0

while True:
    newtime = round(time.time()) - round(start_time)
    update_cursor(0,0)
    screen_time=time.time()
    create_ceil()
    show_bricks()
    pd.print_paddle()
    create_side_walls()
    create_floor()
    for i in range(len(power_ups)):
        power_ups[i].print_powerup()
    if(pd.shooting == True):
        shoot_bullets()
        if(t%15 == 0):
            shoot_new_bullets()
    t+=1
    ball.print_ball()
    m = print_header(newtime)
    if(m == 3):
        break
    print_grid()
    time.sleep(0.03)
    check_powerups()
    check_collision()
    check_bullet_collision()
    move_paddle()
    clear_grid()

os.system('clear')
stop_shooting_bullets()
deactivate_all_powerups()
clear_grid()
reset_brick_board()
reinitialise()
create_boss()
add_few_unbreakable_bricks()

t = 0

while True:
    newtime = round(time.time()) - round(start_time)
    update_cursor(0,0)
    screen_time=time.time()
    create_ceil()
    show_bricks_lvl3()
    pd.print_paddle()
    create_side_walls()
    create_floor()
    create_boss()
    drop_bombs()
    if(t%30 == 0):
        shoot_new_bombs()
    t+=1
    ball.print_ball()
    m = print_header(newtime)
    if(m == 4):
        break
    print_grid()
    time.sleep(0.03)
    check_collision()
    check_ball_enemy_collision()
    check_bomb_collision()
    move_paddle()
    clear_grid()

os.system('clear')
