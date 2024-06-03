class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5

    def feed(self):
        self.hunger -= 1
        if self.hunger < 0:
            self.hunger = 0
        print(f"You fed {self.name}. Hunger level: {self.hunger}")

    def play(self):
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10
        print(f"You played with {self.name}. Happiness level: {self.happiness}")

    def get_status(self):
        print(f"{self.name}'s Hunger: {self.hunger}, Happiness: {self.happiness}")

def virtual_pet_game():
    pet_name = input("What is your pet's name? ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Check Status")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.get_status()
        elif choice == "4":
            print(f"Goodbye! Take care of {pet.name}!")
            break
        else:
            print("Invalid choice. Please try again.")

# Play the game
virtual_pet_game()
