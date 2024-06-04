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
def exponentiation(x, y):
    return x**y

# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
operator = input("Enter a operator (+,-,*,/,**): ")
if operator == "+":
    result = add(x, y)
elif operator == "-":
    result = subtract(x, y)
elif operator == "*":
    result = multiply(x, y)
elif operator == "/":
    result = divide(x, y)
else:
    result = exponentiation(x, y)

# Task 3: Add a new file to the repo with other code of your choice

