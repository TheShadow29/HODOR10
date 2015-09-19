import pygame, sys, time
from pygame.locals import *
import random
from time import sleep

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

score = 0
pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((1200,700))
pygame.display.set_caption('Animation')
bgImg = pygame.image.load('background-2.jpg')

global mousex, mousey

def mouseinbox(box):
	if mousex<=box.right and mousex>=box.left and mousey>=box.top and mousey<=box.bottom:
		return True
	return False

fontObj = pygame.font.Font('freesansbold.ttf', 32)

ben_cover = pygame.image.load('ben10background.jpg')
ben_cover = pygame.transform.scale(ben_cover, (1200,700))
DISPLAYSURF = pygame.display.set_mode((1200,700))
pygame.display.set_caption('BEN10')
brown = (165,42,42)
textNewGame = fontObj.render('New Game', True, (0,0,0))
textNewGame = pygame.transform.scale(textNewGame, (252,54))
textNewGameObj = textNewGame.get_rect()
#print textNewGameObj.size
textNewGameObj.topleft = (200, 350)

textPlayAgain = fontObj.render('Play Again', True, (0,0,0))
textPlayAgain = pygame.transform.scale(textPlayAgain, (252,54))
textPlayAgainObj = textPlayAgain.get_rect()
textPlayAgainObj.topleft = (200, 200)

textQuit = fontObj.render('QUIT', True, (0,0,0))
textQuit = pygame.transform.scale(textQuit, (252,54))
textQuitObj = textQuit.get_rect()
textQuitObj.topleft = (200, 350)


textScore = fontObj.render('Score:', True, GREEN)
textScore = pygame.transform.scale(textScore, (50,20))
textScoreObj = textScore.get_rect()
textScoreObj.topright = (790, 10)

textWin = fontObj.render('You Win', True, (0,0,0))
textWin = pygame.transform.scale(textWin, (252,54))
textWinObj = textWin.get_rect()
textWinObj.topleft = (500, 50)

start = False;

size = bgImg.get_rect().size
bgx = 0
bgy = 700-size[1]
bgx_change=0
k=0
timeMax = 90
healthTot = 100
#healthRemaining = 100 - healthTot

execfile('filelist.py')



def background():
	DISPLAYSURF.fill((0,0,0))
#EDIT IF TIME PERMITS
	for i in xrange(0,5):
		DISPLAYSURF.blit(bgImg, (bgx+i*size[0], bgy))
	global time
	time = pygame.time.get_ticks()
	fontObj = pygame.font.Font('freesansbold.ttf', 20)
	timeSurfaceObj = fontObj.render(str(timeMax-(time/1000)), True, GREEN)
	timeRectObj = timeSurfaceObj.get_rect()
	timeRectObj.center = (400, 20)
	health = pygame.Rect(21, 12, healthTot*200/100, 16)

	scoreSurfaceObj = fontObj.render(str(score),True,GREEN)
	scoreRectObj = scoreSurfaceObj.get_rect()
	scoreRectObj.center = (800,20)

	pygame.draw.rect(DISPLAYSURF, GREEN, (20, 10, 204, 20), 1)
	pygame.draw.rect(DISPLAYSURF, GREEN, health)
	DISPLAYSURF.blit(timeSurfaceObj, timeRectObj)
	DISPLAYSURF.blit(scoreSurfaceObj,scoreRectObj)
	DISPLAYSURF.blit(textScore, textScoreObj)
	pygame.display.update()

ben = [pygame.image.load('Images/sprites/ben_walk_right_FILES/0.png'), 
       pygame.image.load('Images/sprites/ben_walk_right_FILES/1.png'),
       pygame.image.load('Images/sprites/ben_walk_right_FILES/2.png'),
       pygame.image.load('Images/sprites/ben_walk_right_FILES/3.png'),
       pygame.image.load('Images/sprites/ben_walk_right_FILES/4.png')]
ben_left = [pygame.transform.flip(b, True, False) for b in ben]
ben_move = ben[1:]
ben_left_move = ben_left[1:]

hbf = ['./Images/HeatBlast/'+i for i in hblist]
hbs = [pygame.image.load(i) for i in hbf]
hbs_t = hbs[:4]
hbs_right_motion=hbs[6:12]
hbs_left_motion =[pygame.transform.flip(h,True,False) for h in hbs_right_motion]
hbs_attack_right = hbs[13:]
hbs_attack_left =[pygame.transform.flip(h,True,False) for h in hbs_attack_right]

wmf = ['./Images/Wildmutt/'+i for i in wmlist]
wms = [pygame.image.load(i) for i in wmf]
wms_to_t = wms[:3]
wms_back_t=wms[9:11]
wms_right_motion=wms[5:9]
wms_left_motion=[pygame.transform.flip(w,True,False) for w in wms_right_motion]
wms_right_roll=wms[3:6]
wms_left_roll=[pygame.transform.flip(w,True,False) for h in wms_right_roll]

