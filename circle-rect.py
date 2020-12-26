import pygame
from pygame import gfxdraw
import math

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Circle/Rectangle collision')
font = pygame.font.SysFont('microsoftyaheimicrosoftyaheiuibold', 20)
clock = pygame.time.Clock()

circle_pos = (400, 300)
circle_radius = 30

rect = pygame.Rect(300, 250, 400, 100)


def draw_circle(surface, x, y, radius, color):
	gfxdraw.aacircle(surface, int(x), int(y), radius, color)
	gfxdraw.filled_circle(surface, int(x), int(y), radius, color)


def dist(p1, p2, x, y):
	x0, y0, x1, y1, x2, y2 = x, y, *p1, *p2
	return abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1)) / math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def dist2(p1, p2):
	return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def circle_rect(c_x, c_y, r, r_x, r_y, r_w, r_h):
	t_x = c_x
	t_y = c_y

	if c_x < r_x: t_x = r_x
	elif c_x > r_x + r_w: t_x = r_x + r_w

	if c_y < r_y: t_y = r_y
	elif c_y > r_y + r_h: t_y = r_y + r_h

	return dist2((c_x, c_y), (t_x, t_y)) <= r ** 2, t_x != c_x, t_y != c_y


def inp():
	global circle_pos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
	circle_pos = pygame.mouse.get_pos()


while True:
	screen.fill((0, 0, 0))

	colliding = circle_rect(circle_pos[0], circle_pos[1], circle_radius, rect.left, rect.top, rect.width, rect.height)

	color = (200, 150, 50) if colliding[0] else (200, 200, 200)

	gfxdraw.box(screen, rect, color)
	draw_circle(screen, circle_pos[0], circle_pos[1], circle_radius, color)

	text = font.render(str(colliding[1]) + ' ' + str(colliding[2]), True, (50, 250, 50))
	text_rect = text.get_rect(topleft=(10, 10))
	screen.blit(text, text_rect)

	pygame.display.update()
	inp()