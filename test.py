# -*- coding: utf-8 -*-
###############################################
# 重点：
# 		键盘、鼠标、
#		时间、图片的动态显示
#		文字的输出和输入
#
###############################################







# 导入pygame模块
import pygame


# 询问display模块是否加载，若是，返回1，若否，返回0。
getinit_0 = pygame.display.get_init()
print(getinit_0)

# pygame初始化 pygame.time.get_ticks()从零开始计数，以毫秒计时。
pygame.init()

# 设置窗口抬头
pygame.display.set_caption('test')

print(pygame.display.get_caption())

# 获得显示驱动名称，返回值为Quartz
print(pygame.display.get_driver())

# 获取窗口显示 返回值为：{}
print(pygame.display.get_wm_info())

# 获得可用的全屏显示模式 返回值为：[(1366, 768), (1344, 756), (1024, 768), (1024, 576), (800, 600), (640, 480)]
print(pygame.display.list_modes())

# 询问display模块是否加载，若是，返回1，若否，返回0。
getinit_1 = pygame.display.get_init()
print(getinit_1)

# pygame设置显示窗口的大小
size = width, height = 500, 500

# 显示窗口
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

# 设定gamma值
pygame.display.set_gamma(1, 1, 1)


# 获得从pygame.init()开始，时间过了多少，以毫秒计时。
getticks_0 = pygame.time.get_ticks()
print(getticks_0)

# 暂停程序500毫秒
pygame.time.wait(500)

# 再次获得init()开始后的时钟。
getticks_1 = pygame.time.get_ticks()
print(getticks_1)

# 暂停程序，使用CPU计时，比wait更加准确。
pygame.time.delay(500)

# 再次获得init()开始后的时钟。
getticks_2 = pygame.time.get_ticks()
print(getticks_2)


white = (255, 255, 255)
black = (0  , 0  , 0  )



# 获取相机名称


i = 0

while True:
	
	screen.fill((0, 0, 0))
	# 画矩形，pointlist中的前两位数是起始点，后两位（宽，高）是边长
	pygame.draw.rect(screen, white,[125,125,150,150],1) 
	# 画多边形，点对在list中，顺序则是连线的顺序。
	pygame.draw.polygon(screen, white, [(250 ,0), (0, 250), (250, 500), (500, 250)], 1 )
	# 画圆，
	pygame.draw.circle(screen, white,(250, 250), 200, 1)
	
	i += 1
	if i == 200:
		break

	pos = pygame.mouse.get_pos()
	print(pos)
	rel = pygame.mouse.get_rel()
	print(rel)





	pygame.display.flip()
# 退出pygame显示
pygame.display.quit()