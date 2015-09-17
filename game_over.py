import pygame, sys
from pygame.locals import *
pygame.init()
red = (255,0,0)

x=750
y=600
display_height=x
display_width=y
DISPLAYSURF = pygame.display.set_mode((x, y))
overImg= pygame.image.load('ben10background.png')
x,y=makeText("Game Over", red,20,30)
DISPLAYSURF.blit(overImg, (0, 0))
pygame.display.set_caption('Game Over!')
while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			
			pygame.quit()	
			sys.exit()
	pygame.display.update()




