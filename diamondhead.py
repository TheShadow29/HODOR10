#Code by Umut Bilgic, Ankara, Turkey.
#Public release: 11/16/2013
#Release version: 1.1 Beta - Working coin and point system.

from pygame.locals import *
import pygame
import sys
import time
import random
import math

from time import sleep

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((1200,700), 0, 32)
bgImg = pygame.image.load('city_2.png')
direction = 'right'

execfile('sprites.py')
WHITE = (255, 255, 255)

diamondhead=[sprites('Images/Diamondhead/diamondhead_transform_left.png'),          #0
             sprites('Images/Diamondhead/diamondhead_transform_left1.png'),         #1
             sprites('Images/Diamondhead/diamondhead_transform_left2.png'),         #2
             sprites('Images/Diamondhead/diamondhead_move_left1.png'),              #3
             sprites('Images/Diamondhead/diamondhead_move_left2.png'),              #4
             sprites('Images/Diamondhead/diamondhead_move_left3.png'),              #5
             sprites('Images/Diamondhead/diamondhead_move_left4.png'),              #6
             sprites('Images/Diamondhead/diamondhead_attack_left1.png'),            #7
             sprites('Images/Diamondhead/diamondhead_attack_left2.png'),            #8
             sprites('Images/Diamondhead/diamondhead_attack_left3.png'),            #9
             sprites('Images/Diamondhead/diamondhead_attack_left4.png'),            #10
             sprites('Images/Diamondhead/diamondhead_deform_left1.png'),            #11
             sprites('Images/Diamondhead/diamondhead_deform_left2.png'),            #12
             ]

ben = [sprites('Images/sprites/ben_walk_right_FILES/0.png'), 
       sprites('Images/sprites/ben_walk_right_FILES/1.png'),
       sprites('Images/sprites/ben_walk_right_FILES/2.png'),
       sprites('Images/sprites/ben_walk_right_FILES/3.png'),
       sprites('Images/sprites/ben_walk_right_FILES/4.png'),
       sprites('Images/sprites/ben_walk_right_FILES/5.png'),
       sprites('Images/sprites/ben_walk_right_FILES/6.png'),
       sprites('Images/sprites/ben_walk_right_FILES/7.png')]

pygame_img = ben[0].image
bgx = 10
bgy = 10
index1 = 0
index2 = 0
index3 = 0
index4 = 0
index5 = 0
flag=0
while True:
    DISPLAYSURF.fill(WHITE)
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    DISPLAYSURF.blit(bgImg,(bgx,bgy))
    if flag==1:
        pygame_img = diamondhead[2].image
    else:
        pygame_img = pygame.transform.flip(diamondhead[2].image,True,False)
    if keys[pygame.K_RIGHT]:
        bgx-=8
        index1+=1
        pygame_img = pygame.transform.flip(diamondhead[3+index1%4].image,True,False) 
        flag=0
        sleep(.03)
    elif keys[pygame.K_b]:
        pygame_img=ben[0].image

    elif keys[pygame.K_LEFT]:
        bgx+=8
        index2+=1
        pygame_img = diamondhead[3+index2%4].image
        flag=1
        sleep(.03)


    if keys[pygame.K_SPACE]:
        if flag==1:
            index3+=1
            if index3%4==3:
                pygame_img = diamondhead[10].image
                pygame_img1 = diamondhead[2].image
            else:
                pygame_img = diamondhead[7+index3%4].image
            sleep(.03)
        else:
            index4+=1
            if index4%4==3:
                pygame_img = pygame.transform.flip(diamondhead[10].image,True,False)
                pygame_img1 = pygame.transform.flip(diamondhead[2].image,True,False)

            else:
                pygame_img = pygame.transform.flip(diamondhead[7+index4%4].image,True,False)
            sleep(.03)

    if keys[pygame.K_d]:
        if flag == 1:
            pygame_image = diamondhead[index5%3].image
            index5+=1
            sleep(0.03)
        else: 
            pygame_img = pygame.transform.flip(diamondhead[index5%3].image,True,False)
            index5+=1
            sleep(0.03)

    if index3%4==3 or index4%4==3:    
        DISPLAYSURF.blit(pygame_img,(300,500))
        DISPLAYSURF.blit(pygame_img1,(330,500))
    else:
        DISPLAYSURF.blit(pygame_img,(300,500))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
