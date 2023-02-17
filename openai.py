#!/usr/bin/python3
import pygame
import sys
import random
from pokeclass import Pokemon

# Set up Pygame and the window
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Load the player's party of Pokémon
player_party = [Pokemon.Pikachu(), Pokemon.Squirtle(), Pokemon.Charmander()]
# Load the opponent's party of Pokémon
opponent_party = [Pokemon.Bulbasaur(), Pokemon.Caterpie(), Pokemon.Weedle()]
# Set up the current Pokémon for each trainer
player_pokemon = player_party[0]
opponent_pokemon = opponent_party[0]

def draw_pokemon(pokemon, position):
	# Load the Pokémon's sprite
	sprite = pygame.image.load(pokemon.sprite_path).convert_alpha()

	# Scale the sprite to the desired size
	sprite = pygame.transform.scale(sprite, (100, 100))

	# Blit the sprite onto the screen at the specified position
	screen.blit(sprite, position)
# Set up the battle loop
while True:
	opponent_party[0].level = 100
	player_party[0].level = 100

	# Handle events
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
				else:
					move = random.choice(opponent_pokemon.moves)
					attacker = player_pokemon
					opponent_pokemon.use_move(move, attacker)
				player_pokemon.update()
				opponent_pokemon.update()
			if event.key == pygame.K_2:
				player_pokemon.use_move(player_pokemon.moves[1], opponent_pokemon)
				if opponent_pokemon.is_fainted():
					print(f'{opponent_pokemon.name} has fainted!')
				else:
					move = random.choice(opponent_pokemon.moves)
					attacker = player_pokemon
					opponent_pokemon.use_move(move, attacker)
				player_pokemon.update()
				opponent_pokemon.update()
			if event.key == pygame.K_3:
				player_pokemon.use_move(player_pokemon.moves[2], opponent_pokemon)
				if opponent_pokemon.is_fainted():
					print(f'{opponent_pokemon.name} has fainted!')
				else:
					move = random.choice(opponent_pokemon.moves)
					attacker = player_pokemon
					opponent_pokemon.use_move(move, attacker)
				player_pokemon.update()
				opponent_pokemon.update()
			if event.key == pygame.K_4:
				player_pokemon.use_move(player_pokemon.moves[3], opponent_pokemon)
				if opponent_pokemon.is_fainted():
					print(f'{opponent_pokemon.name} has fainted!')
				else:
					move = random.choice(opponent_pokemon.moves)
					attacker = player_pokemon
					opponent_pokemon.use_move(move, attacker)
				player_pokemon.update()
				opponent_pokemon.update()
		
	# Update the game state
	# Check if either Pokémon has fainted
	if player_pokemon.is_fainted():
		# Check if the player has any remaining Pokémon
		if len(player_party) > 1:
			player_party.pop(0)
			player_pokemon = player_party[0]
		else:
			# The player has lost the battle
			print("You have no remaining Pokémon!")
			break
	if opponent_pokemon.is_fainted():
		# Check if the opponent has any remaining Pokémon
		if len(opponent_party) > 1:
			opponent_party.pop(0)
			opponent_pokemon = opponent_party[0]
		else:
			# The player has won the battle
			print("You have defeated the opponent!")
			break
	
	# Render the battle screen
	screen.fill((255, 255, 255))
	draw_pokemon(player_pokemon, (50, 50))
	draw_pokemon(opponent_pokemon, (550, 50))
	if opponent_pokemon.is_fainted():
		print(opponent_pokemon.name + " Fainted!")

	pygame.display.flip()
