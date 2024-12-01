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




def exponentiate(x,y):
    return x**y

keep_running = True


def read_code():
    s = input("What operation do you want to do (+,-,*,/,^):")
    
    if s=='exit':
        global keep_running
        keep_running = False
        return 'Closing'
    
    x = input("First number:")
    y = input("Second number:")
    print('You entered: '+x+s+y)
    x=float(x)
    y=float(y)
    if s=='+':
        return add(x, y)
    elif s=='-':
        return subtract(x, y)
    elif s=='*':
        return multiply(x, y)
    elif s=='/':
        return divide(x, y)
    elif s=='^':
        return exponentiate(x, y)
    else:
        raise ValueError('Unknown operation')
    
while keep_running:
    print(read_code())

# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.

def exponentiate(x,y):
	return (x**y)


# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.

x = input("pick a number")
y = input("pick a exponent")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Welcome to the interactive calculator!")

while True:
    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))




# Task 3: Add a new file to the repo with other code of your choice

