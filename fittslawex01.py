import pygame as pg

pg.init()



width, height = (1366, 768)

step_start = int(width/6)
step = step_start
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
color_right_circle = white
color_left_circle = white
loops = 0
SetR = [10,30,50,70,100]

R = SetR[4]
screen = pg.display.set_mode((width, height), pg.FULLSCREEN)

x_center, y_center = (int(width/2), int(height/2))

while True:
	clock = pg.time.Clock(); 
	clock.tick(120) 
	screen.fill((0,0,0))
	pg.mouse.set_visible(False)

	for event in pg.event.get():

		if event.type == pg.MOUSEMOTION:

			pos = pg.mouse.get_pos()
			x = pos[0]
			y = pos[1]
			



	

	
			pg.draw.circle(screen, color_left_circle, (int(width/6), int(height/2)), 20, 1)
			pg.draw.circle(screen, color_right_circle, (int(width*5/6), int(height/2)), R, 2)
			pg.draw.circle(screen, (255,255,255), (x,y), 5, 0)
			if (x - int(width*5/6))**2 + (y - int(height/2))**2 <= R**2:
				color_right_circle = red
			else:
				color_right_circle = white

			if (x - int(width/6))**2 + (y - int(height/2))**2 <= 20**2:
				color_left_circle = white
			else:
				color_left_circle = green
	
			if x > 1366:
				exit()

			pg.display.update()
		
	# 	if event.type == pg.MOUSEMOTION:
	# 		
    # print(pg.event.poll())
    # print(pg.event.pump())
    
	# event = pg.event.wait()

	# event = pg.event.wait()
	# e = str(event)
	# print(e)
	# step  += 20
	# # if 3 > 1: 

	# # 	pos = pg.mouse.get_pos()
	# # 	print(pos)
	# if step >= width - step_start:
	# 	step = step_start
	# 	loops += 1
	# 	if loops == 3:
	# 		exit()
	