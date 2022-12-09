import pygame

screen = pygame.display.set_mode((1280, 720))
MENU_SIZE = (1280 / 3, 720)


def draw_menu():
	image = pygame.image.load("assets/menu/main.png")
	image = pygame.transform.scale(image, MENU_SIZE)
	screen.blit(image, (1280 / 3 * 2, 0))
	width = image.get_width()
	height = image.get_height()
	return width, height
