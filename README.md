# DASS Assignment II
## Brick Breaker Game
#### Roll no. : 2019111039

### Install dependencies
```bash
$ pip3 install colorama
```
### Run the game
```bash
$ python3 main.py
```
### Guide to the game
i) Use 'A' and 'D' keys to move the paddle to left and right <br />
ii) Use 'S' to launch the ball <br />
iii) Initially you have 10 balls. Each time you hit the ground, you will lose one ball <br />
iv) There are 3 levels <br />
v) Use 'N' to skip levels <br />
iv) You need to break all the breakable bricks before the balls get over to move to next level <br />
v) There are different powerups to aid you in the game <br />
vi) You need to beat the UFO in the third level to win the game <br />

### OOPS concepts used in the game

- Inheritance
Parent class - Brick
Children classes - Unbreakable brick, Brick1, Brick2, Brick3, Rainbow Brick, Explosive brick, 
Parent class - Powerups
Children classes - Expand Paddle, Shrink Paddle, Ball Multiplier, Fast Ball, Tru Ball, Paddle Grab, Shooting Paddle, Fireball
- Polymorphism
Parent class - Powerups
Children classes - Expand Paddle, Shrink Paddle, Ball Multiplier, Fast Ball, Tru Ball, Paddle Grab
Functions overridden - activate(), deactivate()
- Encapsulation
Classes - Paddle, Ball. PowerUps, Bricks, Bullets, Bomb, Boss
- Abstraction
Examples: 
powerups[i].activate()
ball.change_speed()
brick.create_brick()
brick.update_coordinates()
check_powerups()
create_floor()
create_ceil()
