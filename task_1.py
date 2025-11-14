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

def exponential(x, y):
    return x ** y  # x raised to the power of y



# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.



# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.

# Task 2: Interactive user input
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")

    choice = input("Enter choice (1/2/3/4/5): ")

    # Validate choice
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice.")
        return

    # Get numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform calculation
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    elif choice == "5":
        print("Result:", exponent(num1, num2))


# Run the calculator
calculator()

# Task 3: Add a new file to the repo with other code of your choice

