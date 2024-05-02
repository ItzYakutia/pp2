import pygame as pg
from random import randint
from functions import *
import time, psycopg2
from color_palette import *

nick = input('Choose your nickname:\n')
prev_stat(nick)

pg.init()

def drawGrid():
    for x in range(0, SW, CELL):
        for y in range(0, SH, CELL):
            rect = pg.Rect(x, y, CELL, CELL)
            pg.draw.rect(screen, colorSOGREEN, rect, 1)

def win():
    check_existence(nick, level.cnt, level.level_count)
    screen.fill((0, 0, 0))
    text = font1.render('YOU WIN!', True, (colorBLUE))
    text1 = font1.render(f'Level: {level.level_count}', True, (colorBLUE))
    text2 = font1.render(f'Score: {cnt}', True, (colorBLUE))
    screen.blit(text, (175, 200))
    screen.blit(text1, (175, 260))
    screen.blit(text2, (175, 320))
    pg.display.update()

#shows the current score if player leaves the game before loses or wins
def show_the_score():
    screen.fill((0, 0, 0))
    text = font1.render('Come again!', True, (colorBLUE))
    text3 = font2.render(f'{nick}', True, (colorBLUE))
    text1 = font1.render(f'Level: {level.level_count}', True, (colorBLUE))
    text2 = font1.render(f'Score: {cnt}', True, (colorBLUE))
    screen.blit(text3, (250, 200))
    screen.blit(text, (125, 125))
    screen.blit(text1, (175, 260))
    screen.blit(text2, (175, 320))
    pg.display.update()

def pause():
    screen.fill((0, 0, 0))
    text = font1.render('Pause...', True, (colorBLUE))
    text1 = font1.render(f'Level: {level.level_count}', True, (colorBLUE))
    text2 = font1.render(f'Score: {cnt}', True, (colorBLUE))
    screen.blit(text, (175, 200))
    screen.blit(text1, (175, 260))
    screen.blit(text2, (175, 320))
    pg.display.update()


def game_over():
    check_existence(nick, level.cnt, level.level_count)
    screen.fill((0, 0, 0))
    text = font1.render('Ur died', True, (colorBLUE))
    text1 = font1.render(f'Level: {level.level_count}', True, (colorBLUE))
    text2 = font1.render(f'Score: {cnt}', True, (colorBLUE))
    screen.blit(text, (175, 200))
    screen.blit(text1, (175, 260))
    screen.blit(text2, (175, 320))
    pg.display.update()

class level_and_cnt: #remembers and shows the current level and score
    def __init__(self, level):
        self.level_count = level
        self.cnt = 0

    def draw(self, cnt):
        self.cnt = cnt
        font = pg.font.SysFont('Verdana', 30)
        text = font.render(f'Level: {self.level_count} Score: {self.cnt}', True, (colorBLACK))
        screen.blit(text, (7, 565))

class Snake(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = [[10, 10]]
        self.dx = 0
        self.dy = 0

    def move(self): #motion of the snake
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]

        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 

        if self.body[0][0] * CELL > SW - 1:
            self.body[0][0] = 0
        if self.body[0][1] * CELL > SH - 1:
            self.body[0][1] = 0
        if self.body[0][0] < 0:
            self.body[0][0] = SW / CELL
        if self.body[0][1] < 0:
            self.body[0][1] = SH / CELL
        
        for i in range(len(self.body) - 1, 0, -1):
            if self.body[0][0] == self.body[i][0]:
                if self.body[0][1] == self.body[i][1]:
                    global run 
                    run = not run
                    
    def check_collision(self, food): #checks whether snake picks up the food
        global cnt
        point = self.body[0]
        a, b = food.rect.topleft
        if point[0] * CELL == a and point[1] * CELL == b:
            self.body.append([a, b])
            food.change_location()
            cnt += randint(1, 3)

    def draw(self): #draws the snake (head and body separately)
        point = self.body[0]
        rect = pg.Rect(CELL * point[0], CELL * point[1], CELL, CELL)
        pg.draw.rect(screen, (128, 0, 255), rect)

        for point in self.body[1:]:
            rect = pg.Rect(CELL * point[0], CELL * point[1], CELL, CELL)
            pg.draw.rect(screen, (50, 128, 128), rect)

