import pygame
from main import drawsprite


def run():
	pygame.display.set_caption("Generation 1 PokeDex")  # Change Window Title to match current screen
	white = (255, 255, 255)  # RGB Colour Code for White
	black = (0, 0, 0)  # RGB Colour Code for Black
	pygame.init()  # Initialise pygame library
	pygame.font.init()  # Initialise Google Roboto Font
	font = pygame.font.Font('assets/fonts/Roboto-Regular.ttf', 15)
	screen = pygame.display.set_mode((1280, 720))  # Set Window Resolution to HD (1280*720)
	screen.fill(white)  # Set Background colour to white
	posx = 0  # Declare sprite starting position x
	posy = 0  # Declare sprite starting position y

	for i in range(0, 151):
		text = font.render(str(i+1), True, black)
		pygame.display.flip()
		width, height = drawsprite(i+1, posx, posy, 1)
		textrect = text.get_rect()
		textrect.center = (posx + width / 2, posy + height + 10)
		screen.blit(text, textrect)
		posx = posx + width
		if posx >= 1280 - width - 1280/3 - 5:
			posx = 0
			posy = posy + height + 20
