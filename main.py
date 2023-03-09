import input
import pokemon
import pygame
import menu
import font
import pokedex
import subprocess
from sys import exit


class Player(pokemon.Pokemon):
	def __init__(self, health, player, accuracy, entry):
		super().__init__(health, player, accuracy, entry)
		self.health = health
		self.player = player
		self.accuracy = accuracy
		self.name = "Player"
		if len(self.moves["type"]) == 2:
			self.moves["type"] = self.moves["type"][0]


white = (255, 255, 255, 255)  # RGB Colour Code for White
pygame.init()  # Initialise pygame library
pygame.display.set_caption("Pokemon Battle Sim")  # Set Caption for main menu
screen = pygame.display.set_mode((1280, 720))
screen.fill(white)  # Set Background colour to white
screen.convert_alpha()
FRAME_PER_SECOND_CLOCK = pygame.time.Clock()
FRAME_PER_SECOND_CLOCK.tick(60)
main_menu = menu.Menu(screen)
main_menu.draw(screen)


def main():
	battle = False
	running = True
	pygame.display.flip()
	while running:
		font.drawText("POKEMON", "assets/fonts/Font.png", (170, 50), screen, 1)
		font.drawText("Battle", "assets/fonts/Font.png", (210, 140), screen, 1)
		font.drawText("Simulator", "assets/fonts/Font.png", (80, 230), screen, 1)
		main_menu.draw(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # Not technically an input but is grabbed as an event in the same way
				running = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_1:
					pokedex.Dex(screen).draw()
				if event.key == pygame.K_2:
					battlesim = subprocess.Popen(['python', 'battle.py'])
					battle = True
				if event.key == pygame.K_3:
					battlesim = subprocess.Popen(['python', 'multiplayer.py'])
				if event.key == pygame.K_4:
					battlesim = subprocess.Popen(['python', 'simulation.py'])
					pygame.display.iconify()
				if event.key == pygame.K_5:
					if battle is True:
						battlesim.kill()
					exit(0)

		pygame.display.flip()


if __name__ == "__main__":
	main()
