import tkinter as tk

def calculate():
    try:
        result.set(eval(expression.get()))
    except:
        result.set("Error")

# Create the main window
window = tk.Tk()
window.title("Advanced Calauater")

# Create input field for expression
expression = tk.StringVar()
entry = tk.Entry(window, textvariable=expression, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Create buttons for digits and operators
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0
for button in buttons:
    tk.Button(window, text=button, font=("Arial", 18), width=5, height=2, command=lambda b=button: expression.set(expression.get() + b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create button for clearing the expression
tk.Button(window, text="C", font=("Arial", 18), width=5, height=2, command=lambda: expression.set("")).grid(row=row, column=0, columnspan=2, padx=5, pady=5)

# Create button for calculating the expression
result = tk.StringVar()
result.set("")
tk.Button(window, text="=", font=("Arial", 18), width=5, height=2, command=calculate).grid(row=row, column=2, columnspan=2, padx=5, pady=5)

# Create label for displaying the result
label = tk.Label(window, textvariable=result, font=("Arial", 18), anchor="e", width=15)
label.grid(row=row+1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Run the application
window.mainloop()
