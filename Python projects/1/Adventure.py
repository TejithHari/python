def play_text_adventure():
    print("Welcome to the Text Adventure Game!")
    print("You wake up in a mysterious room with three doors: red, blue, and green.")
    choice = input("Which door do you choose? ").lower()

    if choice == "red":
        print("You enter the red door and find a treasure chest. Congratulations, you win!")
    elif choice == "blue":
        print("You enter the blue door and fall into a pit. Game over!")
    elif choice == "green":
        print("You enter the green door and encounter a friendly dragon. You become friends!")
    else:
        print("Invalid choice. Please choose red, blue, or green.")

# Play the game
play_text_adventure()
