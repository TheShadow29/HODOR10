#Code by Umut Bilgic, Ankara, Turkey.
#Public release: 11/16/2013
#Release version: 1.1 Beta - Working coin and point system.

from pygame.locals import *
import pygame
import sys
import time
import random
import math

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((1200,700), 0, 32)
bgImg = pygame.image.load('city_2.png')
direction = 'right'

execfile('sprites.py')
WHITE = (255, 255, 255)
a=0
b=0
ben = [sprites(a,b,'Images/sprites/ben_walk_right_FILES/0.png'), 
       sprites(a,b,'Images/sprites/ben_walk_right_FILES/1.png'),
       sprites(a,b,'Images/sprites/ben_walk_right_FILES/2.png'),
       sprites(a,b,'Images/sprites/ben_walk_right_FILES/3.png'),
       sprites(a,b,'Images/sprites/ben_walk_right_FILES/4.png'),
       sprites(a,b,'Images/sprites/ben_walk_right_FILES/5.png'),
       sprites(a,b,'Images/sprites/ben_walk_right_FILES/6.png'),
       sprites(a,b,'Images/sprites/ben_walk_right_FILES/7.png')]

pygame_img = None
bgx = 10
bgy = 10
index = 0
while True:
    DISPLAYSURF.fill(WHITE)
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    DISPLAYSURF.blit(bgImg,(bgx,bgy))
    pygame_img = ben[index%4].image

    if keys[pygame.K_RIGHT]:
        bgx-=8
        index+=1
        pygame_img = ben[index%4].image
    elif keys[pygame.K_LEFT]:
        bgx+=8
    DISPLAYSURF.blit(pygame_img,(330,500))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)