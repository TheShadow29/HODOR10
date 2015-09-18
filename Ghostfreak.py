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

execfile('filelist.py')
execfile('sprites.py')

gfs = [[0 for x in range(12)] for x in range(12)] 
gfs_attack = [[0 for x in range(6)] for x in range(6)] 

gff = ['./Images/Ghostfreak/'+i for i in gflist]
gfs[0] = [pygame.image.load(i) for i in gff]
gfs[1] = [pygame.transform.flip(g,True,False) for g in gfs[0]]
gfs_attack[0] = gfs[0][6:12]
gfs_attack[1] = gfs[1][6:12]

gfImgspritetrans = [pygame.image.load('./Images/Ghostfreak/02GhostfreakNormalrighttrans.png'), 
					pygame.transform.flip(pygame.image.load('./Images/Ghostfreak/02GhostfreakNormalrighttrans.png'), True, False)] 

time = pygame.time.get_ticks()
fontObj = pygame.font.Font('freesansbold.ttf', 20)
timeSurfaceObj = fontObj.render(str(time), True, GREEN)
timeRectObj = timeSurfaceObj.get_rect()
timeRectObj.center = (400, 20)

health = pygame.Rect(21, 12, healthTot*200/100, 16)
k = 0

direc = 0
trans = 0
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
		elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_RIGHT:
				if bgx == -(2135 + k*2135):
					k+=1
				else :
					bgx_change = -5
				direc = 0	
		    elif event.key == pygame.K_LEFT:
				if bgx >= 0:
					pass
				else: 
					bgx_change = 5
				direc = 1 
		    elif event.key == pygame.K_x:
				print "X"
				if trans == 0 :
					trans = 1
				elif trans == 1 :
					trans = 0
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				bgx_change = 0
#<<<<<<< HEAD:Ghostfreakwalk.py
			
#=======
		elif event.type == pygame.K_SPACE:
			for gfs_attack in xrange(0,6):
				pygame_img = gfs_attack[0][gfs_attack]
				DISPLAYSURF.fill(WHITE)
				bgx-=5
				DISPLAYSURF.blit(bgImg, (bgx, bgy))	
				DISPLAYSURF.blit(gfs,(330,500))
				DISPLAYSURF.blit(pygame_img,(330 + i*10,500))
				pygame.display.update()

#>>>>>>> f2fa2ffd1df197b58c64018cf2ba44e551df1cb8:Ghostfreak.py
	bgx += bgx_change


	if trans == 0 :
		DISPLAYSURF.blit(gfs[direc][0],(800/3, 300))
	elif trans == 1 :
		DISPLAYSURF.blit(gfImgspritetrans[direc],(800/3, 300))
	
	pygame.draw.rect(DISPLAYSURF, GREEN, (20, 10, 204, 20), 1)
	pygame.draw.rect(DISPLAYSURF, GREEN, health)

	DISPLAYSURF.blit(timeSurfaceObj, timeRectObj)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)