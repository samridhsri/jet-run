import pygame, sys
from pygame.locals import *
import random
import math

pygame.init()
screen = pygame.display.set_mode((1000, 600))

# colors
skyblue = (152, 245, 255)

sky = pygame.image.load('sky.jpg')
sky = pygame.transform.scale(sky, (1000,710))
skyx = 0
skyx2 = sky.get_width()


# defined functions
def jet():
    screen.blit(jetimg, (jetx, jety))


def building():
    screen.blit(buildimg, (buildx, buildy))


def build_flip():
    screen.blit(bfimg, (bfx, bfy))

def redrawWindow():
    screen.blit(sky, (skyx, 0))
    screen.blit(sky, (skyx2, 0))
    


# building
buildimg = pygame.image.load('office-building.png')
buildx = 200
buildy = 300

# building-flip
bfimg = pygame.image.load('office-building-flip.png')
bfx = 650
bfy = -200

# jet
jetimg = pygame.image.load('jet-fighter-flipped.png')
jetx = 35
jety = 300
jetx_change = 0
jety_change = 0


pygame.time.set_timer(USEREVENT+1, 500)
speed = 30
run = True
while run:
    redrawWindow()
    skyx -= 1.5
    skyx2 -= 1.5
    if skyx < sky.get_width() * (-1):
        skyx = sky.get_width()
    if skyx2 <sky.get_width() * (-1):
        skyx2 = sky.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jety_change = -3
            if event.key == pygame.K_DOWN:
                jety_change = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                jety_change = 0
                
        if event.type == USEREVENT+1:
            speed += 6
    pygame.time.Clock().tick(speed)

    # jet movement
    jety = jety + jety_change

    # Jet boundaries
    if jety <= 0:
        jety = 0
    elif jety >= 530:
        jety = 530

    jet()
    building()
    build_flip()
    pygame.display.update()
