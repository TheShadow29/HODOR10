from pygame.locals import *
import pygame
import sys
import time
import random
import math
import random 

from time import sleep


pygame.init()
FPS = 20 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((1200,700), 0, 32)

BLUE=(0,0,255)

execfile('sprites.py')

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


boss_img = []


for i in range(0,15):
	boss_img.append(pygame.transform.scale(boss[i].image,(500,500)))
for i in range(16,20):
	boss_img.append(pygame.transform.scale(pygame.transform.flip(boss[i].image,True,False),(500,500)))


def whip_left():
		for i in range(1,11):
			DISPLAYSURF.fill(BLUE)
			DISPLAYSURF.blit(boss_img[i],(500,150))
			pygame.display.update()
			fpsClock.tick(FPS)
    		sleep(0.5)
    		
def wrecking_ball():
		for i in range(11,15):
			DISPLAYSURF.fill(BLUE)
			DISPLAYSURF.blit(boss_img[i],(500,150))
			pygame.display.update()
			fpsClock.tick(FPS)
    		sleep(0.5)

def dragon():
		for i in range(15,19):
			DISPLAYSURF.fill(BLUE)
			DISPLAYSURF.blit(boss_img[i],(500,150))
			pygame.display.update()
			fpsClock.tick(FPS)
    		sleep(0.5)

bgx = 10
bgy = 10
index1 = 0 # right steps taken
index2 = 0 # left steps taken
index3 = 0 #left attack
index4 = 0 #right attack
index5 = 0 #alienchange
flag=0  #Right or Left

while True:
	attack=int(random.random()*3)
	if attack==0:
		wrecking_ball()
		sleep(1)
	elif attack==1:
		whip_left()
		sleep(1)
	elif attack==2:
		dragon()
		sleep(1)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()