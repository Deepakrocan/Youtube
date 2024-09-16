def is_odd_or_even(number):
    if number & 1 == 0:
        print("இலட்சியம் எண்")
    else:
        print("சம எண்")

num = int(input("ஒரு எண்ணை உள்ளிடவும்: "))
result = is_odd_or_even(num)
print(f"எண் {result} ஆகும்")
