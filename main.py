import pygame, sys
from pygame.locals import *
import random
import math

pygame.init()
screen = pygame.display.set_mode((1000, 600))

#colors
skyblue = (152,245,255)


BGcolor = skyblue

# defined functions
def jet():
    screen.blit(jetimg, (jetx, jety))

def building():
    screen.blit(buildimg, (buildx, buildy))

def build_flip():
    screen.blit(bfimg, (bfx, bfy))

#building
buildimg = pygame.image.load('office-building.png')
buildx = 150
buildy = 300

#building-flip
bfimg = pygame.image.load('office-building-flip.png')
bfx = 600
bfy = -200

# jet
jetimg = pygame.image.load('jet-fighter-flipped.png')
jetx = 10
jety = 300

screen.fill(BGcolor)
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        jet()
        building()
        build_flip()
    pygame.display.update()
