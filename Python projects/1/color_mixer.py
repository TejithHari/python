import turtle

def mix_colors():
    print("Welcome to the Color Mixer!")
    print("Mix primary colors (red, blue, yellow) to create secondary colors.")
    
    color1 = input("Enter the first primary color: ").lower()
    color2 = input("Enter the second primary color: ").lower()

    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        result = "purple"
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        result = "orange"
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        result = "green"
    else:
        result = "unknown"

    print(f"The result of mixing {color1} and {color2} is: {result}")

# Mix colors
mix_colors()
