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

execfile('sprites.py')
WHITE = (0, 255, 255)

boss = [sprites('Images/Boss/18.png'),
		sprites('Images/Boss/0.png'),
		sprites('Images/Boss/1.png'),
		sprites('Images/Boss/2.png'),
		sprites('Images/Boss/3.png'),
		sprites('Images/Boss/4.png'),
		sprites('Images/Boss/5.png'),
		sprites('Images/Boss/6.png'),
		sprites('Images/Boss/7.png'),
		sprites('Images/Boss/8.png'),
		sprites('Images/Boss/9.png'),
		sprites('Images/Boss/24.png'),
		sprites('Images/Boss/25.png'),
		sprites('Images/Boss/26.png'),
		sprites('Images/Boss/27.png'),
		sprites('Images/Boss/19.png'),
		sprites('Images/Boss/20.png'),
		sprites('Images/Boss/21.png'),
		sprites('Images/Boss/22.png'),
		sprites('Images/Boss/23.png')
		]

def whip_left():
		for i in range(0,10):
			DISPLAYSURF.fill(WHITE)
			DISPLAYSURF.blit(boss[1+i%10].image,(330,500))
			pygame.display.update()
    		fpsClock.tick(FPS)
    		sleep(1)

while True:
	whip_left()