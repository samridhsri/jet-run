import pygame, sys
from pygame.locals import *
import random
import math

pygame.init()
screen = pygame.display.set_mode((1000, 600))


# defined functions
def jet():
    screen.blit(jetimg, (jetx, jety))


# jet
jetimg = pygame.image.load('jet-fighter-flipped.png')
jetx = 10
jety = 300

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        jet()
        pygame.display.update()
