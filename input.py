import pygame
from math import ceil
import hover
import menu
import pokedex
from sys import exit
import subprocess
import sprite

class Mouse(object):
	def __init__(self, screen):
		self.battle = False
		self.battlesim = None
		self.mouse = None
		self.mousex = None
		self.mousey = None
		self.selmode = False
		self.hoverObj = hover.Hover(screen)
		self.screen = screen
		self.menuObj = menu.Menu(screen)
		self.dexObj = pokedex.Dex(screen)
		self.menuRect = pygame.Rect(0, 0, 850, 720)
		self.sprite = sprite.Sprite(screen)

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
			for i in range(6):
				if i <= 4:
					self.sprite.draw(25, 0+(50*4*i), (720/2)-150, 4)
					self.sprite.draw(7, 0+(50*4*i), (720/2)-150, 4)
					self.sprite.draw(4, 0+(50*4*i), (720/2)-150, 4)
					self.sprite.draw(1, 0+(50*4*i), (720/2)-150, 4)
				else:
					self.sprite.draw(10, 0 + (50 * 4 * i-4), (720 / 2) +200, 4)
					self.sprite.draw(13, 0 + (50 * 4 * i-4), (720 / 2) +200, 4)
		if self.mousex >= 900 and 560 <= self.mousey <= 640:
			self.screen.fill((255, 255, 255), self.menuRect)
			self.battlesim = subprocess.Popen(['python', 'battle.py'])
			self.battle = True
		if self.mousex >= 900 and 640 <= self.mousey <= 720:
			if self.battle is True:
				self.battlesim.kill()
			exit(0)

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
