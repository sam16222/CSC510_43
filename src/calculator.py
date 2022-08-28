import operations

def calculator():

    print("Select operation:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    
    while True:

        operator = input("Enter choice (+, -, *, /): ")

        if operator in ('+', '-', '*', '/'):
            
            num1 = int(input('First operand: '))
            num2 = int(input('Second operand: '))
            if operator == '+':
                print('{} + {} = '.format(num1, num2))
                print(operations.add(num1,num2))

            elif operator == '-':
                print('{} - {} = '.format(num1, num2))
                print(operations.subtract(num1,num2))

            elif operator == '*':
                print('{} * {} = '.format(num1, num2))
                print(operations.multiply(num1,num2))

            elif operator == '/':
                print('{} / {} = '.format(num1, num2))
                print(operations.divide(num1,num2))

            again = input("Calculate again? (Y/N): ")
            if again == "N":
                break
        else: 
            print("Invalid Input!")


# Function call to calculator
calculator()