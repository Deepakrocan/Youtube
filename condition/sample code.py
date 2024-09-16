try:
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
except ValueError:
    print("Invalid input. Please enter integer values.")
    exit()

operation = input('add/sub/mult/div: ')

if operation == 'add':
    print("Your total is:", a + b)
elif operation == 'sub':
    print("Your total is:", a - b)
elif operation == 'mult':
    print("Your total is:", a * b)
elif operation == 'div':
    if b != 0:  # Check if the second number is not zero to avoid division by zero
        print("Your total is:", a / b)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operation. Please enter 'add', 'sub', 'mult', or 'div'.")
