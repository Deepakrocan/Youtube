# Get the input from the user
name = input("Enter a you name :")

# Get a get input for age and error handling 
while True:
    user_input=(input("enter You Age :"))
    try:
        age=int(user_input)
        break
    except ValueError:
        print("Invalid number. Please enter the Valid number")

# PAssing the message for the user
print(f"Hello {name}. Are you {age} year old")
print(f"In 5 Year, you will be a {age + 5} year's old")


