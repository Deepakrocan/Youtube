# add/sub/div/mul all were having declaring 
def add():
    print('Addition')
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("The sum is:", a + b)

def sub():
    print("Subtraction")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print('The result is:', a - b)

def mul():
    print("Multiplication")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print('The result is:', a * b)

def div():
    print("Division")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    if b != 0:
        print('The result is:', a / b)
    else:
        print("Error: Division by zero.")

# Get user input for selecting operation
operation = input("Enter operation (add/sub/mul/div): ")

# Perform the selected operation
if operation == 'add':
    add()
elif operation == 'sub':
    sub()
elif operation == 'mul':
    mul()
elif operation == 'div':
    div()   
else:
    print("Invalid operation.")
