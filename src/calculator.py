# Add two numbers
def add(x, y):
    return x + y

# Subtract two numbers
def subtract(x, y):
    return x - y

# Multiply two numbers
def multiply(x, y):
    return x * y

# Divide two numbers
def divide(x, y):
    if(y!=0):
        return x / y
    else:
        print("Invalid Divisor!")


def calculator():

    print("Select operation:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    
    while True:

        operator = input("Enter choice (+, -, *, /): ")
        num1 = int(input('First operand: '))
        num2 = int(input('Second operand: '))

        if operator in ('+', '-', '*', '/'):
            if operator == '+':
                print('{} + {} = '.format(num1, num2))
                print(add(num1,num2))

            elif operator == '-':
                print('{} - {} = '.format(num1, num2))
                print(subtract(num1,num2))

            elif operator == '*':
                print('{} * {} = '.format(num1, num2))
                print(multiply(num1,num2))

            elif operator == '/':
                print('{} / {} = '.format(num1, num2))
                print(divide(num1,num2))

            again = input("Calculate again? (Y/N): ")
            if again == "N":
                break
        else: 
            print("Invalid Input!")


# Function call to calculator
calculator()



