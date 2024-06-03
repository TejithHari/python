import random
import time

def simon_says():
    print("Welcome to Simon Says!")
    colors = ["red", "blue", "green", "yellow"]
    sequence = []

    while True:
        sequence.append(random.choice(colors))
        print("Watch the sequence:")
        for color in sequence:
            print(color)
            time.sleep(1)
            print("\033c", end="")  # Clear the screen

        for i in range(len(sequence)):
            guess = input("Enter the color: ").lower()
            if guess != sequence[i]:
                print("Wrong! Game Over.")
                print("The correct sequence was:", sequence)
                return

        print("Correct! Get ready for the next round.")

# Play the game
simon_says()