gfs = [[0 for x in range(12)] for x in range(12)] 
gfs_attack = [[0 for x in range(6)] for x in range(6)] 
gff = ['./Images/Ghostfreak/'+i for i in gflist]
gfs[0] = [pygame.image.load(i) for i in gff]
gfs[1] = [pygame.transform.flip(g,True,False) for g in gfs[0]]
gfs_attack[0] = gfs[0][6:12]
gfs_attack[1] = gfs[1][6:12]
gfImgspritetrans = [pygame.image.load('./Images/Ghostfreak/02GhostfreakNormalrighttrans.png'), 
					pygame.transform.flip(pygame.image.load('./Images/Ghostfreak/02GhostfreakNormalrighttrans.png'), True, False)] 

diamondhead=[pygame.image.load('Images/Diamondhead/diamondhead_transform_left.png'),          #0
             pygame.image.load('Images/Diamondhead/diamondhead_transform_left1.png'),         #1
             pygame.image.load('Images/Diamondhead/diamondhead_transform_left2.png'),         #2
             pygame.image.load('Images/Diamondhead/diamondhead_move_left1.png'),              #3
             pygame.image.load('Images/Diamondhead/diamondhead_move_left2.png'),              #4
             pygame.image.load('Images/Diamondhead/diamondhead_move_left3.png'),              #5
             pygame.image.load('Images/Diamondhead/diamondhead_move_left4.png'),              #6
             pygame.image.load('Images/Diamondhead/diamondhead_attack_left1.png'),            #7
             pygame.image.load('Images/Diamondhead/diamondhead_attack_left2.png'),            #8
             pygame.image.load('Images/Diamondhead/diamondhead_attack_left3.png'),            #9
             pygame.image.load('Images/Diamondhead/diamondhead_attack_left4.png'),            #10
             pygame.image.load('Images/Diamondhead/diamondhead_deform_left1.png'),            #11
             pygame.image.load('Images/Diamondhead/diamondhead_deform_left2.png')]			  #12

dmra = [pygame.transform.flip(diamondhead[7+dh%3],True,False) for dh in xrange(0,3)]



drf = ['./Images/Drones/'+i for i in drlist] 

drs = [pygame.image.load(i) for i in drf]
dr_right = drs[:2]
dr_left = drs[2:]
drx = [i for i in xrange(1,5)]
dry = 0
dr_go=True


alienchange=''
curr_alien=''

pygame_img = ben[1]

index1=0
index3=0	#for diamondhead

transform={'h':0, 'w':0, 'g':0, 'b':0, 'd':0}

direction='right'

hbs_count_attack_right = 0
hb_count_move_left = 0
hbs_count_attack_left=0

move_count = 0

wm_count_move_left =0
wm_count_roll=0
wm_count_roll_left=0

curr_alien = 'b'

gftrans = 0

start = False
lose = False
win = False
soundObj = pygame.mixer.Sound('ben10.wav')
soundObj.play()

