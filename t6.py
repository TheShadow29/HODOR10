import pygame, sys, time
from pygame.locals import *
from time import sleep

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((1200,700), 0, 32)
bgImg = pygame.image.load('city_2.png')
direction = 'right'
size = bgImg.get_rect().size
bgx = 0
bgy = 10
timeMax = 30
healthTot = 60
healthRemaining = 100 - healthTot
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

time = pygame.time.get_ticks()
fontObj = pygame.font.Font('freesansbold.ttf', 20)
timeSurfaceObj = fontObj.render(str(time), True, GREEN)
timeRectObj = timeSurfaceObj.get_rect()
timeRectObj.center = (400, 20)

health = pygame.Rect(21, 12, healthTot*200/100, 16)

execfile('filelist.py')
execfile('sprites.py')

hbf = ['./Images/HeatBlast/'+i for i in hblist]

hbs = [sprites(i) for i in hbf]
hbs_t = hbs[:4]
hbs_right_motion=hbs[6:12]
hbs_left_motion =[pygame.transform.flip(h.image,True,False) for h in hbs_right_motion]
hbs_attack_right = hbs[13:]
hbs_attack_left =[pygame.transform.flip(h.image,True,False) for h in hbs_attack_right]
hbs_attack_right.append(hbs[3])
hbs_attack_left.append(pygame.transform.flip(hbs[3].image,True,False))

wmf = ['./Images/Wildmutt/'+i for i in wmlist]
wms = [sprites(i) for i in wmf]
wms_to_t = wms[:3]
wms_back_t=wms[9:11]
wms_right_motion=wms[5:9]
wms_left_motion=[pygame.transform.flip(w.image,True,False) for w in wms_right_motion]
wms_right_roll=wms[3:6]
wms_left_roll=[pygame.transform.flip(w.image,True,False) for h in wms_right_roll]


alienchange=''
curr_alien=''

ben = [sprites('Images/sprites/ben_walk_right_FILES/0.png'), 
       sprites('Images/sprites/ben_walk_right_FILES/1.png'),
       sprites('Images/sprites/ben_walk_right_FILES/2.png'),
       sprites('Images/sprites/ben_walk_right_FILES/3.png'),
       sprites('Images/sprites/ben_walk_right_FILES/4.png'),
       sprites('Images/sprites/ben_walk_right_FILES/5.png'),
       sprites('Images/sprites/ben_walk_right_FILES/6.png'),
       sprites('Images/sprites/ben_walk_right_FILES/7.png')]
transform={'h':0, 'w':0}
pygame_img = ben[0].image
y=pygame_img.get_rect().bottom
hb_count_move_right = 0
hbs_count_attack_right = 0
hb_count_move_left = 0
hbs_count_attack_left=0
direction='right'

wm_count_move_right = 0
wm_count_move_left =0
wm_count_roll=0
wm_count_roll_left=0

def background():
	time = pygame.time.get_ticks()
	DISPLAYSURF.fill(WHITE)
	timeSurfaceObj = fontObj.render(str(timeMax - (time/1000)), True, GREEN)
	timeRectObj.center = (400, 20)
	DISPLAYSURF.blit(bgImg, (bgx, bgy))
	DISPLAYSURF.blit(bgImg, (bgx+size[0], bgy))
	pygame.draw.rect(DISPLAYSURF, GREEN, (20, 10, 204, 20), 1)
	pygame.draw.rect(DISPLAYSURF, GREEN, health)




while True:
	
	time = pygame.time.get_ticks()
	timeSurfaceObj = fontObj.render(str(timeMax - (time/1000)), True, GREEN)
	timeRectObj.center = (400, 20)
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(bgImg, (bgx, bgy))
	DISPLAYSURF.blit(bgImg, (bgx+size[0], bgy))
	pygame.event.pump()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		bgx-=5
		direction='right'
		if curr_alien=='h':
			pygame_img=hbs_right_motion[hb_count_move_right%6].image
			hb_count_move_right+=1
		elif curr_alien=='w':
			pygame_img=wms_right_motion[wm_count_move_right%4].image				
			wm_count_move_right+=1
	elif keys[pygame.K_LEFT]:
		bgx+=5
		direction='left'
		if curr_alien=='h':
			pygame_img=hbs_left_motion[hb_count_move_left%6]
			hb_count_move_left+=1
		elif curr_alien=='w':
			pygame_img=wms_left_motion[wm_count_move_left%4]
			wm_count_move_left+=1

	elif keys[pygame.K_h]:
		alienchange='h'
	elif keys[pygame.K_w]:
		alienchange='w'

	elif keys[pygame.K_SPACE]:
		if curr_alien=='h' and direction=='right':
			for hbs_count_attack_right in xrange(0,6):
				pygame_img = hbs_attack_right[int(hbs_count_attack_right)].image
				DISPLAYSURF.fill(WHITE)
				DISPLAYSURF.blit(bgImg, (bgx, bgy))		
				DISPLAYSURF.blit(pygame_img,(330,500))
				DISPLAYSURF.blit(bgImg, (bgx+size[0], bgy))
				pygame.display.update()
			
		elif curr_alien=='h' and direction=='left':
			for hbs_count_attack_left in xrange(0,6):
				pygame_img = hbs_attack_left[hbs_count_attack_left]
				DISPLAYSURF.fill(WHITE)
				DISPLAYSURF.blit(bgImg, (bgx, bgy))	
				DISPLAYSURF.blit(pygame_img,(330,500))

		elif curr_alien=='w' and direction=='right':
			for wms_count_roll_right in xrange(0,3):
				pygame_img = wms_right_roll[wms_count_roll_right].image
				bgx-=5
				bgx-=5
				background()	
				DISPLAYSURF.blit(pygame_img,(330,500))
				pygame.display.update()

		elif curr_alien=='w' and direction=='left':
			for wms_count_roll_left in xrange(0,3):
				pygame_img = wms_left_roll[wms_count_roll_left]
				bgx+=5
				bgx+=5
				background()	
				DISPLAYSURF.blit(pygame_img,(330,500))
				pygame.display.update()


	if alienchange == 'h':
		curr_alien = 'h'
		pygame_img = hbs[transform[alienchange]].image
		pygame_img.get_rect().bottom = y
		transform[alienchange]+=1
		if transform[alienchange]>3:
			transform[alienchange]=0
			alienchange=''

	if alienchange == 'w':
		curr_alien = 'w'
		pygame_img = wms[transform[alienchange]].image
		transform[alienchange]+=1
		if transform[alienchange]>2:
			transform[alienchange]=0
			alienchange=''




	pygame.draw.rect(DISPLAYSURF, GREEN, (20, 10, 204, 20), 1)
	pygame.draw.rect(DISPLAYSURF, GREEN, health)

	DISPLAYSURF.blit(timeSurfaceObj, timeRectObj)
	DISPLAYSURF.blit(pygame_img,(330,500))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				bgx_change = 0
			if curr_alien=='w' and direction=='right':
				pygame_img=wms_right_motion[0].image
			if curr_alien=='w' and direction=='left':
				pygame_img=wms_left_motion[0]


	pygame.display.update()
	fpsClock.tick(FPS)