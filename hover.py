import pygame

pygame.init()


class Hover(object):
	def __init__(self, screen):
		self.rectsurf = None
		self.hovercolour = pygame.Color((0, 0, 0, 50))
		self.screen = screen

	def draw(self, left, top, width, height):
		self.rectsurf = pygame.Surface((width, height), pygame.SRCALPHA)
		self.rectsurf.fill(self.hovercolour)
		self.rectsurf.set_alpha(100)
		self.screen.blit(self.rectsurf, (left, top))

