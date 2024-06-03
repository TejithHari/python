import turtle
import random

# List of words for the game
words = ["apple", "banana", "orange", "grape", "strawberry", "pineapple"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to draw the hangman
def draw_hangman(errors):
    if errors == 1:
        # Draw head
        pass
    elif errors == 2:
        # Draw body
        pass
    elif errors == 3:
        # Draw left arm
        pass
    elif errors == 4:
        # Draw right arm
        pass
    elif errors == 5:
        # Draw left leg
        pass
    elif errors == 6:
        # Draw right leg
        pass

# Function to play the game
def play_hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6
    errors = 0
    
    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")
    
    while tries > 0:
        # Draw hangman
        draw_hangman(errors)
        
        # Display word with blanks for missing letters
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()
        
        guess = input("Enter a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
            if set(guessed_letters) == set(word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Incorrect guess!")
            tries -= 1
            errors += 1
            if tries == 0:
                print("Sorry, you ran out of tries. The word was:", word)
                break

# Play the game
play_hangman()
