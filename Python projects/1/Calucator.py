def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Error: Cannot divide by zero"
  else:
    return x / y

while True:
  num1 = float(input("Enter first number: "))
  operator = input("Enter operator (+, -, *, /): ")
  num2 = float(input("Enter second number: "))

  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    result = "Invalid operator"

  print("Result:", result)

  # Ask if user wants to continue
  choice = input("Do another calculation? (y/n): ")
  if choice != 'y':
    break

print("Calculator shutting down...")