class Food(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pg.Surface((CELL, CELL))
        self.surface.fill((0, 255, 0))
        self.rect = self.surface.get_rect(topleft = (CELL * randint(0, 19), CELL * randint(0, 19)))
    
    def change_location(self):
        global last_tick
        self.rect.topleft = (CELL * randint(0, 19), CELL * randint(0, 19))
        last_tick = ticks

    def not_in_wall(self, wall):
        wall_coordinates = []
        a, b = self.rect.topleft
        for border in wall.body:
            x = border[0] * CELL
            y = border[1] * CELL
            wall_coordinates.append([x, y])
        if [a, b] in wall_coordinates:
            return False
        return True

    def not_in_snake(self, snake): #check whether food is spawned in the snake
        snake_coordinates = []
        a, b = self.rect.topleft
        for body in snake.body:
            x = body[0] * CELL
            y = body[1] * CELL
            snake_coordinates.append([x, y])
        if [a, b] in snake_coordinates:
            return False
        return True

    def draw(self):
        screen.blit(self.surface, self.rect)

class Wall(pg.sprite.Sprite):
    def __init__(self, level): #initializing the wall by using txt file
        super().__init__()
        self.body = []
        f = open("Lab10/level/L{}.txt".format(level), "r")

        for y in range(0, SH//CELL + 1):
            for x in range(0, SW//CELL + 1):
                if f.read(1) == '#':
                    self.body.append([x, y])

    def collision(self, snake): #checks whether snake collided in the wall
        a, b = snake.body[0]
        for border in wall.body:
            if border[0] == a and border[1] == b:
                game_over()
                time.sleep(2)
                global run
                run = not run

    def draw(self): #draws the wall on the screen
        for point in self.body:
            rect = pg.Rect(CELL * point[0], CELL * point[1], CELL, CELL)
            pg.draw.rect(screen, (255, 255, 0), rect)


SH, SW = 600, 600
cnt, lvl = 0, 1
CELL = 30
run, stop = True, False

pg.display.set_caption('Snake')
screen = pg.display.set_mode((SW, SH))
screen.fill((0, 0, 0))
clock = pg.time.Clock()

font1 = pg.font.SysFont('Verdana', 60)
font2 = pg.font.SysFont('Verdana', 36)

#initializing all the classes
snake = Snake()
food = Food()
wall = Wall(lvl)
level = level_and_cnt(lvl)
last_tick, k = 0, 0
win_score = [6, 12, 18, 24] #the score that player need to get to pass the level
fps = [5.5, 6, 6.25, 6.5] #changes the speed at each level
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            check_existence(nick, level.cnt, level.level_count)
            if level.cnt == 0: check_existence(nick, level.cnt, 1)
            show_the_score()
            time.sleep(2)
            run = not run
        if event.type == pg.KEYDOWN: #moving by arrows
            if event.key == pg.K_SPACE: #pause
                check_existence(nick, level.cnt, level.level_count)
                stop = not stop
            if event.key == pg.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pg.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pg.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pg.K_UP:
                snake.dx = 0
                snake.dy = -1

    if stop: pause()
    else:
        snake.move() #changes the location of the snake
        wall.collision(snake) #stops the game if snake collided in the wall
        snake.check_collision(food) #food eating and snake's growth

        ticks = pg.time.get_ticks()
        if ticks - last_tick > 5000: #changes the location of the food after 5 seconds
            food.change_location()

        while not food.not_in_wall(wall): #makes sure the food isn't spawned in the wall
            food.change_location()

        while not food.not_in_snake(snake): #makes sure the food isn't spawned in the snake's body
            food.change_location()

        if len(snake.body) > win_score[lvl - 1]:
            lvl += 1
            k += 1
            if lvl == 5: 
                win()
                time.sleep(2)
                run = not run 
            snake = Snake()
            wall = Wall(lvl)
            level = level_and_cnt(lvl)

        screen.fill((colorBLUE))
        drawGrid()  

        snake.draw() 
        food.draw() 
        wall.draw()
        level.draw(cnt)

        pg.display.update()
    clock.tick(fps[k])
    