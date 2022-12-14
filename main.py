import json
from sys import exit as gkill
import pygame
from math import ceil

# Self-Written Libraries
import drawHover
import pokedex
import menu
import options
import pokeselect
import fileio

##############
#            #
# SETUP CODE #
#            #
##############

my_team = []
pokecount = 0
white = (255, 255, 255)  # RGB Colour Code for White
black = (0, 0, 0)  # RGB Colour Code for Black
DEFAULT_IMAGE_SIZE = (50, 50)  # Set Default Sprite size to 50px*50px. All sprites will be drawn as a multiple of this
pygame.init()  # Initialise pygame library
pygame.display.set_caption("Pokemon Battle Sim")  # Set Caption for main menu
screen = pygame.display.set_mode((1280, 720))  # Set Window Resolution to HD (1280*720)
screen.fill(white)  # Set Background colour to white
FRAME_PER_SECOND_CLOCK = pygame.time.Clock()
FRAME_PER_SECOND_CLOCK.tick(60)
width = screen.get_width()  # Store screen horizontal resolution as a variable
height = screen.get_height()  # Store screen vertical resolution as a variable


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
	global mouse
	global selector
	global pokecount
	mouse = pygame.mouse.get_pos()  # Grab position of mouse pointer
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  # Not technically an input but is grabbed as an event in the same way
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if mouse[0] >= width / 3 * 2 and height / 10 <= mouse[1] <= height / 10 * 2:  # If POKÉDEX button is clicked
				pygame.display.set_caption("Generation 1 PokeDex")
				pokedex.run()
			if mouse[0] >= width / 3 * 2 and height - 80 <= mouse[1] <= height:  # If QUIT button is clicked
				running = False
				gkill(0)
			if mouse[0] >= width / 3 * 2 and height - 160 <= mouse[1] <= height - 80:
				options.run()
			if mouse[0] >= 900 and 144 <= mouse[1] <= 216:
				global selector
				pygame.display.set_caption("Choose 6 Pokemon")
				pokedex.run()
				pokeselect.run()
				selector = True
			if mouse[0] >= width / 3 * 2 and height - 300 <= mouse[1] <= height - 160:
				fileio.save(my_team)
			if selector:
				print(my_team)
				selectedx = ceil(mouse[0] / 50)
				selectedy = ceil(mouse[1] / 66)
				if selectedy == 1 and selectedx < 800:
					drawHover.run(50 * (selectedx - 1), 50 * (selectedy - 1), 50, 66)
				elif 10 > selectedy > 1 and selectedx < 800:
					drawHover.run(50 * (selectedx - 1), (selectedy - 1) * 70, 50, 66)
					my_team.append(selectedx+((selectedy-1)*16))
				if selectedy > 10 and selectedx <= 6:
					drawHover.run(50 * (selectedx - 1), 630, 50, 66)
					my_team.append(selectedx+((selectedy-1)*16))

	if mouse[0] >= width / 3 * 2 and height / 10 <= mouse[1] <= height / 10 * 2:  # PokeDex
		drawHover.run(900, 75, 350, 90)
	if mouse[0] >= 900 and 144 <= mouse[1] <= 216:
		drawHover.run(900, 160, 350, 90)
	if mouse[0] >= width / 3 * 2 and height - 80 <= mouse[1] <= height:  # Exit
		drawHover.run(900, height - 110, 350, 90)
	if mouse[0] >= width / 3 * 2 and height - 160 <= mouse[1] <= height - 80:  # Option
		drawHover.run(900, height - 190, 350, 90)
	if mouse[0] >= width / 3 * 2 and height - 300 <= mouse[1] <= height - 160:  # Save
		drawHover.run(900, height - 300, 350, 90)


def main():
	global running
	global selector
	selector = False
	running = True
	while running:
		menu.draw_menu()  # Draw main menu to screen
		read_input()  # Read user input and window state
		pygame.display.flip()  # Update display
		if len(my_team) > 6:
			selector = False
			pygame.display.set_caption("Press Save to save your team")


if __name__ == "__main__":  # Do not run this file if referenced as a module, only if run independently
	main()
