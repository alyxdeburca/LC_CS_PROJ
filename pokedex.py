import pygame
from menu import draw_menu
from main import drawsprite


def run():
	pygame.display.set_caption("Generation 1 PokeDex")
	white = (255, 255, 255)
	black = (0, 0, 0)
	pygame.init()
	pygame.font.init()
	pygame.font.get_init()
	font = pygame.font.Font('assets/fonts/Roboto-Regular.ttf', 12)
	screen = pygame.display.set_mode((1280, 720))
	screen.fill(white)
	posx = 0
	posy = 0
	draw_menu()

	for i in range(1, 151):
		text = font.render(str(i), True, black)
		pygame.display.flip()
		width, height = drawsprite(i, posx, posy, 1)
		textrect = text.get_rect()
		textrect.center = (posx + width / 2, posy + height + 10)
		screen.blit(text, textrect)
		posx = posx + width
		if posx >= 1280 - width - 1280/3 - 5:
			posx = 0
			posy = posy + height + 20
