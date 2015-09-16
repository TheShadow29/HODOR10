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
bgx = 10
bgy = 10
direction = 'right'
while True: # the main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			DISPLAYSURF.fill(WHITE)
			if event.key == K_LEFT:
				bgx += 50
			elif event.key == K_UP:
				bgy += 50
			elif event.key == K_RIGHT:
				bgx -= 50
			elif event.key == K_DOWN:
				bgy -= 50
		DISPLAYSURF.blit(bgImg, (bgx, bgy))
		DISPLAYSURF.blit(bgImg, (bgx+size[0], bgy))
	pygame.display.update()
	fpsClock.tick(FPS)