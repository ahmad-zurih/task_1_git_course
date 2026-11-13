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



# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.
def exponentiation(x,y):
    return x ** y


# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")


# Task 3: Add a new file to the repo with other code of your choice

