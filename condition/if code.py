salary = int(input("enter you salary :"))
age = int(input("enter you age :"))
if salary>=20000 or age<=25:
    print("you are eligible for loan")
    loan = int(input("Enter a loan required :"))
    if loan<=50000:
        print("Maximum loan amount is 50,000")
    else:
        print("you are eligible for ")
else:
    print("you are not eligible for loan")


score = int(input("Enter a score :"))
if score>=70:
    name = input("enter you name :")
    age  = int(input("enter a you age :"))
    address = input("enter a address :") 
    print("you are eligible ")
else:
    print("You not eligible ")

