import pygame
import sys
import time
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")

clock = pygame.image.load("Lab7/mainclock.png")
left = pygame.image.load("Lab7/leftarm.png")
right = pygame.image.load("Lab7/rightarm.png")

clock_rect = clock.get_rect(center=(WIDTH // 2, HEIGHT // 2))
left_rect = left.get_rect(center=(WIDTH // 2, HEIGHT // 2))
right_rect = right.get_rect(center=(WIDTH // 2, HEIGHT // 2))

clock60 = dict(zip(range(60), range(0, 360, 6)))

while True:
    current_time = datetime.now()
    minute = current_time.minute
    second = current_time.second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    screen.blit(clock, clock_rect)

    rotated_left = pygame.transform.rotate(left, -clock60[minute])
    left_rect = rotated_left.get_rect(center=left_rect.center)
    screen.blit(rotated_left, left_rect)

    rotated_right = pygame.transform.rotate(right, -clock60[second] + 90)
    right_rect = rotated_right.get_rect(center=right_rect.center)
    screen.blit(rotated_right, right_rect)

    pygame.display.flip()
    time.sleep(1)  
