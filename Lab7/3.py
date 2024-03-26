import pygame as pg

pg.init()

clock = pg.time.Clock()

W, H = 750, 750
screen = pg.display.set_mode((W, H))
almostWhite = (88, 127, 64)
red = (255, 0, 0)
step = 20
x, y = 50, 50
r = 25
screen.fill(almostWhite)

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            quit()
            
    key = pg.key.get_pressed()
    
    dx, dy = 0, 0
    
    if key[pg.K_UP] or key[pg.K_w]:
        dy = -1
    if key[pg.K_DOWN] or key[pg.K_s]:
        dy = 1
    if key[pg.K_LEFT] or key[pg.K_a]:
        dx = -1
    if key[pg.K_RIGHT] or key[pg.K_d]:
        dx = 1
    
    x += step * dx
    y += step * dy
    
    x = max(r, min(x, W - r))
    y = max(r, min(y, H - r))
    
    screen.fill(almostWhite)
    pg.draw.circle(screen, red, (x, y), r)
    
    pg.display.flip()
    clock.tick(60)
