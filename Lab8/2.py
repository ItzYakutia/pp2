import pygame as pg, random, time
from color_palette import *

pg.init()

SW, SH = 600, 600

CELL = 30

font = pg.font.SysFont("Verdana", 36)
font_small = pg.font.SysFont("Verdana", 60)

def draw_grid():
    for i in range(SH // 2):
        for j in range(SW // 2):
            pg.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1) #drawing screen

def draw_grid_chess(): #also
    colors = [colorWHITE, colorGRAY]

    for i in range(SH // 2):
        for j in range(SW // 2):
            pg.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pg.display.set_mode((SH, SW))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)] #firstly snake
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pg.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pg.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y)) #adding to snake body

snake = Snake()

class Food:
    def __init__(self):
        self.pos = self.generate_random_position()

    def generate_random_position(self):
        while True:
            x = random.randint(0, (SW // CELL) - 1)
            y = random.randint(0, (SH // CELL) - 1)
            if not any(part.x == x and part.y == y for part in snake.body): #checking if food was in snake
                return Point(x, y)

    def draw(self):
        pg.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


FPS = 5
clock = pg.time.Clock()

food = Food()

score = 0
level = 1

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
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

    draw_grid_chess()

    snake.move()

    # Check for border (wall) 
    head = snake.body[0]
    if head.x < 0:
        snake.dx = -1
        snake.dy = 0
    if head.x >= SW // CELL or head.y < 0 or head.y >= SH // CELL:
        screen.fill(colorRED)
        d_text = font.render(f'YOU DIED!', True, colorBLACK)
        screen.blit(d_text, (SW/2-100, SH/2))
        pg.display.update()
        time.sleep(2)
        done = True

    # Check if snake is leaving the playing area
    for part in snake.body[1:]:
        if part.x == head.x and part.y == head.y:
            screen.fill(colorRED)
            b_text = font.render(f'Dont touch the body!', True, colorBLACK)
            screen.blit(b_text, (SW/2-200, SH/2))
            pg.display.update()
            time.sleep(2)
            done = True

    snake.check_collision(food)

    # Generate new food position 
    if head.x == food.pos.x and head.y == food.pos.y:
        score += 1
        if score % 3 == 0:  # Increase level every 3 foods
            level += 1
            FPS += 0  # Increase speed 
        food.pos = food.generate_random_position()
        if food.pos in snake.body: #also checking if food in snake
            food.pos = food.generate_random_position()
            
    c_text = font.render(f'Food: {score}', True, colorBLACK) #score counter
    levelk = font.render(f'Level: {FPS - 5}', True, colorBLACK) #level counter
    screen.blit(levelk, (0, 30))
    screen.blit(c_text, (0, 0))
    snake.draw()
    food.draw()
    
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
