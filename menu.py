import pygame


class Menu(object):
	def __init__(self, screen):
		self.image = None
		self.screen = screen
		self.MENU_SIZE = (1280 / 3, 720)

	def draw(self, screen):
		self.image = pygame.image.load("assets/menu/main.png").convert()
		self.image = pygame.transform.scale(self.image, self.MENU_SIZE)
		screen.blit(self.image, (1280 / 3 * 2, 0))
