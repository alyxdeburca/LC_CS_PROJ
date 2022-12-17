import pygame
from sys import exit as kill_game
from math import ceil
import hover
import menu
hovercolour = pygame.Color(0, 0, 0, 50)
hoverObj = hover.Hover()
screen = pygame.display.set_mode((1280, 720))
menuObj = menu.Menu(screen)
pygame.init()
def draw(left, top, width, height):
	rectsurf = pygame.Surface((width, height), pygame.SRCALPHA)
	rectsurf.fill(hovercolour)
	rectsurf.set_alpha(50)
	screen.blit(rectsurf, (left, top))

class Mouse(object):
	def __init__(self):
		self.mouse = None
		self.mousex = None
		self.mousey = None
		self.selmode = False


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
			# hoverObj.draw(900, 75, 350, 90)
			draw(900, 77, 350, 90)
		else:
			menuObj.draw(screen)
