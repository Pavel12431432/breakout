from ball import Ball

class Drop(Ball):
	def __init__(self, pos, velocity, r, type):
		self.type = type
		self.pos = pos
		self.velocity = velocity
		self.r = r

	def collide_paddles(self, paddle1_y, paddle_height, paddle_width):
		if 50 - self.r < self.pos[0] < 50 + paddle_width + self.r and paddle1_y - self.r < self.pos[
			1] < paddle1_y + paddle_height + self.r:
			return True

	def update_position(self):
		self.pos = list(map(sum, zip(self.pos, self.velocity)))
		if self.pos[0] < self.r + 1:
			return True