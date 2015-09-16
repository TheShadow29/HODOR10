import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((1200,700), 0, 32)
pygame.display.set_caption('Animation')
WHITE = (255, 255, 255)
bgImg = pygame.image.load('city_2.png')
print bgImg.get_rect().size
size = bgImg.get_rect().size
bgx = 0
bgy = 0
while True:
	DISPLAYSURF.fill(WHITE)
	pygame.event.pump()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		bgx-=5
	elif keys[pygame.K_LEFT]:
		bgx+=5
	DISPLAYSURF.blit(bgImg, (bgx, bgy))
	DISPLAYSURF.blit(bgImg, (bgx+size[0], bgy))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)