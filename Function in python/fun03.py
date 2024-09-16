def is_odd_or_even(number):
    if number&1==0:
        print("odd number")
    else:
        print("even number")
    
num = int(input("Enter a number: "))
result = is_odd_or_even(num)
print(f"The number is {result}")




