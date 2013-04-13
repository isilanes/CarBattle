import sys
import time
import pygame

from libcb import core

#------------------------------------------------------------------------------#

# Initialize:
pygame.init()

size = width, height = 900, 450
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
grey = 100, 100, 100
bg = grey

screen = pygame.display.set_mode(size)

car1, car1_r = core.load_car_png("amarillo100x50.png")

# Run loop:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move car:
    car1_r = car1_r.move(speed)
    if car1_r.left < 0 or car1_r.right > width:
        speed[0] = -speed[0]
    if car1_r.top < 0 or car1_r.bottom > height:
        car1 = pygame.transform.rotate(car1, 15)
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(car1, car1_r)
    pygame.display.flip()
    time.sleep(0.05)
