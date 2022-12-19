import pygame


class Sprite(object):
	def __init__(self, screen):
		self.screen = screen

	def draw(self, sprite, x, y):
		image = pygame.image.load("assets/sprites/" + str(sprite) + ".png")
		image = pygame.transform.scale(image, (50, 50))
		self.screen.blit(image, (x, y))
