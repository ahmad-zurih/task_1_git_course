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
# solution by Michael, copied from Henrique


# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.


# Task 2: Interactive user input

print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == "1":
    print(add(num1, num2))

elif operation == "2":
    print(subtract(num1, num2))

elif operation == "3":
    print(multiply(num1, num2))

elif operation == "4":
    print(divide(num1, num2))

else:
    print("Invalid operation")


# Task 3: Add a new file to the repo with other code of your choice

