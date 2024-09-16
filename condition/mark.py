while True:
    try:
        a = int(input("Enter an integer value: "))
        if a < 0 or a > 100:
            print("Invalid integer. Please enter a value between 0 and 100.")
        else:
            if a < 35:
                print("You have failed.")
            elif a <= 69:
                print("Average")
            elif a <= 90:
                print("Good Student")
            else:
                print("Excellent Student")
            break
    except ValueError:
        print("Invalid input. Please enter an integer value.")
