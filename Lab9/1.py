import sys, random, time
import pygame as pg
from pygame.locals import *


pg.init()

SW = 400
SH = 600
screen = pg.display.set_mode((SW, SH)) #window mode
FPS = 60
FPSs = pg.time.Clock()
speed = 5
score = 0

BLUE  = (0, 0, 255) #colors
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pg.font.SysFont("Verdana", 36)
font_small = pg.font.SysFont("Verdana", 60)

background = pg.image.load("Lab9/AnimatedStreet.png") 

pg.display.set_caption("Racer")

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("Lab9/Player.png")
        self.rect = self.image.get_rect() #geting rect for image
        self.rect.center = (160, 520)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        pressed_keys = pg.key.get_pressed()
         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0) #moving to left
        if self.rect.right < SW:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
"""
        if self.rect.bottom < SH:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
"""    
  
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Lab9/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(160, SW-160), 0)
    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > SH):
            global score 
            score += 1    #summizing to score
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Lab9/gold.png")
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(22, 378), 520)  #spawning in random positon in line with car
    def draw(self, screen):
        screen.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
C = Coin()
k = 0
rapid = 30 #creating a value if coins > rapid then speed is increases
#speed_inc = pg.USEREVENT + 1
#pg.time.set_timer(speed_inc, 1000)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if k > rapid: #increases enemy's speed if k > rapid
        speed += 1
        rapid += 30
    E1.move()       
     
    screen.fill(WHITE)
    screen.blit(background, (0,0))
    scores = font_small.render(str(score), True, BLACK)
    if score < 10: screen.blit(scores, (360, 0)) #place the score counter on screen 
    else: screen.blit(scores, (325, 0)) #another place if score > 10
    P1.draw(screen)
    E1.draw(screen)
    C.draw(screen)
    P1.update()
    
 

    
    if pg.sprite.collide_rect(P1, C):
        k += random.randint(1,9)
        C.rect.center = (random.randint(22, 378), 520)
    c_text = font.render(f'Coins: {k}', True, BLACK)
    screen.blit(c_text, (0, 0)) #showint coins
 
    if pg.sprite.collide_rect(P1, E1):
        screen.fill(RED)
        d_text = font.render(f'YOU DIED!', True, BLACK)
        screen.blit(d_text, (SW/2-100, SH/2)) #showing text if enemy car crashing with player
        pg.display.update()
        time.sleep(2)
        pg.quit()
        sys.exit()
        
    pg.display.update()
    FPSs.tick(FPS)


