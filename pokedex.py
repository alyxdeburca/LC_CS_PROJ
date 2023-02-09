import pygame
import sprite


class Dex(object):
	def __init__(self, screen):
		pygame.init()
		pygame.font.init()
		self.font = pygame.font.Font('assets/fonts/Roboto-Regular.ttf', 15)
		self.black = (0, 0, 0)  # RGB Colour Code for Black
		self.posx = 0  # Declare sprite starting position x
		self.posy = 0  # Declare sprite starting position y
		self.screen = screen
		self.scale = 1

	def draw(self):
		for i in range(0, 151):
			text = self.font.render(str(i + 1), True, (0, 0, 0))
			spriteobj = sprite.Sprite(self.screen)
			spriteobj.draw(i + 1, self.posx, self.posy, self.scale)
			textrect = text.get_rect()
			textrect.center = (self.posx + 50 / 2, self.posy + 50 + 10)
			self.screen.blit(text, textrect)
			self.posx = self.posx + 50
			if self.posx >= 1280 - 50 - 1280 / 3 - 5:
				self.posx = 0
				self.posy = self.posy + 50 + 20
			if i == 150:
				self.posx = 0
				self.posy = 0
		pygame.display.flip()

