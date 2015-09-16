import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 #frames per second setting
fpsClock =pygame.time.Clock()

#setup the window
DISPLAYSURF = pygame.display.set_mode((1000,1000),0,32)
pygame.display.set_caption('Animation')

brown = (165,42,42)
cityimg = pygame.image.load('city_2.png')
citx=5
direction = 'right'
while True:
	citx -=5
	DISPLAYSURF.fill(brown)
	DISPLAYSURF.blit(cityimg,(citx,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(FPS)
	if citx == -1900:
		citx=5
	if event.type == KEYUP:
		break
for event in pygame.event.get():
	if event.type == QUIT:
		pygame.quit()
		sys.exit()
print citx