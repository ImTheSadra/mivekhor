from pygame import *

class Player:
	keyLeft = False
	keyRight = False
	keyTop = False
	keyDown = False
	score = 0
	def __init__(self, window:Surface, speed:int=2):
		self.window = window
		self.speed = speed
		self.rightOrLeft = "R"
		self.mode = 0
		self.img = self.getSurface()
		self.x = window.get_width()/2-self.img.get_width()/2
		self.y = window.get_height()/2-self.img.get_height()/2

	def getRect(self) -> Rect:
		r = Rect(
			self.x, self.y,
			self.img.get_width(),
			self.img.get_height()
		)
		return r

	def getSurface(self):
		img = image.load(f"./package/images/player/{self.rightOrLeft}run{str(round(self.mode))}.png")
		self.img = img
		return img

	def draw(self):
		if self.keyLeft:
			if self.x > 30:
				self.x -= self.speed
			self.mode += 0.1
			if round(self.mode) >= 9:
				self.mode = 0
		elif self.keyRight:
			if self.x < self.window.get_width()-30-self.img.get_width():
				self.x += self.speed
			self.mode += 0.1
			if round(self.mode) >= 9:
				self.mode = 0
		if self.keyTop:
			if self.y > 20:
				self.y -= self.speed
			self.mode += 0.1
			if round(self.mode) >= 9:
				self.mode = 0
		elif self.keyDown:
			if self.y < self.window.get_height()-self.img.get_height()-30:
				self.y += self.speed
			self.mode += 0.1
			if round(self.mode) >= 9:
				self.mode = 0

		img = self.getSurface()
		rect = self.getRect()
		rect.x -= img.get_width()/2

		self.window.blit(
			img,
			rect
		)

	def checkEvent(self, event):
		if not event.type in [KEYDOWN, KEYUP]:
			return

		if event.type == KEYUP:
			if event.key == K_a:self.keyLeft = False
			if event.key == K_d:self.keyRight = False
			if event.key == K_w:self.keyTop = False
			if event.key == K_s:self.keyDown = False
			return

		if event.key == K_a:
			self.rightOrLeft = "L"
			self.keyLeft = True

		elif event.key == K_d:
			self.rightOrLeft = "R"
			self.keyRight = True

		elif event.key == K_w:
			self.keyTop = True

		elif event.key == K_s:
			self.keyDown = True