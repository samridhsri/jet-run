import pygame, sys
from pygame.locals import *
import random
import math

pygame.init()
screen = pygame.display.set_mode((1000, 600))

# colors
skyblue = (152, 245, 255)

BGcolor = skyblue


# defined functions
def jet():
    screen.blit(jetimg, (jetx, jety))


def building():
    screen.blit(buildimg, (buildx, buildy))


def build_flip():
    screen.blit(bfimg, (bfx, bfy))


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
jetx = 10
jety = 300
jetx_change = 0
jety_change = 0

run = True
while run:
    screen.fill(BGcolor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jety_change = -1
            if event.key == pygame.K_DOWN:
                jety_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                jety_change = 0

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