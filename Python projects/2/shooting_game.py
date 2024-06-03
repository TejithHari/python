import random

def shooting_game():
    # Game settings
    max_position = 10
    attempts_left = 3
    target_position = random.randint(1, max_position)

    print("Welcome to the Shooting Game!")
    print(f"Try to hit the target by guessing its position (1 to {max_position}). You have {attempts_left} attempts.")

    # Game loop
    while attempts_left > 0:
        try:
            guess = int(input("Guess the target's position: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if guess < 1 or guess > max_position:
            print(f"Please guess a number between 1 and {max_position}.")
            continue

        attempts_left -= 1

        if guess == target_position:
            print("Hit! You've destroyed the target.")
            break
        else:
            print("Miss! Try again.")
            if attempts_left > 0:
                print(f"Attempts left: {attempts_left}")
            else:
                print("You've run out of attempts. Game over.")
                print(f"The target was at position {target_position}.")

if __name__ == "__main__":
    shooting_game()
