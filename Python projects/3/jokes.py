import random

def random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you get when you cross a snowman and a vampire? Frostbite."
    ]
    print("Here's a random joke for you:")
    print(random.choice(jokes))

# Generate a random joke
random_joke()
