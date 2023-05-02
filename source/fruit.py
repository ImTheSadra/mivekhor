from pygame import *
from random import choice

def aFruit() -> Surface:
	fruits = [
		"apple",
		"carrot",
		"bannana",
		"hendevane",
		"totfarangi",
		"cacke2", "cacke",
		"humber",
		"cockie", "goje"
	] 
	img = image.load("./package/images/{0}.png".format(choice(fruits)))
	img = transform.scale(
		img,
		(img.get_width()*2, img.get_height()*2)
	)
	return img

class Fruit:
	def __init__(self, window:Surface):
		self.window = window
		self.img = aFruit()
		self.x = choice(range(50, 600-50))
		self.y = choice(range(50, 600-50))

	def draw(self):
		self.window.blit(self.img, (self.x, self.y))

	def reGenerate(self):
		self.__init__(self.window)

	def getRect(self) -> Rect:
		r = Rect(
			self.x, self.y,
			self.img.get_width(),
			self.img.get_height()
		)

	def check(self, rect:Rect):
		result = rect.collidepoint(self.x, self.y)
		if result:
			draw.circle(
				self.window,
				(78, 237, 81),
				(
					self.x+self.img.get_width()/2,
					self.y+self.img.get_height()/2
				),
				width=2, radius=15
			)
		return result