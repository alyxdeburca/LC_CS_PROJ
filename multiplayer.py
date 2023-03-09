#!/usr/bin/python3
import pygame
import sys
from pokeclass import Pokemon
import font
from time import sleep

# Set up Pygame and the window
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
clock.tick(10)
# Load the player's party of Pokémon
player_party = [Pokemon.pikachu(), Pokemon.Squirtle(), Pokemon.Charmander()]
# Load the opponent's party of Pokémon
opponent_party = [Pokemon.Bulbasaur(), Pokemon.Caterpie(), Pokemon.Weedle()]
# Set up the current Pokémon for each trainer
player_pokemon = player_party[0]
opponent_pokemon = opponent_party[0]
screen.fill((255, 255, 255))
pygame.display.set_caption("Pokemon Battle Sim")


def draw_pokemon(pokemon, position):
	# Load the Pokémon's sprite
	sprite = pygame.image.load(pokemon.sprite_path).convert_alpha()

	# Scale the sprite to the desired size
	sprite = pygame.transform.scale(sprite, (100, 100))

	# Blit the sprite onto the screen at the specified position
	screen.blit(sprite, position)


def refreshMoves():
	screen.fill((255, 255, 255))
	i = 0
	global move
	if move % 2 != 0:
		print(opponent_party[0])
		for option in opponent_party[0].moves:
			font.drawText(str(i + 1) + " " + option.name, "assets/fonts/Font.png", (0, 400 + (80 * i)), screen, 0.5)
			pygame.display.flip()
			i = i + 1
	else:
		for option in player_party[0].moves:
			font.drawText(str(i + 1) + " " + option.name, "assets/fonts/Font.png", (0, 400 + (80 * i)), screen, 0.5)
			pygame.display.flip()
			i = i + 1


move = 0
refreshMoves()
# Set up the battle loop
hp_lvls = []
opp_hp = []
while True:
	opponent_party[0].level = 100
	player_party[0].level = 100
	# Handle events
	if move % 2 == 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYUP:
				# Check for player input to select a move
				if event.key == pygame.K_1:
					player_pokemon.use_move(player_pokemon.moves[0], opponent_pokemon)
					if opponent_pokemon.is_fainted():
						print(f'{opponent_pokemon.name} has fainted!')
				if event.key == pygame.K_2:
					player_pokemon.use_move(player_pokemon.moves[1], opponent_pokemon)
					if opponent_pokemon.is_fainted():
						print(f'{opponent_pokemon.name} has fainted!')
				if event.key == pygame.K_3:
					player_pokemon.use_move(player_pokemon.moves[2], opponent_pokemon)
					if opponent_pokemon.is_fainted():
						print(f'{opponent_pokemon.name} has fainted!')
				if event.key == pygame.K_4:
					player_pokemon.use_move(player_pokemon.moves[3], opponent_pokemon)
					if opponent_pokemon.is_fainted():
						print(f'{opponent_pokemon.name} has fainted!')
				player_pokemon.update()
				opponent_pokemon.update()
				move = move + 1
				screen.fill((255, 255, 255))
				refreshMoves()
	else:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYUP:
				# Check for player input to select a move
				if event.key == pygame.K_1:
					opponent_pokemon.use_move(opponent_pokemon.moves[0], player_pokemon)
					if player_pokemon.is_fainted():
						print(f'{player_pokemon.name} has fainted!')
				if event.key == pygame.K_2:
					opponent_pokemon.use_move(opponent_pokemon.moves[1], player_pokemon)
					if player_pokemon.is_fainted():
						print(f'{player_pokemon.name} has fainted!')
				if event.key == pygame.K_3:
					opponent_pokemon.use_move(opponent_pokemon.moves[2], player_pokemon)
					if player_pokemon.is_fainted():
						print(f'{player_pokemon.name} has fainted!')
				if event.key == pygame.K_4:
					opponent_pokemon.use_move(opponent_pokemon.moves[3], player_pokemon)
					if player_pokemon.is_fainted():
						print(f'{player_pokemon.name} has fainted!')
				player_pokemon.update()
				opponent_pokemon.update()
				move = move + 1
				screen.fill((255, 255, 255))
				refreshMoves()
	# Update the game state
	# Check if either Pokémon has fainted
	if player_pokemon.is_fainted():
		hp_lvls = []
		# Check if the player has any remaining Pokémon
		if len(player_party) > 1:
			player_party.pop(0)
			player_pokemon = player_party[0]
			refreshMoves()
		else:
			# The player has lost the battle
			print("You have no remaining Pokémon!")
			break
	if opponent_pokemon.is_fainted():
		opp_hp = []
		# Check if the opponent has any remaining Pokémon
		if len(opponent_party) > 1:
			opponent_party.pop(0)
			opponent_pokemon = opponent_party[0]
		else:
			# The player has won the battle
			opponent_party = []
			player_party = []
			screen.fill((0, 0, 0))
			font.drawText("WINNER", "assets/fonts/Font.png", (400, 280), screen, 1)
			print("You have defeated the opponent!")
			pygame.display.flip()
			sleep(10)
			break

	# Render the battle screen
	if len(player_party) >= 1 or len(opponent_party) >= 1:
		draw_pokemon(player_pokemon, (50, 50))
		draw_pokemon(opponent_pokemon, (550, 50))
		hp_lvls.append(int(player_party[0].stats['hp']))
		opp_hp.append(int(opponent_party[0].stats['hp']))
		if hp_lvls[-1] > 0:
			pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(50, 180, (hp_lvls[-1]) / max(hp_lvls) * 100, 10))
		if opp_hp[-1] > 0:
			pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(550, 180, (opp_hp[-1]) / max(opp_hp) * 100, 10))

	pygame.display.flip()
