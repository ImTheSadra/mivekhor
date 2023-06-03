from pygame import *

class Khabis:
	mode = 0
	fruit = None
	speed = 1
	modeStr = ""
	def __init__(self, window:Surface):
		self.window = window
		self.x = 70
		self.y = 120
		self.getSurface()

	def setFruit(self, fruit):
		self.fruit = fruit

	def getSurface(self):
		img = image.load(f"./package/images/khabis/{self.modeStr}run{round(self.mode)}.png")
		self.img = img
		return img

	def getRect(self) -> Rect:
		rect = Rect(
			self.x,self.y,
			self.img.get_width(),
			self.img.get_height()
		)
		return rect

	def draw(self):
		if self.fruit != None:
			if self.fruit.x > self.x:
				self.x += self.speed
				self.modeStr = ""
			if self.fruit.y > self.y:
				self.y += self.speed
			if self.fruit.x < self.x:
				self.x -= self.speed
				self.modeStr = "L"
			if self.fruit.y < self.y:
				self.y -= self.speed
		self.mode += 0.3
		if round(self.mode) > 5:
			self.mode = 0.0

		rect = self.getRect()
		img = self.getSurface()
		if rect.collidepoint(mouse.get_pos()):
			name = image.load("./package/images/khabis/name.png")
			self.window.blit(
				name, (rect.x, rect.y-name.get_height()-1)
			)
		self.img = img
		self.window.blit(
			img, rect
		)