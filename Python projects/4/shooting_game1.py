import random
import time

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def shoot(self, enemy):
        damage = random.randint(10, 30)
        print(f"{self.name} shoots and deals {damage} damage to the enemy.")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

class Enemy:
    def __init__(self, name, health=50):
        self.name = name
        self.health = health

    def attack(self, player):
        damage = random.randint(5, 15)
        print(f"{self.name} attacks and deals {damage} damage to {player.name}.")
        player.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")


def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    enemy = Enemy("Enemy")

    print("Welcome to the shooting game!")
    print("You have encountered an enemy.")
    print("Fight to survive!\n")

    while player.health > 0 and enemy.health > 0:
        print(f"Player Health: {player.health}")
        print(f"Enemy Health: {enemy.health}\n")
        action = input("Do you want to shoot (s) or dodge (d)? ")

        if action.lower() == 's':
            player.shoot(enemy)
        elif action.lower() == 'd':
            print("You attempt to dodge the enemy's attack.")
            time.sleep(1)
            if random.random() < 0.5:
                print("You successfully dodge the attack!")
            else:
                print("You failed to dodge the attack!")
                enemy.attack(player)
        else:
            print("Invalid action! Please choose 's' to shoot or 'd' to dodge.")

        if enemy.health > 0:
            enemy.attack(player)
        time.sleep(1)

    print("\nGame Over!")

if __name__ == "__main__":
    main()
