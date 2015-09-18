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
             sprites('Images/Diamondhead/diamondhead_deform_left1.png'),            #10
             sprites('Images/Diamondhead/diamondhead_deform_left2.png'),            #11
             ]

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


ben = [sprites('Images/sprites/ben_walk_right_FILES/0.png'), 
       sprites('Images/sprites/ben_walk_right_FILES/1.png'),
       sprites('Images/sprites/ben_walk_right_FILES/2.png'),
       sprites('Images/sprites/ben_walk_right_FILES/3.png'),
       sprites('Images/sprites/ben_walk_right_FILES/4.png'),
       sprites('Images/sprites/ben_walk_right_FILES/5.png'),
       sprites('Images/sprites/ben_walk_right_FILES/6.png'),
       sprites('Images/sprites/ben_walk_right_FILES/7.png')]



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
			DISPLAYSURF.blit(boss_img[i],(330,150))
			pygame.display.update()
			fpsClock.tick(FPS)
    		sleep(0.5)

def dragon():
		for i in range(15,19):
			DISPLAYSURF.fill(BLUE)
			DISPLAYSURF.blit(boss_img[i],(330,150))
			pygame.display.update()
			fpsClock.tick(FPS)
    		sleep(0.5)

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

	DISPLAYSURF.fill(BLUE)
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
		sleep(.06)
	elif keys[pygame.K_b]:
		pygame_img=ben[0].image

	elif keys[pygame.K_LEFT]:
		bgx+=8
		index2+=1
		pygame_img = diamondhead[3+index2%4].image
		flag=1
		sleep(.06)


	if keys[pygame.K_SPACE]:
		index3+=1
		pygame_img = pygame.transform.flip(diamondhead[7+index3%3].image,True,False)
		sleep(.1)

	if keys[pygame.K_d]:
		if flag == 1:
			pygame_image = diamondhead[index5%3].image
			index5+=1
			sleep(0.3)
		else: 
			pygame_img = pygame.transform.flip(diamondhead[index5%3].image,True,False)
			index5+=1
			sleep(0.3)
   
	DISPLAYSURF.blit(pygame_img,(300,500))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()