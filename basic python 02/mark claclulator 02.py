# add to all subjecct value 
a=int(input("Enter the Subject1:"))
b=int(input("Enter the Subject2:"))
c=int(input("Enter the Subject3:"))
d=int(input("Enter the Subject4:"))
e=int(input("Enter the Subject5:"))
f=int(input("Enter the Subject6:"))
g=a+b+c+d+e+f
print(g)
#adding the mark and total mark 
mark_a=int(input("Enter the  Youe Mark:"))
mark_b=int(input("ENter the Total mark:"))  
operation=input("add/su/mul/div: ")
if(operation=="add"):
    print(mark_a+mark_b)
elif(operation=="sub"):
    print(mark_a-mark_b)
elif(operation=="mul"):
    print(mark_a*mark_b)
elif(operation=="div"):
    print(mark_b/mark_a)
else:
    print("Invalid mark")

# finding weathr your fail or pass

mark=int(input("Enter the calculation total mark:"))
if(mark%2==0):
    print("Your Pass")
else:
    print("Your fail")  