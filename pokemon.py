import random
import filehandler


# noinspection PyTypeChecker
class Pokemon(object):
    def __init__(self, health, player, accuracy, entry):
        self.entry = entry
        self.health = 100
        self.accuracy = 100
        self.moves = filehandler.FileHandler.read(filehandler.FileHandler, "dex.json")
        self.moves = self.moves["pokedex"][entry-1]
        if len(self.moves["type"]) == 2:
            print(self.moves["type"])
            typing = self.moves["type"][0]
            self.moves["type"] = typing

    def attack(self, player):
        if random.randrange(1, 100) > self.accuracy:
            print("You Missed!")
        if self.moves["type"] == "dragon" or self.moves["type"] == player.moves["type"]:
            print("Dealt Neutral Damage.")
        elif (player.moves["type"] == "water" or player.moves["type"] == "ground" or player.moves["type"] == "rock") and self.moves["type"] == "grass":
            print("Super Effective!")
        elif (player.moves["type"] == "fire" or player.moves["type"] == "rock" or player.moves["type"] == "ground") and self.moves["type"] == "water":
            print("Super Effective!")
        elif (player.moves["type"] == "grass" or player.moves["type"] == "bug" or player.moves["type"] == "ice" or player.moves["type"] == "steel") and self.moves["type"] == "fire":
            print("Super Effective!")
        elif (player.moves["type"] == "water" or player.moves["type"] == "flying") and self.moves["type"] == "electric":
            print("Super Effective!")
        elif (player.moves["type"] == "grass" or player.moves["type"] == "ground" or player.moves["type"] == "flying" or player.moves["type"] == "dragon") and self.moves["type"] == "ice":
            print("Super Effective!")
        elif (player.moves["type"] == "Normal" or player.moves["type"] == "ice" or player.moves["type"] == "rock" or player.moves["type"] == "dark" or player.moves["type"] == "steel") and self.moves["type"] == "fighting":
            print("Super Effective!")
        elif (player.moves["type"] == "grass" or player.moves["type"] == "fairy") and self.moves["type"] == "poison":
            print("Super Effective!")
        elif (player.moves["type"] == "fire" or player.moves["type"] == "electric" or player.moves["type"] == "poison" or player.moves["type"] == "rock" or player.moves["type"] == "steel") and self.moves["type"] == "ground":
            print("Super Effective!")
        elif (player.moves["type"] == "grass" or player.moves["type"] == "fighting" or player.moves["type"] == "bug") and self.moves["type"] == "flying":
            print("Super Effective!")
        elif (player.moves["type"] == "fighting" or player.moves["type"] == "poison" or player.moves["type"]) and self.moves["type"] == "psychic":
            print("Super Effective!")
        elif (player.moves["type"] == "grass" or player.moves["type"] == "psychic" or player.moves["type"] == "dark") and self.moves["type"] == "bug":
            print("Super Effective!")
        elif (player.moves["type"] == "fire" or player.moves["type"] == "ice" or player.moves["type"] == "flying" or player.moves["type"] == "bug") and self.moves["type"] == "rock":
            print("Super Effective!")
        elif (player.moves["type"] == "psychic" or player.moves["type"] == "ghost") and self.moves["type"] == "dark":
            print("Super Effective!")
        elif player.moves["type"] == "dragon" and self.moves["type"] == "dragon":
            print("Super Effective!")
        elif (player.moves["type"] == "psychic" or player.moves["type"] == "ghost") and self.moves["type"] == "dark":
            print("Super Effective!")
        elif (player.moves["type"] == "ice" or player.moves["type"] == "rock" or player.moves["type"] == "fairy") and self.moves["steel"]:
            print("Super Effective!")
        elif (player.moves["type"] == "fighting" or player.moves["type"] == "dragon" or player.moves["type"] == "dark") and self.moves["type"] == "fairy":
            print("Super Effective!")
        elif (self.moves["type"] == "fire" or self.moves["type"] == "grass" or self.moves["type"] == "ice" or self.moves["type"] == "bug" or self.moves["type"] == "steel" or self.moves["type"] == "fairy") and player.moves["type"] == "fire":
            print("Not Very Effective..")
        elif (self.moves["type"] == "fire" or self.moves["type"] == "water" or self.moves["type"] == "ice" or self.moves["type"] == "steel") and player.moves["type"] == "water":
            print("Not Very Effective..")
        elif (self.moves["type"] == "electric" or self.moves["type"] == "flying" or self.moves["type"] == "steel") and player.moves["type"] == "electric":
            print("Not Very Effective..")
        elif (self.moves["type"] == "water" or self.moves["type"] == "electric" or self.moves["type"] == "grass" or self.moves["type"] == "ground") and player.moves["type"] == "grass":
            print("Not Very Effective..")
        elif self.moves["type"] == "ice" and player.moves["type"] == "ice":
            print("Not Very Effective..")
        elif (self.moves["type"] == "bug" or self.moves["type"] == "rock" or self.moves["type"] == "dark") and player.moves["type"] == "fighting":
            print("Not Very Effective..")
        elif (self.moves["type"] == "grass" or self.moves["type"] == "fighting" or self.moves["type"] == "poison" or self.moves["type"] == "bug" or self.moves["type"] == "fairy") and player.moves["type"] == "poison":
            print("Not Very Effective..")
        elif (self.moves["type"] == "poison" or self.moves["type"] == "rock") and player.moves["type"] == "ground":
            print("Not Very Effective..")
        elif (self.moves["type"] == "grass" or self.moves["type"] == "fighting" or self.moves["type"] == "bug") and player.moves["type"] == "flying":
            print("Not Very Effective..")
        elif (self.moves["type"] == "fighting" or self.moves["type"] == "psychic") and player.moves["type"] == "psychic":
            print("Not Very Effective..")
        elif (self.moves["type"] == "grass" or self.moves["type"] == "fighting" or self.moves["type"] == "ground") and player.moves["type"] == "bug":
            print("Not Very Effective..")
        elif (self.moves["type"] == "normal" or self.moves["type"] == "fire" or self.moves["type"] == "poison" or self.moves["type"] == "flying") and player.moves["type"] == "rock":
            print("Not Very Effective..")
        elif (self.moves["type"] == "normal" or self.moves["type"] == "fighting" or self.moves["type"] == "poison" or self.moves["type"] == "bug") and player.moves["type"] == "ghost":
            print("Not Very Effective..")
        elif (self.moves["type"] == "fire" or self.moves["type"] == "water" or self.moves["type"] == "electric" or self.moves["type"] == "grass") and player.moves["type"] == "dragon":
            print("Not Very Effective..")
        elif (self.moves["type"] == "psychic" or self.moves["type"] == "ghost" or self.moves["type"] == "dark") and player.moves["type"] == "dark":
            print("Not Very Effective..")
        elif (self.moves["type"] == "normal" or self.moves["type"] == "grass" or self.moves["type"] == "ice" or self.moves["type"] == "poison" or self.moves["type"] == "flying" or self.moves["type"] == "psychic" or self.moves["type"] == "bug" or self.moves["type"] == "rock" or self.moves["type"] == "dragon" or self.moves["type"] == "steel" or self.moves["type"] == "fairy") and player.moves["type"] == "steel":
            print("Not Very Effective..")
        elif (self.moves["type"] == "fighing" or self.moves["type"] == "bug" or self.moves["type"] == "dragon" or self.moves["type"] == "dark") and player.moves["type"] == "fairy":
            print("Not Very Effective..")
        else:
            print("Dealt Neutral Damage")
