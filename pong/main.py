"""Pong!"""

___name___         = "Pong"
___license___      = "MIT"
___categories___   = ["Games"]
___dependencies___ = ["dialogs", "app", "ugfx_helper", "random", "sleep", "buttons"]

import math, ugfx, ugfx_helper, random, sleep, buttons, time
from tilda import Buttons

ugfx_helper.init()

SCREEN_WIDTH = ugfx.width()
SCREEN_HEIGHT = ugfx.height()

bgColor = ugfx.BLACK
ballColor = ugfx.html_color(0x00FF00)
paddleColor = ugfx.html_color(0x00FF00)

class Paddle():
    height = 10
    width = 40

    moveSpeed = 4

    def __init__(self, type):
        self.type = type

        self.x = SCREEN_WIDTH/2

        if type == 0:
            self.y = 15
        else:
            self.y = SCREEN_HEIGHT - 15

    def draw(self, color):
        ugfx.area(int(self.x-self.width/2),int(self.y-self.height/2),int(self.width),int(self.height),color)

    def update(self):
        if self.type == 1:
            if Buttons.is_pressed(Buttons.BTN_Hash):
                self.x += self.moveSpeed
            if Buttons.is_pressed(Buttons.BTN_Star):
                self.x -= self.moveSpeed
        if self.type == 0:
            if Buttons.is_pressed(Buttons.BTN_3):
                self.x += self.moveSpeed
            if Buttons.is_pressed(Buttons.BTN_1):
                self.x -= self.moveSpeed

class Ball():
    size = 10

    x = 0
    y = 0

    def __init__(self):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2

        self.vX = 3
        self.vY = 3

    def draw(self, color):
        ugfx.area(int(self.x-self.size/2),int(self.y-self.size/2),int(self.size),int(self.size),color)

    def update(self):
        self.x += self.vX
        self.y += self.vY

        if self.x > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH
            self.vX = -self.vX

        if self.x < 0:
            self.x = 0
            self.vX = -self.vX

        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            self.vY = -self.vY

        if self.y < 0:
            self.y = 0
            self.vY = -self.vY


def one_round():
    ball = Ball()
    topPaddle = Paddle(0)
    bottomPaddle = Paddle(1)

    ugfx.clear(bgColor)
    ugfx.backlight(100)

    while True:
        ball.draw(bgColor)
        topPaddle.draw(bgColor)
        bottomPaddle.draw(bgColor)

        ball.update()
        topPaddle.update()
        bottomPaddle.update()

        ball.draw(ballColor)
        topPaddle.draw(paddleColor)
        bottomPaddle.draw(paddleColor)

        time.sleep_ms(10)

playing = 1
while playing:
    score = one_round()
    ugfx.area(0,0,ugfx.width(),ugfx.height(),0)
    ugfx.text(30, 30, "GAME OVER Score: %d" % (score), 0xFFFF)
    ugfx.text(30, 60, "Press A to play again", 0xFFFF)
    ugfx.text(30, 90, "Press MENU to quit" , 0xFFFF)
    while True:
        sleep.wfi()
        if buttons.is_triggered(Buttons.BTN_A):
            break

        if buttons.is_triggered(Buttons.BTN_Menu):
            playing = 0
            break

app.restart_to_default()



#def one_round():
#    grid_size = 8;
#    body_colour = ugfx.RED
#    back_colour = 0;
#    food_colour = ugfx.YELLOW
#    wall_colour = ugfx.BLUE
#    score = 0;
#    edge_x = math.floor(ugfx.width()/grid_size)-2;
#    edge_y = math.floor(ugfx.height()/grid_size)-2;

#    def disp_square(x,y,colour):
#        ugfx.area((x+1)*grid_size, (y+1)*grid_size, grid_size, grid_size, colour)

#    def disp_body_straight(x,y,rotation,colour):
#        if (rotation == 0):
#            ugfx.area((x+1)*grid_size+1, (y+1)*grid_size+1, grid_size-2, grid_size, colour)
#        elif (rotation == 90):
#            ugfx.area((x+1)*grid_size+1, (y+1)*grid_size+1, grid_size, grid_size-2, colour)
#        elif (rotation == 180):
#            ugfx.area((x+1)*grid_size+1, (y+1)*grid_size-1, grid_size-2, grid_size, colour)
#        else:
#            ugfx.area((x+1)*grid_size-1, (y+1)*grid_size+1, grid_size, grid_size-2, colour)

#    def disp_eaten_food(x,y,colour):
#        ugfx.area((x+1)*grid_size, (y+1)*grid_size, grid_size, grid_size, colour)

#    def randn_square():
#        return  [random.randrange(edge_x), random.randrange(edge_y)]

#    body_x = [12,13,14,15,16]
#    body_y = [2,2,2,2,2]

#    ugfx.area(0,0,ugfx.width(),ugfx.height(),0)

#    ugfx.area(0,0,grid_size*(edge_x+1),grid_size,wall_colour)
#    ugfx.area(0,0,grid_size,grid_size*(edge_y+1),wall_colour)
#    ugfx.area(grid_size*(edge_x+1),0,grid_size,grid_size*(edge_y+1),wall_colour)
#    ugfx.area(0,grid_size*(edge_y+1),grid_size*(edge_x+2),grid_size,wall_colour)

#    keepgoing = 1;

#    food = [20,20]
#    disp_square(food[0],food[1],food_colour)

#    dir_x = 1
#    dir_y = 0
#    orient = 270

#    #for i in range(0,len(body_x)):
#    #   disp_body_straight(body_x[i],body_y[i],orient,body_colour)

#    while keepgoing:
#        if dir_x != -1 and (Buttons.is_pressed(Buttons.JOY_Right) or Buttons.is_pressed(Buttons.BTN_6)):
#            dir_x = 1;
#            dir_y = 0;
#            orient = 270
#        elif dir_x != 1 and (Buttons.is_pressed(Buttons.JOY_Left) or Buttons.is_pressed(Buttons.BTN_4)):
#            dir_x = -1;
#            dir_y = 0;
#            orient = 90
#        elif dir_y != -1 and (Buttons.is_pressed(Buttons.JOY_Down) or Buttons.is_pressed(Buttons.BTN_8)):
#            dir_y = 1;
#            dir_x = 0;
#            orient = 180
#        elif dir_y != 1 and (Buttons.is_pressed(Buttons.JOY_Up) or Buttons.is_pressed(Buttons.BTN_0)):
#            dir_y = -1;
#            dir_x = 0;
#            orient = 0

#        body_x.append(body_x[-1]+dir_x)
#        body_y.append(body_y[-1]+dir_y)

#        for i in range(0,len(body_x)-1):
#            if (body_x[i] == body_x[-1]) and (body_y[i] == body_y[-1]):
#                keepgoing = 0

#        if not((body_x[-1] == food[0]) and (body_y[-1] == food[1])):
#            x_del = body_x.pop(0)
#            y_del = body_y.pop(0)
#            disp_eaten_food(x_del,y_del,back_colour)
#        else:
#            disp_eaten_food(food[0],food[1],body_colour)
#            food = randn_square()
#            disp_square(food[0],food[1],food_colour)
#            score = score + 1

#        disp_body_straight(body_x[-1],body_y[-1],orient,body_colour)


#        if ((body_x[-1] >= edge_x) or (body_x[-1] < 0) or (body_y[-1] >= edge_y) or (body_y[-1] < 0)):
#            break

#        sleep.sleep(0.1)
#    return score





