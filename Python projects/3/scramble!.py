import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def word_scramble_game():
    words = ["python", "turtle", "computer", "programming", "game"]
    word = random.choice(words)
    scrambled_word = scramble_word(word)
    
    print("Welcome to the Word Scramble Game!")
    print("Unscramble the letters to form a word.")
    print("Scrambled word:", scrambled_word)

    guess = input("Your guess: ").lower()

    if guess == word:
        print("Correct! You guessed the word.")
    else:
        print("Wrong! The correct word was:", word)

# Play the game
word_scramble_game()

