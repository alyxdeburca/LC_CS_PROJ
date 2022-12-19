import pygame
from sys import exit as kill_game
from math import ceil
import hover
import menu
hovercolour = pygame.Color(0, 0, 0, 50)
pygame.init()


class Mouse(object):
	def __init__(self, screen):
		self.mouse = None
		self.mousex = None
		self.mousey = None
		self.selmode = False
		self.hoverObj = hover.Hover(screen)
		self.screen = screen
		self.menuObj = menu.Menu(screen)

	def grab(self):
		if self.selmode is True and self.mousex <= 800:
			print("Selected", ceil(self.mousex/50))
		if self.mousex >= 900 and 72 <= self.mousey <= 144:
			print("Pokedex")
		if self.mousex >= 900 and 144 <= self.mousey <= 216:
			print("Pokemon")
			self.selmode = True
		if self.mousex >= 900 and 560 <= self.mousey <= 640:
			print("Options")
		if self.mousex >= 900 and 640 <= self.mousey <= 720:
			print("Quit")
			kill_game(0)

	def get_pos(self):
		self.mouse = pygame.mouse.get_pos()
		self.mousex = self.mouse[0]
		self.mousey = self.mouse[1]

		if self.mousex >= 900 and 72 <= self.mousey <= 144:
			self.hoverObj.draw(900, 75, 350, 90)
		elif
		else:
			self.menuObj.draw(self.screen)
