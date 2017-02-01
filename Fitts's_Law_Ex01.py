import pygame as pg

pg.init()



width, height = (1366, 726)

screen = pg.display.set_mode((width, height), pg.FULLSCREEN)

while True:

	pg.mouse.set_visible(True)

	clock = py.time.Clock(); 
	clock.tick(60)

	screen.fill((0,0,0))

	pg.draw.circle(screen, (255,255,255), (width/5.0, height/2.0), 50, 2)

	pygame.display.flip()

