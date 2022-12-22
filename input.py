import pygame
from math import ceil
import hover
import menu
import pokedex
from sys import exit as kill_game
import subprocess


def spawn_program_and_die(program, exit_code=0):
	"""
	Start an external program and exit the script
	with the specified return code.
	Takes the parameter program, which is a list
	that corresponds to the argv of your command.
	"""
	# Start the external program
	subprocess.Popen(program)
	# We have started the program, and can suspend this interpreter


class Mouse(object):
	def __init__(self, screen):
		self.mouse = None
		self.mousex = None
		self.mousey = None
		self.selmode = False
		self.hoverObj = hover.Hover(screen)
		self.screen = screen
		self.menuObj = menu.Menu(screen)
		self.dexObj = pokedex.Dex(screen)
		self.menuRect = pygame.Rect(0, 0, 850, 720)

	def grab(self):
		if self.selmode is True and self.mousex <= 800:
			print("Selected", ceil(self.mousex / 50))
		if self.mousex >= 900 and 72 <= self.mousey <= 144:
			self.screen.fill((255, 255, 255), self.menuRect)
			self.dexObj.draw()
		if self.mousex >= 900 and 420 <= self.mousey <= 560:
			self.screen.fill((255, 255, 255), self.menuRect)
		if self.mousex >= 900 and 144 <= self.mousey <= 216:
			self.screen.fill((255, 255, 255), self.menuRect)
			self.dexObj.draw()
			self.selmode = True
		if self.mousex >= 900 and 560 <= self.mousey <= 640:
			self.screen.fill((255, 255, 255), self.menuRect)
			spawn_program_and_die(['python', 'openai.py'])
		if self.mousex >= 900 and 640 <= self.mousey <= 720:
			kill_game(0)

	def get_pos(self):
		self.mouse = pygame.mouse.get_pos()
		self.mousex = self.mouse[0]
		self.mousey = self.mouse[1]

		if self.mousex >= 900 and 72 <= self.mousey <= 144:
			self.hoverObj.draw(900, 75, 350, 90)
		elif self.mousex >= 900 and 144 <= self.mousey <= 216:
			self.hoverObj.draw(900, 160, 350, 90)
		elif self.mousex >= 900 and 640 <= self.mousey <= 720:
			self.hoverObj.draw(900, 610, 350, 90)
		elif self.mousex >= 900 and 560 <= self.mousey <= 640:
			self.hoverObj.draw(900, 530, 350, 90)
		elif self.mousex >= 900 and 420 <= self.mousey <= 560:
			self.hoverObj.draw(900, 420, 350, 90)
		else:
			self.menuObj.draw(self.screen)
