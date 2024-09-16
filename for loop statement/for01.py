def multiplication_table(number):
    for i  in range(1,11):
        result = number *1
        print(f"{number} X {i} = {result} ")

# Example Usage
User_input = int(input("Enter the number to display :"))
multiplication_table(User_input)