import pygame,sys
from pygame.locals import *

pygame.init()

cityimg = pygame.image.load('city_2.png')
ben_cover = pygame.image.load('ben10.jpg')
ben_cover_rect = ben_cover.get_rect()
DISPLAYSURF = pygame.display.set_mode((1000,1000),0,32)
pygame.display.set_caption('BEN10')
brown = (165,42,42)
while True:
	DISPLAYSURF.fill(brown,)
	DISPLAYSURF.blit(cityimg,(0,0))
	DISPLAYSURF.blit(ben_cover,(250,250))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()