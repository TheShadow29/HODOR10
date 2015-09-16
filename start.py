import pygame,sys
from pygame.locals import *

pygame.init()

global mousex, mousey

def mouseinbox(box):
	if mousex<=box.right and mousex>=box.left and mousey>=box.top and mousey<=box.bottom:
		return True
	return False

cityimg = pygame.image.load('city_2.png')
ben_cover = pygame.image.load('ben10.jpg')
ben_rect = ben_cover.get_rect()
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
		elif event.type == MOUSEMOTION:
			mousex, mousey = pygame.mouse.get_pos()
		elif event.type == MOUSEBUTTONDOWN and event.button == 1:
			mousex, mousey = pygame.mouse.get_pos()
			if mouseinbox(pygame.Rect(10, 20, 200, 300))==False:
				print mousex,mousey
				print ben_rect.get_
				print True
			else:
				print False


	pygame.display.update()