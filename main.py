import input
import pokemon
import pygame
import menu


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
mouseObj = input.Mouse(screen)
main_menu = menu.Menu(screen)
main_menu.draw(screen)


def main():
	global main_menu
	running = True
	pygame.display.flip()
	while running:
		main_menu.draw(screen)
		mouseObj.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # Not technically an input but is grabbed as an event in the same way
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseObj.grab()
		pygame.display.flip()


if __name__ == "__main__":
	main()
