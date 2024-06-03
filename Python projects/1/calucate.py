def calculator_for_kids():
    print("Welcome to Calaculate!")
    print("Enter two numbers and choose an operation (add, subtract, multiply, divide).")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero!")
            return
    else:
        print("Invalid operation!")
        return

    print(f"The result is: {result}")

# Use the calculator
calculator_for_kids()
