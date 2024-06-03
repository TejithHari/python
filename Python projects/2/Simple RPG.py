import random

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacks {enemy} and deals {damage} damage.")
        return damage

# Enemy class
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacks {player.name} and deals {damage} damage.")
        return damage

# Game function
def play_rpg():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    enemy = Enemy("Goblin", 50, 5)

    print(f"Welcome, {player.name}, to the Simple RPG Game!")
    print("You encounter a Goblin. Prepare to fight!")

    while player.health > 0 and enemy.health > 0:
        print(f"{player.name} - Health: {player.health}")
        print(f"{enemy.name} - Health: {enemy.health}")

        # Player attacks
        enemy.health -= player.attack("Goblin")
        if enemy.health <= 0:
            print("Congratulations! You defeated the Goblin!")
            break

        # Enemy attacks
        player.health -= enemy.attack(player)
        if player.health <= 0:
            print("Game Over! You were defeated by the Goblin.")
            break

# Play the game
play_rpg()
