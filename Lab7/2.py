import pygame as pg
import os
import re

pg.init()

def resize_image(image_path, width, height):
    image = pg.image.load(image_path)
    resized_image = pg.transform.scale(image, (width, height))
    return resized_image

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Resized Image')

image_path = 'Lab7/font.png'
resized_image = resize_image(image_path, 250, 200)

def theme():
    screen.blit(resized_image, (20, 20))

    font = pg.font.SysFont('calisto ', 36)
    screen.blit(font.render("Music time", True, (88, 127, 64)), (350, 110))

    pg.draw.rect(screen, (0, 0, 0), pg.Rect(20, 275, 160, 115))
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(180, 340, 400, 40))
    
    font = pg.font.SysFont('arial', 15)
    manual = "SPACE to start and pause_press   '->' next song_<-' previous song"
    point = 280
    for i in manual.split('_'):
        m = font.render(i, True, (88, 127, 64))
        if 'press' in i or 'SPACE' in i: screen.blit(m, (30, point))
        else: screen.blit(m, (70, point))
        point += 20

def get_path(path):
    canon_path = path.replace('/',os.sep).replace('\\',os.sep)
    return canon_path

def track_name(playlist, track, screen):
    font = pg.font.SysFont('gillsans', 19)
    track_name = playlist[track]
    track_name = re.sub('.ogg', '', track_name)
    track_name = re.sub('.mp3', '', track_name) 
    screen.blit(font.render(track_name, True, (88, 127, 64)), (190, 340))

def next_song(track, playlist, state):
    if state:
        if track != len(playlist) - 1: track += 1
        else: track = 0
    else:
        if track != 0: track -= 1 
        else: track = len(playlist) - 1
    return track

def load_new_song(track, playlist):
    pg.mixer.music.load(get_path(f'Lab7/mus/{playlist[track]}'))
    pg.mixer.music.play(0)

screen = pg.display.set_mode((600, 400))
pg.display.set_caption('Music Player')
playlist = [i for i in os.listdir('Lab7/mus') if '.ogg' in i or '.mp3' in i]
track = 0

run = True 
play = False

while run:
    theme()
    track_name(playlist, track, screen)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
        if i.type == pg.KEYDOWN: 
            if i.key == pg.K_SPACE:
                if not play: 
                    load_new_song(track, playlist)
                else: pg.mixer.music.pause()
                play = not play
            if i.key == pg.K_RIGHT and play:
                track = next_song(track, playlist, True)
                load_new_song(track, playlist)
            if i.key == pg.K_LEFT and play:
                track = next_song(track, playlist, False)
                load_new_song(track, playlist)
        if pg.mixer.music.get_busy() == False and play:
            track = next_song(track, playlist, True)
            load_new_song(track, playlist)
    pg.display.update()