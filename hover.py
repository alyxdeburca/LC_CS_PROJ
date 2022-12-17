import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))


class Hover(object):
	def __init__(self):
		self.rectsurf = None
		self.hovercolour = pygame.Color((0, 0, 0, 50))
		self.screen = screen

	# def draw(self, left, top, width, height):
	# 	self.rectsurf = pygame.Surface((width, height), pygame.SRCALPHA)
	# 	self.rectsurf.fill(self.hovercolour)
	# 	screen.blit(self.rectsurf, (left, top))
