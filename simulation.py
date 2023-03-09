#!/usr/bin/python3
from pokeclass import Pokemon
import random

# Set up Pygame and the window
# Load the player's party of Pokémon
# Load the opponent's party of Pokémon
# Set up the current Pokémon for each trainer

# Set up the battle loop
wins = []
games=int(input("How many games to play? "))
for i in range(games):
	opponent_party = [Pokemon.Bulbasaur(), Pokemon.Caterpie(), Pokemon.Weedle()]
	player_party = [Pokemon.pikachu(), Pokemon.Squirtle(), Pokemon.Charmander()]
	player_pokemon = player_party[0]
	opponent_pokemon = opponent_party[0]

	while True:
		opponent_party[0].level = 100
		player_party[0].level = 50
		if player_party[0].is_fainted() is not True or opponent_party[0].is_fainted() is not True:
			if random.randrange(1, 100, 1) > 50:
				player_party[0].use_move(random.choice(player_party[0].moves), opponent_party[0])
				opponent_party[0].use_move(random.choice(opponent_party[0].moves), player_party[0])
			else:
				opponent_party[0].use_move(random.choice(opponent_party[0].moves), player_party[0])
				player_party[0].use_move(random.choice(player_party[0].moves), opponent_party[0])
		# Update the game state
		# Check if either Pokémon has fainted
		if player_pokemon.is_fainted():
			# Check if the player has any remaining Pokémon
			if len(player_party) > 1:
				player_party.pop(0)
				player_pokemon = player_party[0]
			else:
				wins.append('opp')
				break
		if opponent_pokemon.is_fainted():
			# Check if the opponent has any remaining Pokémon
			if len(opponent_party) > 1:
				opponent_party.pop(0)
				opponent_pokemon = opponent_party[0]
			else:
				# The player has won the battle
				wins.append('pla')
				break

print(wins)
