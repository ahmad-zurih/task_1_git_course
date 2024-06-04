# This is a simple calculator program.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:  # Check for division by zero
        return x / y
    else:
        return "Cannot divide by zero."

# Task 1: Implement a function for Exponentiation operation
def exponentiation(x, y):
    return x ** y

# Helper function to process operations
def process_operation(operation, x, y):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'exponentiation': exponentiation
    }
    func = operations.get(operation)
    if func:
        return func(x, y)
    return "Invalid operation"

# Task 2: Create an interactive user input for the calculator
def choice():
    operation = input("What operation do you wish to run? add, subtract, multiply, divide, or exponentiation? ")
    x = float(input("Enter your first number: "))  # Convert input to float
    y = float(input("Enter your second number: "))  # Convert input to float
    result = process_operation(operation, x, y)
    print(f"Result: {result}")

# Execute the interactive choice function
if __name__ == "__main__":
    choice()

# Task 3: Add a new file to the repo with other code of your choice

