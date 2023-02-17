import random
class Pokemon:
    def __init__(self, name, level, sprite_path):
        self.name = name
        self.level = level
        self.sprite_path = sprite_path
        self.moves = []
        self.stats = {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "sp_attack": 0,
            "sp_defense": 0,
            "speed": 0
        }
        
    def use_move(self, move, target):
        if move in self.moves:
            attack_stat = self.stats["attack"] if move.category == "Physical" else self.stats["sp_attack"]
            defense_stat = target.stats["defense"] if move.category == "Physical" else target.stats["sp_defense"]
            damage = (((2 * self.level / 5 + 2) * move.power * attack_stat / defense_stat) / 50) + 2
            target.stats["hp"] = max(0, target.stats["hp"] - damage)
            print(f"{self.name} used {move.name} on {target.name} and did {damage} damage.")
        else:
            print(f"{self.name} does not know {move.name}.")




        
    def Pikachu():
        pikachu = Pokemon("Pikachu", 5, "sprites/pikachu.png")
        pikachu.moves = [Thunderbolt(), QuickAttack(), TailWhip(), ThunderWave()]
        pikachu.stats = {
            "hp": 35,
            "attack": 55,
            "defense": 40,
            "sp_attack": 50,
            "sp_defense": 50,
            "speed": 90
        }
        return pikachu

    def Squirtle():
        squirtle = Pokemon("Squirtle", 5, "sprites/squirtle.png")
        squirtle.moves = [Tackle(), TailWhip(), WaterGun(), Bubble()]
        squirtle.stats = {
            "hp": 44,
            "attack": 48,
            "defense": 65,
            "sp_attack": 50,
            "sp_defense": 64,
            "speed": 43
        }
        return squirtle

    def Charmander():
        charmander = Pokemon("Charmander", 5, "sprites/charmander.png")
        charmander.moves = [Scratch(), Growl(), Ember(), MetalClaw()]
        charmander.stats = {
            "hp": 39,
            "attack": 52,
            "defense": 43,
            "sp_attack": 60,
            "sp_defense": 50,
            "speed": 65
        }
        return charmander

    def Bulbasaur():
        bulbasaur = Pokemon("Bulbasaur", 5, "sprites/bulbasaur.png")
        bulbasaur.moves = [Tackle(), Growl(), RazorLeaf(), SleepPowder()]
        bulbasaur.stats = {
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "sp_attack": 65,
            "sp_defense": 65,
            "speed": 45
        }
        return bulbasaur

    def Caterpie():
        caterpie = Pokemon("Caterpie", 5, "sprites/caterpie.png")
        caterpie.moves = [Tackle(), StringShot()]
        caterpie.stats = {
            "hp": 45,
            "attack": 30,
            "defense": 35,
            "sp_attack": 20,
            "sp_defense": 20,
            "speed": 45
        }
        return caterpie

    def Weedle():
        weedle = Pokemon("Weedle", 5, "sprites/weedle.png")
        weedle.moves = [PoisonSting(), StringShot()]
        weedle.stats = {
            "hp": 40,
            "attack": 35,
            "defense": 30,
            "sp_attack": 20,
            "sp_defense": 20,
            "speed": 50
        }
        return weedle

    def update(self):
        # Update the Pokémon's state or any other game logic here
        pass

    def is_fainted(self):
        return self.stats["hp"] == 0

class Move:
    def __init__(self, name, type, category, power, accuracy):
        self.name = name
        self.type = type
        self.category = category  # Added category attribute
        self.power = power
        self.accuracy = accuracy
def Thunderbolt():
    return Move("Thunderbolt", "Electric", "Special", 90, 100)

def QuickAttack():
    return Move("Quick Attack", "Normal", "Physical", 40, 100)

def TailWhip():
    return Move("Tail Whip", "Normal", "Status", 0, 100)

def ThunderWave():
    return Move("Thunder Wave", "Electric", "Status", 0, 100)

def Tackle():
    return Move("Tackle", "Normal", "Physical", 50, 100)

def WaterGun():
    return Move("Water Gun", "Water", "Special", 40, 100)

def Bubble():
    return Move("Bubble", "Water", "Special", 40, 100)

def Growl():
    return Move("Growl", "Normal", "Status", 0, 100)

def Ember():
    return Move("Ember", "Fire", "Special", 40, 100)

def MetalClaw():
    return Move("Metal Claw", "Steel", "Physical", 50, 95)

def Scratch():
    return Move("Scratch", "Normal", "Physical", 40, 100)

def RazorLeaf():
    return Move("Razor Leaf", "Grass", "Physical", 55, 95)

def SleepPowder():
    return Move("Sleep Powder", "Grass", "Status", 0, 75)

def StringShot():
    return Move("String Shot", "Bug", "Status", 0, 95)

def PoisonSting():
    return Move("Poison Sting", "Poison", "Physical", 15, 100)
