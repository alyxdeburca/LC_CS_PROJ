import drawHover
import menu
import pokedex
import pygame
pokecount=0
def run():
	global selector
	global pokecount
	selector = True
	mouse = pygame.mouse.get_pos()
	print(mouse[0]/50)
