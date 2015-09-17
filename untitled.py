import pygame, sys, time
from pygame.locals import *

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((800,400))
pygame.display.set_caption('Animation')
bgImg = pygame.image.load('city_2.png')
print bgImg.get_rect().size
size = bgImg.get_rect().size
bgx = 0
bgy = 400-size[1]
timeMax = 30
healthTot = 60
healthRemaining = 100 - healthTot
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
gfImgsprite = [pygame.image.load('Images/Ghostfreak/GhostfreakNormalright.png'), 
			   pygame.image.load('Images/Ghostfreak/GhostfreakNormalleft.png')] 
gfImgspritetrans = [pygame.image.load('Images/Ghostfreak/GhostfreakNormalrighttrans.png'), 
					pygame.image.load('Images/Ghostfreak/GhostfreakNormallefttrans.png')] 

time = pygame.time.get_ticks()
fontObj = pygame.font.Font('freesansbold.ttf', 20)
timeSurfaceObj = fontObj.render(str(time), True, GREEN)
timeRectObj = timeSurfaceObj.get_rect()
timeRectObj.center = (400, 20)

health = pygame.Rect(21, 12, healthTot*200/100, 16)
k = 0

direc = 0
trans = 0
key = ""
bgx_change = 0

while True:
	
	time = pygame.time.get_ticks()
	timeSurfaceObj = fontObj.render(str(timeMax - (time/1000)), True, GREEN)
	timeRectObj.center = (400, 20)

	DISPLAYSURF.fill(WHITE)

	DISPLAYSURF.blit(bgImg, (bgx+(k-1)*size[0], bgy))
	DISPLAYSURF.blit(bgImg, (bgx+k*size[0], bgy))
	pygame.event.pump()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()			
		if event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_LEFT:
		        bgx_change = 5
		    elif event.key == pygame.K_RIGHT:
		        bgx_change = -5
		    elif event.key == pygame.K_x:
		    	print "X"
		if event.type == pygame.KEYUP:
		    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		        bgx_change = 0

	bgx += bgx_change




	if trans == 0 :
		DISPLAYSURF.blit(gfImgsprite[direc],(800/3, 300))
	elif trans == 1 :
		DISPLAYSURF.blit(gfImgspritetrans[direc],(800/3, 300))
	
	pygame.draw.rect(DISPLAYSURF, GREEN, (20, 10, 204, 20), 1)
	pygame.draw.rect(DISPLAYSURF, GREEN, health)

	DISPLAYSURF.blit(timeSurfaceObj, timeRectObj)

	pygame.display.update()
	fpsClock.tick(FPS)