import random

class Brick:
	def __init__(self, pos, size, color):
		self.pos = pos
		self.size = size
		self.color = color

	def collide(self, ball_pos, future_ball_pos, ball_r):

		x, y = abs(ball_pos[0] - self.pos[0] - self.size[0] // 2), abs(ball_pos[1] - self.pos[1] - self.size[1] // 2)

		if x <= self.size[0] // 2 + ball_r and y <= self.size[1] // 2 + ball_r:
			if ball_pos[1] <= self.pos[1] or ball_pos[1] >= self.pos[1] + self.size[1]:
				return 1, -1
			elif ball_pos[0] <= self.pos[0] or ball_pos[0] >= self.pos[0] + self.size[0]:
				return -1, 1
		return

		# if self.pos[0] - ball_r <= ball_pos[0] <= self.pos[0] + self.size[0] + ball_r:
		# 	if ball_pos[1] + ball_r <= self.pos[1] <= future_ball_pos[1] + ball_r or \
		# 			ball_pos[1] - ball_r >= self.pos[1] + self.size[1] >= future_ball_pos[1] - ball_r:
		# 		return 1, -1
		# if self.pos[1] - ball_r <= ball_pos[1] <= self.pos[1] + self.size[1] + ball_r:
		# 	if ball_pos[0] + ball_r <= self.pos[0] <= future_ball_pos[0] + ball_r or \
		# 			ball_pos[0] - ball_r >= self.pos[0] + self.size[0] >= future_ball_pos[0] - ball_r:
		# 		return -1, 1