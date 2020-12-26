import pygame
import random
import math
from brick import Brick
from ball import Ball
from drop import Drop

# configuration constants
WIDTH, HEIGHT = 800, 600
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 15
MOVEMENT_SPEED = 8
MAX_BALL_SPEED = 2
MAX_BALLS = 9

# init pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('BreakOut')
font = pygame.font.SysFont('microsoftyaheimicrosoftyaheiuibold', 20)
clock = pygame.time.Clock()

# initial state
paddle_y = 300 - PADDLE_HEIGHT // 2


def inp():
	global paddle_y
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
	# update paddle positions on key press
	if pygame.key.get_pressed()[ord('a')]:
		paddle_y = min(max(paddle_y - MOVEMENT_SPEED, 0), HEIGHT - PADDLE_HEIGHT)
	if pygame.key.get_pressed()[ord('z')]:
		paddle_y = min(max(paddle_y + MOVEMENT_SPEED, 0), HEIGHT - PADDLE_HEIGHT)




def loop():
	global balls, paddle_y, bounces_left
	screen.fill((0, 0, 0))
	# draw paddle
	pygame.draw.rect(screen, (200, 200, 200), ((50, paddle_y), (PADDLE_WIDTH, PADDLE_HEIGHT)))

	for ball in balls:

		for brick in bricks:
			brick.color = (200, 50, 50)
			r = brick.collide(ball.pos, list(map(sum, zip(ball.pos, ball.velocity))), ball.r)
			if r:
				bricks.remove(brick)
				brick.color = (50, 200, 50)
				if random.random() <= 0.01:
					drops.append(Drop([brick.pos[0] + brick.size[0] // 2, brick.pos[1] + brick.size[1] // 2],
									  (-MAX_BALL_SPEED, 0), 4, 'no-bounce'))
				if not bounces_left:
					ball.velocity = list(map(lambda x: x[0] * x[1], zip(ball.velocity, r)))
					break
				else:
					bounces_left -= 1

		# update ball pos
		if ball.update_position():
			# balls.remove(ball)
			print('end')
		# check ball collisions
		ball.collide_edges(WIDTH, HEIGHT)
		ball.collide_paddles(paddle_y, PADDLE_HEIGHT, PADDLE_WIDTH)

		# draw ball
		pygame.draw.circle(screen, (200, 200, 200), tuple(map(int, ball.pos)), ball.r)

	for brick in bricks:
		pygame.draw.rect(screen, brick.color, (brick.pos, brick.size))

	for drop in drops:
		pygame.draw.circle(screen, (50, 200, 50), tuple(map(int, drop.pos)), drop.r)
		if drop.update_position():
			drops.remove(drop)
		if drop.collide_paddles(paddle_y, PADDLE_HEIGHT, PADDLE_WIDTH):
			if len(balls) <= MAX_BALLS / 3 and drop.type == 'split':
				b = []
				for ball in balls:
					a = math.atan(ball.velocity[1] / ball.velocity[0])
					b.append(Ball(ball.pos, [MAX_BALL_SPEED * math.cos(a - 0.26) * 1 if ball.velocity[0] > 0 else -1,
											 MAX_BALL_SPEED * math.sin(a - 0.26)], 10, MAX_BALL_SPEED))
					b.append(Ball(ball.pos, [MAX_BALL_SPEED * math.cos(a + 0.26) * 1 if ball.velocity[0] > 0 else -1,
											 MAX_BALL_SPEED * math.sin(a + 0.26)], 10, MAX_BALL_SPEED))
				balls.extend(b)
			if drop.type == 'no-bounce':
				bounces_left += 10
			drops.remove(drop)

	text = font.render(str(int(clock.get_fps())), True, (50, 250, 50))
	text_rect = text.get_rect(topleft=(10, 10))
	screen.blit(text, text_rect)

	pygame.display.update()


balls = [Ball((50 + PADDLE_WIDTH + 10 + 100, paddle_y + PADDLE_HEIGHT // 2),
			  [MAX_BALL_SPEED * math.cos(0), MAX_BALL_SPEED * math.sin(0)], 10, MAX_BALL_SPEED)]
bricks = [Brick((x + 2, y + 2), (20 - 4, 40 - 4), (200, 50, 50)) for x in range(400, 720, 20) for y in
		  range(80, 520, 40)]
drops = []
bounces_left = 0

while True:
	inp()
	loop()
	clock.tick(144)