import random

def roll_dice(num_dice, num_sides):
    print("Rolling", num_dice, "dice with", num_sides, "sides...")
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        print("Die", i+1, ":", roll)

# Get user input for number of dice and number of sides
num_dice = int(input("Enter the number of dice: "))
num_sides = int(input("Enter the number of sides per die: "))

# Roll the dice
roll_dice(num_dice, num_sides)
