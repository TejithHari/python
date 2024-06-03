def fruit_shop():
    print("Welcome to the Fruit Shop Game!")
    fruits = {
        "apple": 3,
        "banana": 2,
        "orange": 4,
        "grape": 5,
        "dragonfruit": 10,
        "watermelon": 20
    }

    basket = {}
    
    while True:
        print("Available fruits and their prices:")
        for fruit, price in fruits.items():
            print(f"{fruit.capitalize()}: ${price}")

        choice = input("Enter the name of the fruit to buy or 'done' to finish: ").lower()
        
        if choice == "done":
            break
        elif choice in fruits:
            if choice in basket:
                basket[choice] += 1
            else:
                basket[choice] = 1
            print(f"Added one {choice} to your basket.")
        else:
            print("Sorry, we don't have that fruit.")

    total_cost = sum(fruits[fruit] * quantity for fruit, quantity in basket.items())
    print(f"Your total cost is: ${total_cost}")

# Play the Fruit Shop Game
fruit_shop()