while True:

	while start == False and lose == False and win == False:
		DISPLAYSURF.fill(brown)
		DISPLAYSURF.blit(ben_cover,(0,0))
		DISPLAYSURF.blit(textNewGame, textNewGameObj)
		for event in pygame.event.get():
			if event.type == QUIT:
				soundObj.stop()
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = pygame.mouse.get_pos()
			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				mousex, mousey = pygame.mouse.get_pos()
				if mousex > 200 and mousex < 452 and mousey > 350 and mousey < 404:
					start = True;
		pygame.display.update()
	
	while start == True and lose == False and win == False:
		background()
		pygame.event.pump()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					bgx_change = 0
				if curr_alien == 'h':
					if direction =='right':
						pygame_img=hbs[3] 
					elif direction == 'left':
						pygame_img = pygame.transform.flip(hbs[3],True,False)
				elif curr_alien == 'b':
					if direction =='right':
						pygame_img=ben[1] 
					elif direction == 'left':
						pygame_img = ben_left[1]
				elif curr_alien=='w':
					if direction =='right':
						pygame_img=wms[2] 
					elif direction == 'left':
						pygame_img = pygame.transform.flip(wms[2],True,False)
				elif curr_alien=='d':
					if direction =='right':
						pygame_img = pygame.transform.flip(diamondhead[2],True,False) 
					elif direction == 'left':
						pygame_img = diamondhead[2]
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					if bgx == -(3715 + k*3715):
						k+=1
					else :
						bgx_change = -5
					direction='right'
					#for i in drx:
					#	i-=5				
				elif event.key == pygame.K_LEFT:
					if bgx >= 0:
						pass
					else: 
						bgx_change = 5
					direction='left'
					#for i in drx:
					#	i=5
	#Alienchanges			
				elif event.key == pygame.K_h:
					alienchange = 'h'
				elif event.key == pygame.K_w:
					alienchange = 'w'
				elif event.key == pygame.K_b:
					alienchange = 'b'
				elif event.key == pygame.K_g:
					alienchange = 'g'
				elif event.key == pygame.K_x and curr_alien == 'g':
					gftrans = 1 - gftrans
				elif event.key == pygame.K_d:
					alienchange = 'd'
					
	###############
	#Attack
				elif event.key == pygame.K_SPACE:
					if curr_alien=='h' and direction=='right':
						for hbs_count_attack_right in xrange(0,5):
							pygame_img = hbs_attack_right[int(hbs_count_attack_right)]
							background()
							DISPLAYSURF.blit(pygame_img,(330,500))
							pygame.display.update()

					if curr_alien=='d' and direction=='right':
						index3+=1
						for dh in xrange(0,3):
							pygame_img = dmra[dh]
							background()
							DISPLAYSURF.blit(pygame_img,(330,500))
							sleep(0.01)
							pygame.display.update()
	        			#sleep(.1)
	        		if curr_alien=='w' and direction=='right':
						for i in xrange(0,3):
							for wms_count_roll_right in xrange(0,2):
								pygame_img = wms_right_roll[wms_count_roll_right]
								bgx-=5
								bgx-=5
								background()	
								DISPLAYSURF.blit(pygame_img,(330,500))
								pygame.display.update()
							pygame_img = wms_right_roll[i]
							bgx-=5
							bgx-=5
							background()	
							DISPLAYSURF.blit(pygame_img,(330,500))
							pygame.display.update()



	######################
	#movement + Wildmutt attack
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			if curr_alien == 'h':
				pygame_img=hbs_right_motion[int(move_count)%6] 
				move_count+=0.5
			elif curr_alien == 'b':
				pygame_img = ben_move[int(move_count)%4]
				move_count+=0.5
			elif curr_alien=='w':
				pygame_img=wms_right_motion[int(move_count)%4]				
				move_count+=0.5
			elif curr_alien == 'd':
				pygame_img = pygame.transform.flip(diamondhead[3 + int(move_count)%4],True,False)
				move_count+=0.5
			
		elif keys[pygame.K_LEFT]:
			if curr_alien=='h':
				pygame_img=hbs_left_motion[int(move_count)%6]
				move_count+=0.5
			elif curr_alien == 'b':
				pygame_img = ben_left_move[int(move_count)%4]
				move_count+=0.5
			elif curr_alien=='w':
				pygame_img=wms_left_motion[int(move_count)%4]				
				move_count+=0.5
			elif curr_alien == 'd':
				pygame_img = diamondhead[3 + int(move_count)%4]
				move_count+=0.5
				
	##########
	#ghostfreak sprites
		if curr_alien == 'g':
			if direction == 'right':
				if gftrans == 0:
					pygame_img = gfs[0][1]
				elif gftrans == 1:
					pygame_img = gfImgspritetrans[0]
			elif direction == 'left':
				if gftrans == 0:
					pygame_img = gfs[1][1]
				elif gftrans == 1:
					pygame_img = gfImgspritetrans[1]

	###########

	#Alienchange sprites		
		if alienchange == 'h':
			curr_alien = 'h'
			pygame_img = hbs[transform[alienchange]]
			transform[alienchange]+=1
			if transform[alienchange]>3:
				transform[alienchange]=0
				alienchange=''

		if alienchange == 'w':
			curr_alien = 'w'
			pygame_img = wms[transform[alienchange]]
			transform[alienchange]+=1
			if transform[alienchange]>2:
				transform[alienchange]=0
				alienchange=''

		if alienchange == 'g':
			curr_alien = 'g'
			pygame_img = gfs[0][transform[alienchange]]
			transform[alienchange]+=1
			if transform[alienchange]>1:
				transform[alienchange]=0
				alienchange=''

		if alienchange == 'b':
			curr_alien = 'b'
			pygame_img = ben[transform[alienchange]]
			transform[alienchange]+=1
			if transform[alienchange] > 1:
				transform[alienchange]=0
				alienchange=''

		if alienchange == 'd':
			curr_alien = 'd'
			pygame_img = pygame.transform.flip(diamondhead[transform[alienchange]],True,False)
			transform[alienchange]+=1
			if transform[alienchange] > 2:
				transform[alienchange]=0
				alienchange=''



	#########

		bgx += bgx_change
	#DRONES#####
	############
		for i in xrange(0,4):
			if dr_go == True:
				for j in range(0,1):
					DISPLAYSURF.blit(dr_right[0],(1200-drx[i],500+dry))
					#dr_right[0].get_rect().right=1200-drx[i]
					#dr_right[0].get_rect().bottom=500+dry
					DISPLAYSURF.blit(dr_right[1],(1200-drx[i]-100,500+dry))	
					#dr_right[1].get_rect().right=1200-drx[i]-100
					#dr_right[1].get_rect().bottom=500+dry		
					if drx[i]>=670 and abs(dry)>=0.5:
						if curr_alien=='h':
							#if pygame_img != hbs[3]:
							if pygame_img == hbs_attack_right[0] or pygame_img == hbs_attack_right[1] or pygame_img==hbs_attack_right[2] or pygame_img==hbs_attack_right[3] or pygame_img==hbs_attack_right[4]:
								#if 
								#print 'good'
								score+=5
								drx[i]=0
								dry=0
							else:
								healthTot-=0.5
					if drx[i]>=690 and abs(dry)>=0.5:
						if curr_alien=='w':
							if pygame_img==wms_right_roll[0] or pygame_img==wms_right_roll[1]:
								#print 'good'
								score+=5
								drx[i]=0
								dry=0
							else:
								healthTot-=0.5	

					if drx[i]>=690 and abs(dry)>=0.5:
						if curr_alien=='g':
							if gftrans==0:
								healthTot-=0.5
						if curr_alien=='b':
							healthTot-=0.5

					if drx[i]>=670 and abs(dry)>=0.5:
						if curr_alien=='d':
							#if pygame_img != hbs[3]:
							if pygame_img == dmra[0] or pygame_img == dmra[1] or pygame_img==dmra[2]:
								score+=5
								drx[i]=0
								dry=0
							else:
								healthTot-=0.5

					if keys[pygame.K_RIGHT]:
						drx[i]+=i+5
					elif keys[pygame.K_LEFT]:
						drx[i]+=i-5
					elif keys[pygame.K_SPACE] and curr_alien=='w':
						drx[i]+=i+10
					else:
						drx[i]+=i
						
					
					dry += (2*random.random()-1)
					if drx[i]>1100:
						drx[i] = 0

					

		if dry>100 or dry<-100:
			dry=0


		DISPLAYSURF.blit(pygame_img,(330,500))
		if healthTot < 0 or time > timeMax*1000:
			lose = True
			break

		pygame.display.update()
		fpsClock.tick(FPS)



	textLose = fontObj.render('Game Over! Your Score is: '+ str(score), True, (0,0,0))
	textLose = pygame.transform.scale(textLose, (252,54))
	textLoseObj = textLose.get_rect()
	textLoseObj.topleft = (500, 50)

	while lose == True:
		DISPLAYSURF.fill(brown)
		DISPLAYSURF.blit(ben_cover,(0,0))
		DISPLAYSURF.blit(textPlayAgain, textPlayAgainObj)
		DISPLAYSURF.blit(textLose, textLoseObj)
		DISPLAYSURF.blit(textQuit, textQuitObj)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT:
				soundObj.stop()
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				mousex, mousey = pygame.mouse.get_pos()
				if mousex > 200 and mousex < 452 and mousey >200  and mousey < 300:
					direction='right'
					hbs_count_attack_right = 0
					hb_count_move_left = 0
					hbs_count_attack_left=0
					move_count = 0
					wm_count_move_left =0
					wm_count_roll=0
					wm_count_roll_left=0
					alienchange = 'b'
					gftrans = 0
					start = False
					lose = False
					win = False
					healthTot = 100
					drx = [i for i in xrange(1,5)]
					bgx = 0
					bgy = 700 - size[1]
				elif mousex > 200 and mousex < 452 and mousey >350  and mousey < 404:
					soundObj.stop()
					pygame.quit()
					sys.exit()

	while win == True:
		DISPLAYSURF.fill(brown)
		DISPLAYSURF.blit(ben_cover,(0,0))
		DISPLAYSURF.blit(textPlayAgain, textPlayAgainObj)
		DISPLAYSURF.blit(textWin, textWinObj)
		DISPLAYSURF.blit(textQuit, textQuitObj)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT:
				soundObj.stop()
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				mousex, mousey = pygame.mouse.get_pos()
				if mousex > 200 and mousex < 452 and mousey >200  and mousey < 300:
					
					hbs_count_attack_right = 0
					hb_count_move_left = 0
					hbs_count_attack_left=0

					move_count = 0

					wm_count_move_left =0
					wm_count_roll=0
					wm_count_roll_left=0

					alienchange = 'b'
					gftrans = 0
					start = False
					lose = False
					win = False
					healthTot = 100
					drx = [i for i in xrange(1,5)]
					bgx = 0
					bgy = 700 - size[1]
				elif mousex > 200 and mousex < 452 and mousey >350  and mousey < 404:
					soundObj.stop()
					pygame.quit()
					sys.exit()

		pygame.display.update()