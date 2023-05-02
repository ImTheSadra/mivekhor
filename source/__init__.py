from pygame import *
init()
from pygame.font import init, Font, get_default_font
init()
import sys
from .player import Player
from .fruit import Fruit
from .khabis import Khabis

# make screen
w, h = 600, 600
screen = display.set_mode((w, h))

# asigment's
font = Font(get_default_font(), 25)
font2 = Font(get_default_font(), 80)

bg = image.load("./package/images/background.png")
bg = transform.scale(bg, (w, h))

player = Player(screen)
fruit = Fruit(screen)
khabis = Khabis(screen)
khabis.setFruit(fruit)

def gameOver():
	text = font2.render("Game over", True, (255,0,0))
	text2 = font.render("Press any key to continue...", True, (255,0,0))
	screen.fill((255,255,255))
	screen.blit(text,
		(
			w/2-text.get_width()/2,
			h/2-text.get_height()/2
		)
	)
	screen.blit(
		text2,
		(
			w/2-text2.get_width()/2,
			h/3-text2.get_height()/2
		)
	)
	screen.fill((255,255,255))
	display.update()
	run = True
	while run:
		for ev in event.get():
			if ev.type == QUIT:sys.exit()
			if ev.type == KEYDOWN:
				run = False
				return

def gameWin():
	text = font2.render("Game Win", True, (0,255,0))
	text2 = font.render("Press any key to continue...", True, (0,255,0))
	screen.fill((255,255,255))
	screen.blit(text,
		(
			w/2-text.get_width()/2,
			h/2-text.get_height()/2
		)
	)
	screen.blit(
		text2,
		(
			w/2-text2.get_width()/2,
			h/3*2-text2.get_height()/2
		)
	)
	display.update()
	run = True
	while run:
		for ev in event.get():
			if ev.type == QUIT:sys.exit()
			if ev.type == KEYDOWN:
				run = False
				return

while True:
	if player.score <= -1:
		gameOver()
		player = Player(screen)
		khabis = Khabis(screen)
		khabis.setFruit(fruit)
	elif player.score >= 10:
		gameWin()
		player = Player(screen)
		khabis = Khabis(screen)
		khabis.setFruit(fruit)
	screen.blit(bg, (0,0))
	fruit.draw()
	player.draw()
	khabis.draw()
	rect = player.getRect().copy()
	rect.x -= rect.w
	rect.w = rect.w*2
	rect.y -= rect.h
	rect.h = rect.h*2
	if fruit.check(rect):
		player.score += 1
		fruit.reGenerate()
		khabis.setFruit(fruit)
	if fruit.check(khabis.getRect()):
		player.score -= 1
		fruit.reGenerate()
		khabis.setFruit(fruit)
	screen.blit(
		font.render("score > {0}".format(str(player.score)), True, (0,0,0)),
		(2, 2)
	)

	for ev in event.get():
		if ev.type == QUIT:sys.exit()
		player.checkEvent(ev)

	display.update()
	clock = time.Clock()
	clock.tick(clock.get_fps())