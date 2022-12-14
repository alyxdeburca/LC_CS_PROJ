import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))


def run(left, top, width, height):
	hovercolour = pygame.Color(0, 0, 0, 50)
	rectsurf = pygame.Surface((width, height), pygame.SRCALPHA)
	rectsurf.fill(hovercolour)
	screen.blit(rectsurf, (left, top))

