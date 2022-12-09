import json
from sys import exit as gkill
import pygame
import pokedex
from menu import draw_menu

##############
#            #
# SETUP CODE #
#            #
##############

white = (255, 255, 255)  # RGB Colour Code for White
black = (0, 0, 0)  # RGB Colour Code for Black
DEFAULT_IMAGE_SIZE = (50, 50)  # Set Default Sprite size to 50px*50px. All sprites will be drawn as a multiple of this
pygame.init()  # Initialise pygame library
pygame.display.set_caption("Pokemon Battle Sim")  # Set Caption for main menu
screen = pygame.display.set_mode((1280, 720))  # Set Window Resolution to HD (1280*720)
screen.fill(white)  # Set Background colour to white
font = pygame.font.Font('assets/fonts/Roboto-Regular.ttf', 12)  # Import Google Roboto Font from assets folder
FRAME_PER_SECOND_CLOCK = pygame.time.Clock()
FRAME_PER_SECOND_CLOCK.tick(60)
width = screen.get_width()
height = screen.get_height()


def drawsprite(dex, x, y, scale):
	image = pygame.image.load("assets/sprites/" + str(dex) + ".png")  # Open Sprite from File
	# Set the Sprites size to a multiple of DEFAULT_IMAGE_SIZE
	image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE * scale)
	screen.blit(image, (x, y))  # Draw the Sprite to the Screen
	imgwidth = image.get_width()  # Get horizontal resolution of Sprite PNG
	imgheight = image.get_height()  # Get vertical resolution of Sprite PNG
	return imgwidth, imgheight


def read_dex(poke):
	with open("dex.json", "r") as f:
		full_dex = f.read()  # Read Pokédex from dex.json
		dex_json = json.loads(full_dex)  # Convert json string to dictionary
		# Return Pokédex entry and Types of a given Pokémon
		return dex_json["pokedex"][poke]["entry"], dex_json["pokedex"][poke]["type"]


def read_input():
	global running
	mouse = pygame.mouse.get_pos()  # Grab position of mouse pointer
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  # Not technically an input but is grabbed as an event in the same way
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if mouse[0] >= width / 3 * 2 and height / 10 <= mouse[1] <= height / 10 * 2:  # If POKÉDEX button is clicked
				pokedex.run()
				draw_menu()
			if mouse[0] >= width / 3 * 2 and height - 80 <= mouse[1] <= height:  # If QUIT button is clicked
				running = False
				gkill(0)


def main():
	global running
	running = True
	while running:
		draw_menu()  # Draw main menu to screen
		read_input()  # Read user input and window state
		pygame.display.flip()  # Update display


if __name__ == "__main__":  # Do not run this file if referenced as a module, only if run independently
	main()
