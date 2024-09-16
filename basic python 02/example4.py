# Initialize counters for even and odd numbers
e_count=0
o_count=0

# Loop through numbers from 1 to 10
for i in range(1,10):
# Check if the number is even or odd
    if(i%2==0):
        e_count =e_count+1
    else:
        o_count=o_count+1
# Print the counts
print(e_count)
print(o_count)