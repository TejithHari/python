import random,time
print('Welcome to Word Guesser!')
words = ["apple", "banana", "orange", "chair", "table"]
secret_word = random.choice(words)
# Create an empty list to store the displayed word with dashes
displayed_word = ["-" for _ in secret_word]
# Number of guesses allowed
guesses_left = 6

while True:
    while guesses_left > 0 and "-" in displayed_word:
        guess = input("Guess a letter: ").lower()  # Convert guess to lowercase

        # Check if guess is a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue

        # Check if the guess is in the secret word
        if guess in secret_word:
            # Update displayed word with the guessed letter
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    displayed_word[i] = guess
        else:
            guesses_left -= 1
            print("Wrong guess. You have", guesses_left, "guesses left.")

        # Print the current state of the word
        print(" ".join(displayed_word))
    if "-" not in displayed_word:
        print("Congratulations! You guessed the word:", secret_word)
        time.sleep(5)
        break
    else:
        print("You ran out of guesses. The word was:", secret_word)
        time.sleep(5)


        res = input('Do you want to exit?(y|n)')
        if res == 'y':
            break
